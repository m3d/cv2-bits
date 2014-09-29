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


if __name__ == "__main__":
    unittest.main()

#-------------------------------------------------------------------
# vim: expandtab sw=4 ts=4

