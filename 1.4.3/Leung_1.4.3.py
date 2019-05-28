from __future__ import print_function
import matplotlib 
matplotlib.use('Agg')
import matplotlib.pyplot as plt 
import os.path
import numpy as np      # 'as' lets us use standard abbreviations
import make_mask

'''Read the image data'''
# Get the directory of this python script
directory = os.path.dirname(os.path.abspath(__file__)) 
# Build an absolute filename from directory + filename
filename = os.path.join(directory, 'woman.jpg')
# Read the image data into an array

'''Show the image data'''
# Create figure with 1 subplot
# Show the image data in a subplot
img = plt.imread(filename)

mask = make_mask.make_mask(100, 100, 4) 
height = len(img)
width = len(img[0])
for r in range(155):
    for c in range(width):
        if sum (img[r][c])>500:
            img[r][c]=[255, 0 ,255]
for r in range(420, 470):
    for c in range(130, 160):
        if sum (img[r][c])>500:
            img[r][c]=[255, 0 ,255]
# Saves the figure
fig, ax = plt.subplots(1, 2)
ax[0].imshow(img, interpolation='none')
ax[1].imshow(mask, interpolation='none')
fig.savefig('women2')

print(type(img))
print(img)
print(len(img))
