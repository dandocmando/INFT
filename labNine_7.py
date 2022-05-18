"""
Boring stuff
Author: Dan
Date: 3/3/22
"""

import numpy as np
import Inft1004Lecture9BottomUp_v2 as ln
import matplotlib.image as mpimg
from PIL import Image

image = mpimg.imread('Campus0.png')
smpimg = mpimg.imread('SimpleImage.png')


def main(source):
    height = source.shape[0]
    width = source.shape[1]

    target = np.zeros((height * 2, width * 2, 3))

    target = ln.copy(ln.red_channel(source), target, 0, 0)
    target = ln.copy(negative_flip_vert(source), target, height, 0)
    target = ln.copy(greyscale_flip_horiz(source), target, 0, width)
    target = ln.copy(ln.flip_vert(ln.flip_horiz(ln.green_channel(source))), target, height, width)
    target = ln.copy(source, target, height // 2, width // 2)

    ln.display(target)


def showimage(source):
    target = non_weighted_grayscale(source)
    ln.display(target)


def compare_greys(source):
    height = source.shape[0]
    width = source.shape[1]

    target = np.zeros((height*4, width*4,3))
    print(target)
    
    
    target = ln.copy(ln.greyscale(source), target, 0, 0)
    target = ln.copy(non_weighted_grayscale(source), target, height, width)

    ln.display(target)


def negative_flip_vert(im):
    # flips vertically and turns image negative
    newimage = np.array(im)
    height = newimage.shape[0]  # Height is the first dimension
    width = newimage.shape[1]  # Width is the second dimension

    # Iterate though all the pixels in the new image
    for y in range(height):
        for x in range(width):
            rgb_source = im[y, x]  # An array of the r, g, and b of the pixel at (y, x)
            # Copy the rgb of the original pixel to the new location
            newimage[height - 1 - y, x] = rgb_source

    # negative image
    for y in range(height):
        for x in range(width):
            newimage[y, x] = 1 - newimage[y, x]  # Replace the pixel at (y, x) with its negative

    return newimage


def greyscale_flip_horiz(im):
    newimage = np.array(im)
    height = newimage.shape[0]
    width = newimage.shape[1]

    # flips image horizonatally
    for y in range(height):
        for x in range(width):
            rgb = im[y, x]
            newimage[y, width - 1 - x] = rgb

    # greyscales image
    for y in range(height):
        for x in range(width):
            rgb = image[y, x]
            grey = rgb[0] * .299 + rgb[1] * .587 + rgb[2] * .114
            newimage[y, x] = np.array([grey, grey, grey])

    return newimage


def non_weighted_grayscale(im):
    newimage = np.array(im)
    height = newimage.shape[0]
    width = newimage.shape[1]

    for y in range(height):
        for x in range(width):
            rgb = image[y, x]
            non_weighted_grey = (rgb[0] + rgb[1] + rgb[2]) / 3
            newimage[y, x] = np.array([non_weighted_grey, non_weighted_grey, non_weighted_grey])

    return newimage


main(image)
#showimage(image)
#compare_greys(smpimg)

