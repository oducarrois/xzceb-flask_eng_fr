import unittest
from translator import english_to_french
from translator import french_to_english

class TestE2F(unittest.TestCase):
    def test_english_to_french(self):
        self.assertEqual(english_to_french("Hello"), "Bonjour")

class TestF2E(unittest.TestCase):
    def test_french_to_english(self):
        self.assertEqual(french_to_english("Bonjour"), "Hello")


unittest.main()

#print (englishToFrench("Hello"))
#print (frenchToEnglish("Bonjour"))
