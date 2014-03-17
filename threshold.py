"""
  Threshold with slide bar
  usage:
     ./threshold.py <filename>
"""
import sys
import cv2

def threshold( img ):
  gray = cv2.cvtColor( img, cv2.COLOR_BGR2GRAY )
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

