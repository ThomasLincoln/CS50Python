import unittest
from um import count

class TestCountFunction(unittest.TestCase):
    def test_um_appearance(self):
        
        text1 = "It's not uncommon, in English, at least, to say 'um' when trying to, um, think of a word."
        self.assertEqual(count(text1), 2)

        text2 = "hello, um, world"
        self.assertEqual(count(text2), 1)

        text3 = "yummy"
        self.assertEqual(count(text3), 0)

    def test_case_insensitivity(self):
        
        text1 = "UM is not the same as um, UM"
        self.assertEqual(count(text1), 1)

        text2 = "this is um, um"
        self.assertEqual(count(text2), 2)

if __name__ == '__main__':
    unittest.main()
