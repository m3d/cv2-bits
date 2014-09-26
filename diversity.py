"""
  Threshold with slide bar
  usage:
     ./threshold.py <filename>
"""
import sys
import cv2

import numpy as np

def diversity( img ):
    gray = cv2.cvtColor( img, cv2.COLOR_BGR2GRAY )
    for i in xrange(512):
        for j in xrange(639):
            if gray[i][j] > gray[i][j+1]:
                gray[i][j] = gray[i][j] - gray[i][j+1]
            else:
                gray[i][j] = gray[i][j+1] - gray[i][j]

    arr=[]
    for i in xrange(512):
        arr.append([])
        for j in xrange(639):
            arr[i].append( int(gray[i][j]) )
        arr[i].append( 0 )

    for i in xrange(512):
        for j in xrange(640):
            if j > 0:
                arr[i][j] = arr[i][j-1] + arr[i][j]

    for i in xrange(512):
        for j in xrange(640):
            if i > 0:
                arr[i][j] = arr[i-1][j] + arr[i][j]

    W,H = 20,20
    best = None
    for i in xrange(512-H):
        for j in xrange(640-W):
            val = arr[i][j] + arr[i+H][j+W] - arr[i+H][j] - arr[i][j+W]
            if best is None or val > best[0]:
                best = val, (i,j)
    print best

    val, (i,j) = best
    cv2.rectangle( img, (j,i), (j+W,i+H), (0,0,255), thickness=2 )

    cv2.imshow( 'image', img )
    cv2.imwrite( "diver.jpg", img )
    cv2.waitKey()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print __doc__
        sys.exit(1)
    img = cv2.imread( sys.argv[1], cv2.CV_LOAD_IMAGE_COLOR )
    diversity( img )

# vim: expandtab sw=4 ts=4

