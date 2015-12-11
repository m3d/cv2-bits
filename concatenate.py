#!/usr/bin/python
"""
  Concatenate two images into one
  usage:
       ./concatenate.py <image1> <image2> <outputImage>
"""
import sys
import math
import os
import cv2
import numpy

def concatenate( img1, img2 ):
    return numpy.concatenate( (img1, img2), axis=1 )

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print __doc__
        sys.exit(2)
    result = concatenate(cv2.imread(sys.argv[1]), cv2.imread(sys.argv[2]))
    cv2.imwrite( sys.argv[3], result )

# vim: expandtab sw=4 ts=4 

