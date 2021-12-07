import unittest
from machinetranslation.translator import englishToFrench, frenchToEnglish

class TestTranslatorModule(unittest.TestCase):

    def test_en_to_fr_with_null(self):
        result = englishToFrench(None)
        self.assertEqual(result,"")

    def test_fr_to_en_with_null(self):
        result = frenchToEnglish(None)
        self.assertEqual(result,"")

    def test_en_to_fr_with_hello(self):
        result = englishToFrench("Hello")
        self.assertEqual(result,"Bonjour")

    def test_fr_to_en_with_bonjour(self):
        result = frenchToEnglish("Bonjour")
        self.assertEqual(result,"Hello")

if __name__ == "__main__":
    unittest.main()
