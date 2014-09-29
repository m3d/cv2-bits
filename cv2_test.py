import unittest

import cv2
import numpy as np

class Cv2Test( unittest.TestCase ): 
    def testContours( self ):
        "does contours use 4 or 8 neighbors?"
        img = np.zeros([10,10,1], dtype=np.uint8)
        contours, hierarchy = cv2.findContours( img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE )
        self.assertEqual( len(contours), 0 )
        img[3][3] = 255
        contours, hierarchy = cv2.findContours( img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE )
        self.assertEqual( len(contours), 1 )
        img[4][4] = 255
        contours, hierarchy = cv2.findContours( img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE )
        self.assertEqual( len(contours), 1 )

    def testContours2( self ):
        # see http://stackoverflow.com/questions/3286024/is-there-any-official-place-to-find-opencv-article-references
        img = np.zeros([10,10,1], dtype=np.uint8)
        for i in xrange(3,8):
            img[i][3],img[i][7] = 255, 255
            img[3][i],img[7][i] = 255, 255            
        contours, hierarchy = cv2.findContours( img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE )
        self.assertEqual( len(contours), 2 )
        img[3][3] = 0
        img[3][4] = 0
        img[4][3] = 0
        contours, hierarchy = cv2.findContours( img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE )
        self.assertEqual( len(contours), 1 )
        img[4][4] = 255
        contours, hierarchy = cv2.findContours( img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE )
        self.assertEqual( len(contours), 2 )


    def testTargetContours( self ):
        img = cv2.imread( "target100.png" )
        gray = cv2.cvtColor( img, cv2.COLOR_BGR2GRAY )
        ret, binary = cv2.threshold( gray, 128, 255, cv2.THRESH_BINARY )
        kernel = np.ones((3,3),np.uint8)
        binary = cv2.erode(binary, kernel)
#        cv2.imshow('image', binary)
#        cv2.waitKey(0)
        contours, hierarchy = cv2.findContours( binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE )
        self.assertEqual( len(contours), 14 )

        cv2.drawContours(img, contours, 1, (0,255,0), 2)
        cv2.imwrite( "contour100.png", img )


if __name__ == "__main__":
    unittest.main()

#-------------------------------------------------------------------
# vim: expandtab sw=4 ts=4

