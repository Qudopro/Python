"""Dynamically graphing frequencies of die rolls"""
from matplotlib import animation
import matplotlib.pyplot as plt
import random
import seaborn as sns

"""Function call once per animation frame
frame_number: next value from FuncAnimation's frames argument (don't use, but required)
rolls: The number of dice rolls per animation frame
faces: The dice face values used as labels along the graph's x-axis
frequencies: The list in which we summarize the dice frequencies"""
def update(frame_number, rolls, faces, frequencies):
    """Configures bar plot contents for each animation frame"""
    #Roll die and update frequencies
    for i in range(rolls):
        frequencies[random.randrange(1,7)-1] += 1
    #Reconfigure plot for update die frequencies
    plt.cla()           #Clear old contents of current Figure, before drawing new ones for the current animation frame
    axes = sns.barplot(x=values, y=frequencies, palette='bright')
    axes.set_title(f'Die frequencies for {sum(frequencies):,} Rolls')
    axes.set(xlabel='Die Value', ylabel='Frequency')
    axes.set_ylim(top=max(frequencies)*1.10)        #Scale y_axis by 10%

    #Display frequency & percentage above each patch (bar)
    for bar,frequency in zip(axes.patches, frequencies):
        text_x = bar.get_x() + bar.get_width()/2.0
        text_y = bar.get_height()
        text = f'{frequency:,}\n{frequency/sum(frequencies):.3%}'
        axes.text(text_x, text_y, text, ha='center', va='bottom')

number_of_frames = 10_000
rolls_per_frame = 600

sns.set_style('whitegrid')
figure = plt.figure('Rolling a Six-Sided Die')      #Figure for animation. The function's argument is the window's title
values = list(range(1,7))           #Die Faces for display on x_axis
frequencies=[0]*6                   #Six element list of die frequencies

#Configure & start animation that calls funciotn update
die_animation = animation.FuncAnimation(figure, update, repeat=False, frames=number_of_frames, interval=33, fargs=(rolls_per_frame, values, frequencies))   #Update dynamically
plt.show()          #Display window

"""
FuncAnimation arguments:
    -figure. The Figure object in which to display the animation
    -update. The function to call once per animation frame
    -repeat=False. Terminates the animation after the specified number of frames
    -frames=number_of_frames. The total number of animation frames. How many times FuncAnimation calls update
    -interval. The number of milliseconds between animation frames. Waits 33 milliseconds before making the next call to the function update
    -fargs. A tuple of other arguments to pass to the function update
    
"""
