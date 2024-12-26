import unittest
import capi

class TestCapiText(unittest.TestCase):

    def test_one_word(self):
        text = 'python'
        result = capi.capitalize_text(text)
        self.assertEqual(result, 'Python')

    def text_multiple_word(self):
        text = 'multi python'
        result = capi.capitalize_text(text)
        self.assertEqual(result, 'Multi Python')

if __name__ == "__main__":
    unittest.main()