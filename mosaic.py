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

DESIRED_SIZE = 1200,800

def mosaic( csvFile ):
  result = None
  reader = csv.reader( open(csvFile) )
  for row in reader:
    filename = row[0]
    x, y, degAngle = [int(t) for t in row[1:]]
    img = cv2.imread( filename, cv2.CV_LOAD_IMAGE_COLOR )
    while True:
      a = math.radians(int(degAngle))
      M = np.float32( [[math.cos(a), math.sin(a), x],
                       [-math.sin(a),math.cos(a),y],
                       [0,0,1]])
      img2 = cv2.warpPerspective(img,M,DESIRED_SIZE)
      tmp = result
      if tmp != None:
        tmp = cv2.add(result,img2)
      else:
        tmp = img2
      cv2.imshow('result', tmp) 
      key = cv2.waitKey()
      if key == 2424832: # left
        x -= 1
      elif key == 2555904: # right
        x += 1
      elif key == 2490368: # up
        y -= 1
      elif key == 2621440: # down
        y += 1
#      elif key = 
      elif key == 113: # q turn clockwise
        degAngle += 1
      elif key == 97: # a turn anticlockwise
        degAngle -= 1
      elif key == 13:
        break
      elif key == 27: # ESC
        return None
      else:
        print key
    print "%s,%d,%d,%d" % (filename,x,y,degAngle)
    result = tmp
  return result

if __name__ == "__main__":
  if len(sys.argv) < 3:
    print __doc__
    sys.exit(1)
  img = mosaic( sys.argv[1] )
  if img != None:
    cv2.imwrite( sys.argv[2], img )

