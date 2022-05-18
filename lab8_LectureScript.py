from Inft1004Lecture8 import *

"""
Boring stuff
Author: Dan
Date: 3/3/22
"""

def main():
    #read_and_display('rockbeach.png')
    #read_and_display('cityLine.png')
    
    #red_channel2('rockbeach.png')
    sunset('rockbeach.png', 0.6)


def red_channel2(image):
    # Take a copy of an image and set its green and blue channels to 0, leaving only the red channel
    # Copy the image
    newimage = np.array(image)  # A new array based on the initial array
    # Iterate though all the pixels in the new image
    for y in range(0, newimage.shape[0]):
        for x in range(0, newimage.shape[1]):
            rgb = newimage[y, x]    # An array of the r, g, and b of the pixel at (y, x)
            rgb[1] = 0   # Set the green channel to 0
            rgb[2] = 0  # Set the blue channel to 0
    plt.imshow(newimage)  # Display the image - from matplotlib.pyplot
    return newimage  # And return the new image


#red_channel2('rockbeach.png')

main()