"""
  Threshold with slide bar
  usage:
     ./threshold.py <filename>
"""
import sys
import cv2

import numpy as np

bins = np.arange(256).reshape(256,1)

# taken from c:\opencv\sources\samples\python2\hist.py 
def histogram(im):
    h = np.zeros((300,256,3))
    if len(im.shape) == 2:
        color = [(255,255,255)]
    elif im.shape[2] == 3:
        color = [ (255,0,0),(0,255,0),(0,0,255) ]
    for ch, col in enumerate(color):
        hist_item = cv2.calcHist([im],[ch],None,[256],[0,256])
        cv2.normalize(hist_item,hist_item,0,255,cv2.NORM_MINMAX)
        hist=np.int32(np.around(hist_item))
        pts = np.int32(np.column_stack((bins,hist)))
        cv2.polylines(h,[pts],False,col)
    y=np.flipud(h)
    return y 

def threshold( img ):
  gray = cv2.cvtColor( img, cv2.COLOR_BGR2GRAY )
  cv2.imshow('histogram', histogram( img )) 
  def update( level ):
    ret, binary = cv2.threshold( gray, level, 255, cv2.THRESH_BINARY )
    cv2.imshow( 'image', binary )
  ret, binary = cv2.threshold( gray, 0, 255, cv2.THRESH_OTSU )
  update( int(ret) )
  cv2.createTrackbar( "threshold", "image", 0, 256, update )
  cv2.setTrackbarPos( "threshold", "image", int(ret) )
  cv2.waitKey()
  cv2.destroyAllWindows()

if __name__ == "__main__":
  if len(sys.argv) < 2:
    print __doc__
    sys.exit(1)
  img = cv2.imread( sys.argv[1], cv2.CV_LOAD_IMAGE_COLOR )
  threshold( img )

