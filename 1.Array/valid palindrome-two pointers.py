"""
#resources:
1.https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/introduction-to-two-pointers-pattern

"""

# Two Pointers


import unittest
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
       """
        string_list = []
        for char in s:
            if char.isalnum():
                string_list.append(char)
        string = ''.join(string_list).lower()
        
        left = 0
        right = len(string) - 1
        while left < right:
            if string[left] != string[right]:
                return False
            left += 1
            right -= 1
        return True
    
    
class TestIsPalindrome(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        s = "A man, a plan, a canal: Panama"
        self.assertTrue(self.solution.isPalindrome(s))

    def test_example2(self):
        s = "race a car"
        self.assertFalse(self.solution.isPalindrome(s))

    def test_example3(self):
        s = " "
        self.assertTrue(self.solution.isPalindrome(s))

if __name__ == '__main__':
    unittest.main()
