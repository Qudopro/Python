"""Tokenizing a string and counting unique words"""
text = ('this is sample text with several words'
        ' this is more sample text with some different words')

word_counts = {}

#Count ocurrences of each unique word
for word in text.split():
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

print(f'{"WORD":<12}COUNT')
for word, count in word_counts.items():
    print(f'{word:<12}{count}')

print('\nNumber of unique words', len(word_counts))