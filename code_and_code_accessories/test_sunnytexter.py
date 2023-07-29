#Tests for sunnytexter.py
#Written before actually making the function, because that's a great habit!
import numpy as np
import unittest

from sunnytexter import sunnytexter

class TestTexter(unittest.TestCase):

    def test_smoke(self):
        ##Smoketest## 
        sunnytexter("emailuser.json","gmail.json")  #returns something, maybe
        return

    ##Edge tests##
    def emptyjson(self):
        #empty json file
        with self.assertRaises(ValueError):
            sunnytexter("empty.json","empty.json")

    def emailinvalid(self):
        #not an email in the email form
        with self.assertRaises(ValueError):
            sunnytexter("notemail.json","gmail.json")
            
if __name__ == '__main__':
    unittest.main()           
