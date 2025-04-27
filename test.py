




# import unittest
# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         l, r = 0, len(s) - 1
#
#         while l < r:
#             while l < r and not self.alphaNum(s[l]):
#                 l += 1
#             while r > l and not self.alphaNum(s[r]):
#                 r -= 1
#             if s[l].lower() != s[r].lower():
#                 return False
#             l, r = l + 1, r - 1
#         return True
#
#     def alphaNum(self, c):
#         return (ord('A') <= ord(c) <= ord('Z') or
#                 ord('a') <= ord(c) <= ord('z') or
#                 ord('0') <= ord(c) <= ord('9'))
#
# class TestIsPalindrome(unittest.TestCase):
#     def setUp(self):
#         self.solution = Solution()
#
#     def test_example1(self):
#         s = "A man, a plan, a canal: Panama"
#         self.assertTrue(self.solution.isPalindrome(s))
#
#     def test_example2(self):
#         s = "race a car"
#         self.assertFalse(self.solution.isPalindrome(s))
#
#     def test_example3(self):
#         s = " "
#         self.assertTrue(self.solution.isPalindrome(s))
#
# if __name__ == '__main__':
#     unittest.main()
#

