import unittest
from translator import englishToFrench, frenchToEnglish

class TestE2F(unittest.TestCase):
   
    def test_englishToFrench(self):
        self.assertEqual(englishToFrench(''), '')
        self.assertNotEqual(frenchToEnglish('Hello'), 'Bonjour')

    def test_frenchToEnglish(self):
        self.assertEqual(frenchToEnglish(''), '')
        self.assertNotEqual(frenchToEnglish('Bonjour'), 'Hello')

if __name__=='__main__':
    unittest.main()
