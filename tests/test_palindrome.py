import unittest

# Para detectar el directorio src
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.palindrome import is_palindrome

class TestPalindrome(unittest.TestCase):
    # Test para palindromo simple
    def test_simple_palindromes(self):
        self.assertTrue(is_palindrome("madam"))
        self.assertTrue(is_palindrome("racecar"))
        self.assertTrue(is_palindrome("level"))

    # Test para frases palíndromas
    def test_phrase_palindromes(self):
            self.assertTrue(is_palindrome("A man, a plan, a canal: Panama"))
            self.assertTrue(is_palindrome("Was it a car or a cat I saw?"))
            self.assertTrue(is_palindrome("No lemon, no melon"))
    
    # Test para casos no palíndromos
    def test_non_palindromes(self):
        self.assertFalse(is_palindrome("hello"))
        self.assertFalse(is_palindrome("python"))
        self.assertFalse(is_palindrome("This is not a palindrome"))

    # Test para casos edge
    def test_edge_cases(self):
        self.assertTrue(is_palindrome(""))
        self.assertTrue(is_palindrome("a"))
        self.assertTrue(is_palindrome("A"))

if __name__ == '__main__':
    unittest.main()