import scipy
import myscipy as myscipy
import unittest

class TestAdd(unittest.TestCase):
   
    def test_cbrt(self):
        result = myscipy.cuberoot(64)
        self.assertEqual(result,4.0)

    def test_comb(self):
        result = myscipy.comb(4)
        self.assertEqual(result, 4.0)


if __name__=='_main_':
    unittest.main()
