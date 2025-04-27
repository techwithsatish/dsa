
# resources
# 1. https://leetcode.com/problems/remove-duplicates-from-sorted-array/
# 2. https://neetcode.io/solutions/remove-duplicates-from-sorted-array
    

import unittest
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if not nums:
            return 0
        
        l = 1
        for r in range(1, len(nums)):
            
            if nums[r] != nums[r-1]:
                nums[l] = nums[r]
                l += 1
                
        return l


# test cases

class TestRemoveDuplicates(unittest.TestCase):

    def test_example1(self):
        nums = [1, 1, 2]
        expected_k = 2
        expected_nums_prefix = [1, 2]
        
        sol = Solution()
        k = sol.removeDuplicates(nums)
        self.assertEqual(k, expected_k)
        self.assertEqual(nums[:k], expected_nums_prefix)

    def test_example2(self):
        nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
        expected_k = 5
        expected_nums_prefix = [0, 1, 2, 3, 4]
        
        sol = Solution()
        k = sol.removeDuplicates(nums)
        self.assertEqual(k, expected_k)
        self.assertEqual(nums[:k], expected_nums_prefix)
        
    def test_empty_array(self):
        nums = []
        expected_k = 0
        expected_nums_prefix = []
        
        sol = Solution()
        k = sol.removeDuplicates(nums)
        self.assertEqual(k, expected_k)
        self.assertEqual(nums[:k], expected_nums_prefix)

if __name__ == '__main__':
    unittest.main()