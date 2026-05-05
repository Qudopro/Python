#SimpleLanguageTranslator.py
"""Use IBM Watson Speech to Text, Language Translator and Text to Speech APIs to enable English and Spanish speakers to communicate"""
from ibm_watson import SpeechToTextV1
#from ibm_watson import LanguageTranslatorV3
from ibm_watson import TextToSpeechV1

import keys         #Contains your API keys for accessing Watson services
import pyaudio      #Used to record from microphone
import pydub        #Used to load a WAV file
import pydub.playback       #Used to play a WAV file
import wave         #Used to save a WAV file

def run_translator():
    """Calls the functions that interact with Watson services"""
    #Step 1: Prompt for then record English speech into an audio file
    input('Press Enter then ask your question in English')
    record_audio('english.wav')             #Records audio for five seconds and stores it in the file english.wav

    #Step 2: Transcribe the English speech to English text (with Speech to Text Service)
    # Define which file transcription and We tell the Speech to Text Service to transcribe the text using its predefined model
    english = speech_to_text(file_name='english.wav', model_id='en-US_BroadbandModel')
    print('English:', english)                  #Display the transcribed text

    #Step 3: Translate the English text into Spanish text (with Language Translator Service)
    #We define the text to translate and its predefined model 'en-es' to translate from English to Spanish
    spanish =  translate(text_to_translate=english, model='en-es')
    print('Spanish:', spanish)

    #Step 4: Synthesize the Spanish text into Spanish speech
    #We pass the Spanish text and use its voice Sofia, then specify the file in which the audio should be saved
    text_to_speech(text_to_speak=spanish, voice_to_use='es-US_SofiaVoice', file_name='spanish.wav')

    #Step 5. Play the file audio
    play_audio(file_name='spanish.wav')

    #Step 6: Prompt for then record Spanish speech into an audio file
    input('Press Enter then speak the Spanish answer')
    record_audio('spanishresponse.wav')

    #Step 7: Transcribe the Spanish speech to Spanish text
    spanish = speech_to_text(file_name='spanishresponse.wav', model_id='es-ES_BroadbandModel')
    print('Spanish response:', spanish)

    #Step 8: Translate the Spanish text into English text
    english = translate(text_to_translate=spanish, model='es-en')
    print('English:', english)

    #Step 9: Synthesize the English text into English speech
    text_to_speech(text_to_speak=english, voice_to_use='en-US_AllisonVoice', file_name='englishresponse.wav')

    #Step 10: Play the English audio
    play_audio(file_name='englishresponse.wav')

def speech_to_text(file_name, model_id):
    """Use Watson Speech to Text to convert audio file to text"""
    #Create Watson Speech to Text client
    stt = SpeechToTextV1(iam_apikey=keys.speech_to_text_keys)

    #open the audio file
    with open(file_name, 'rb') as audio_file:
        # pass the file to Watson for transcription
        result = stt.recognize(audio=audio_file, content_type='audio/wav',model=model_id).get_result()           #Invoke the Speech to Text service

    #Recognize return a DetailedResponse. get_result returns a JSON document containing the transcribed text

    #Get the 'results' list.
    results_list = result['results']                    #Get all result of the transcript with key  results ({"results":[...]}. It contains nested dictrionaries and lists

    #Get the final speech recognition result -- the list's only element
    speech_recognition_result = results_list[0]             #Get the final transcription

    #Get the 'alternatives' list.
    alternatives_list = speech_recognition_result['alternatives']           #Get value of key alternatives [{"alternatives":[...]}]

    #Get the only alternative transcription from alternatives_list (which contains the transcript text)
    first_alternative = alternatives_list[0]

    #Get the 'transcript' key's value, which contains the audio's text transcription
    transcript = first_alternative['transcript']                    #[{"confidence":0.987, "transcript":"..."}]}]

    return transcript               #Return the audio's text transcription

def translate(text_to_translate, model):
    """Use Watson Language Translator to translate English to Spanish (en-es) or Spanish to English (es-en) as specified by model"""
    #Create Watson Tranlator Client
    language_translator = LanguageTranslatorV3(version="2018-05-31", iam_apikey=keys.language_translator_key)   #Use the service version and the API Key

    #Perform the translation
    translated_text = language_translator.translate(text=text_to_translate, model_id=model).get_result()      #Text to translate to another language and the model will use to understand the original text and translate it into the appropiate language

    #Translate returns a DetailedResponse and its method get_results returns a JSON document

    #Get 'translations' list.
    translations_list = translated_text['translations']             #{"translations":[...]}

    #Get translations_list's only element
    first_translation = translations_list[0]                #Get first translation... [{},{}]

    #Get 'translation' key's value, which is the translated text
    translation = first_translation['translation']          #{"translation":"..."}

    return translation

def text_to_speech(text_to_speak, voice_to_use, file_name):
    """Use Watson Text to Speech to convert text to specified voice and save to a WAV file"""
    #Create Text to Speech client
    tts = TextToSpeechV1(iam_apikey=keys.text_to_speech_key)

    #open file and write the synthesized audio content into the file
    with open(file_name, 'wb') as audio_file:
        audio_file.write(tts.synthesize(text_to_speak, accept='audio/wav', voice=voice_to_use).get_result().content)

        #Method synthesize invoke the Speech to Text service with the string to speak, the media type that Speech to Text service should return and the voice of the Speech to Text service
        #get_resutl contains the spoken text audio file.
        #content get the bytes of the audio to output the bytes to a .wav file

def record_audio(file_name):
    """Use pyaudio to record 5 seconds of audio to a WAV file"""
    FRAME_RATE = 44100          #Number of frames per second
    CHUNK = 1024                #Number of frames read at a time
    FORMAT = pyaudio.paInt16    #Each frame is a 15 bit integer
    CHANNELS = 2                #2 samples per frame
    SECONDS = 5                 #Total recording time

    recorder = pyaudio.PyAudio()            #opens/closes audio streams

    #Configure and open audio stream for recording (input = True indicates that the stream will be used to receive audio input)
    audio_stream = recorder.open(format=FORMAT,channels=CHANNELS,rate=FRAME_RATE,input=True,frames_per_buffer=CHUNK)            #Return a pyaudio Stream object for interacting with the stream

    audio_frames = []           #stores raw bytes of mic input
    print('Recording 5 seconds of audio...')

    #Read 5 seconds of audio in CHUNK-sized pieces
    for i in range(0, int(FRAME_RATE * SECONDS / CHUNK)):
        audio_frames.append(audio_stream.read(CHUNK))               #Get 1024 frames at a time from the input stream

    print('Recording done.')
    audio_stream.stop_stream()          #Stop recording
    audio_stream.close()            #Close the Stream object
    recorder.terminate()            #Release underlying resources used by PyAudio

    #Save audio_frames to a WAV file
    with wave.open(file_name, 'wb') as output_file:             #Open the WAV file for writing in binary format
        output_file.setnchannels(CHANNELS)                              #Configure number of channels of the file
        output_file.setsampwidth(recorder.get_sample_size(FORMAT))      #Sample width
        output_file.setframerate(FRAME_RATE)                            #Frame rate
        output_file.writeframes(b''.join(audio_frames))                 #Writes the audio content to the file, concatenates all the frames' bytes into a byte string: b'' -> string of bytes

def play_audio(file_name):
    """Use the pydub model to play a WAV file"""
    sound = pydub.AudioSegment.from_wav(file_name)                  #Load a WAV file. Returns a new AudioSegment object representing the audio file
    pydub.playback.play(sound)                                      #Play tha AudioSegment

if __name__ == '__main__':
    run_translator()

