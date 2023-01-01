import unittest
from translator import english_to_french,french_to_english

class TestTranslationModule(unittest.TestCase):
    def test_E2F(self):
        self.assertEqual(english_to_french("Hello world"),"Bonjour le monde")
        self.assertNotEqual(english_to_french("Bye"),"Bonjour")
        self.assertEqual(english_to_french("Gray skies"),"Ciel gris")
        self.assertEqual(english_to_french("Hello"),"Bonjour")
    def test_F2E(self):
        self.assertEqual(french_to_english("Grand ours"),"Great Bear")
        self.assertNotEqual(french_to_english("Ciel gris"),"White skies")
        # self.assertEqual(french_to_english("Exécuter plus rapidement"),"Run faster")
        self.assertEqual(french_to_english("Bonjour"),"Hello")
    
if __name__== "__main__":
    unittest.main()