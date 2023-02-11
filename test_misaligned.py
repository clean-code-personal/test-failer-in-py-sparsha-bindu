import unittest
from misaligned import *
import re

class TestMisaligned(unittest.TestCase):

    def test_misaligned(self):
     #performs these checks and asserts that the length of the list is 25, which is the number of mappings that should be present
        color_map = print_color_map()
        assert len(color_map) == 25
        for i, color in enumerate(color_map):
            parts = color.split(" | ")
            self.assertEqual(int(parts[0]), i+1)  # Check that the first value starts from 1, not 0
            self.assertIn(parts[1],["White", "Red", "Black", "Yellow", "Violet"])
            self.assertIn(parts[2],["Blue", "Orange", "Green", "Brown", "Slate"])
        
print("All tests passed!")

if __name__ == '__main__':
    unittest.main()
