import unittest
from translator import english_to_french,french_to_english

class english_to_french(unittest.TestCase):
    def test1(self):
        self.assertTrue(english_to_french(''), '')  # test when a null imput is given and the output is not null.
        self.assertTrue(english_to_french('Hello'), 'Bonjour') # test when "Hello" is given as input the output is "Bonjour".
        

class french_to_english(unittest.TestCase):
    def test1(self):
        self.assertTrue(french_to_english(''), '')  # test when a null imput is given and the output is not null.
        self.assertTrue(french_to_english('Bonjour'),'Hello') # test when "Bonjour" is given as input the output is "Hello".
unittest.main()