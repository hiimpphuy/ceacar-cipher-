import unittest
from func import encode,decode

class test(unittest.TestCase):
    def testEncode(self):
        self.assertEqual(encode("aab",3), "dde")
    def testDecode(self):
        self.assertEqual(decode("dde",3), "aab")

if __name__ == "__main__":
    unittest.main()
