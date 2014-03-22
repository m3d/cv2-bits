"""
  Composed image from multiple small images
  usage:
     ./mosaic.py <pattern.csv> <output filename>
  CSV:
     <filename>,<x>,<y>,<degAngle>
"""
import sys
import cv2
import numpy as np
import csv
import math

DESIRED_SIZE = 900,500

def mosaic( csvFile ):
  result = None
  reader = csv.reader( open(csvFile) )
  for row in reader:
    print row
    filename, x, y, degAngle = row
    img = cv2.imread( filename, cv2.CV_LOAD_IMAGE_COLOR )
    a = math.radians(int(degAngle))
    M = np.float32( [[math.cos(a), math.sin(a), x],
                     [-math.sin(a),math.cos(a),y],
                     [0,0,1]])
    img = cv2.warpPerspective(img,M,(900,500))
    if result != None:
#      result = cv2.addWeighted(result,0.7,img,0.3,0)
      result = cv2.add(result,img)
    else:
      result = img
  cv2.imshow('result', result) 
  cv2.waitKey()
  return result

if __name__ == "__main__":
  if len(sys.argv) < 3:
    print __doc__
    sys.exit(1)
  img = mosaic( sys.argv[1] )
  cv2.imwrite( sys.argv[2], img )

