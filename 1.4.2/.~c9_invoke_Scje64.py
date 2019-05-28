#1
'''N/A'''
#2
'''N/A'''
#3
'''N/A'''
#4
'''C:/Users/Student Login/Desktop/nice.jpg'''
#5
'''admin..Users/Student Login/Desktop/nice.jpg'''
#6
'''These commands is different in cloud 9 because we have different directory
which meanas that the outcomes are different'''
#7
'''
JDoe_JSmith_1_4_2: Read and show an image.
'''
import matplotlib.pyplot as plt 
import os.path
import numpy as np      # 'as' lets us use standard abbreviations

'''Read the image data'''
# Get the directory of this python script
directory = os.path.dirname(os.path.abspath(__file__)) 
# Build an absolute filename from directory + filename
filename = os.path.join(directory, 'woman.jpg')
# Read the image data into an array
img = plt.imread(filename)

'''Show the image data'''
# Create figure with 1 subplot
fig, ax = plt.subplots(1, 1)
# Show the image data in a subplot
ax.imshow(img, interpolation='none')
# Show the figure on the screen
fig.show()
