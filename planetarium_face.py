"""
  Excercise for Planetarium
  - cut the green background from photobox 
               and replace it by Mars/Universe image
  usage:
     ./planetarium_face.py <filename>
"""
import sys
import cv2
import numpy as np

def cutFace( img, debug=False ):
  hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
  lower = np.array([70,100,100])
  upper = np.array([90,255,255])
  mask = cv2.inRange(hsv, lower, upper)
  contours, hierarchy = cv2.findContours( mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE )
  best, bestArea = None, 0
  for cnt in contours:
    area = cv2.contourArea(cnt)
    if area > bestArea:
      best = cnt
      bestArea = area
  mask = np.zeros(img.shape, np.uint8)
  cv2.drawContours(mask, [best], -1, (255,255,255), -1)    
#  if debug:
#    cv2.imshow( 'image', mask )
  gray = cv2.cvtColor( mask, cv2.COLOR_BGR2GRAY )
  ret, binary = cv2.threshold( gray, 0, 255, cv2.THRESH_OTSU )
  return binary

def testFrame( filename ):
  img = cv2.imread( filename, cv2.CV_LOAD_IMAGE_COLOR )
  mask = cutFace( img, debug=True )
  mask_inv = cv2.bitwise_not(mask)
  img2 = cv2.imread( "pozadi.jpg", cv2.CV_LOAD_IMAGE_COLOR )

  img1_fg = cv2.bitwise_and(img, img, mask = mask_inv)
  img2_fg = cv2.bitwise_and(img2, img2, mask = mask)
  dst = cv2.add(img1_fg,img2_fg)
  cv2.imshow( 'image', dst )  
  cv2.imwrite( "out.jpg", dst )
  cv2.waitKey(0)

if __name__ == "__main__":
  if len(sys.argv) < 2:
    print __doc__
    sys.exit(1)
  testFrame( sys.argv[1] )

