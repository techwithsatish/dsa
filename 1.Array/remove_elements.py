
import unittest

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        l = 0
        
        for r in range(len(nums)):
            if val != nums[r]:
                nums[l] = nums[r]
                l += 1
        
        return l
    
class TestRemoveElement(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        nums = [3, 2, 2, 3]
        val = 3
        expected_nums = [2, 2]
        k = self.solution.removeElement(nums, val)
        self.assertEqual(k, 2)
        self.assertCountEqual(nums[:k], expected_nums)

    def test_example2(self):
        nums = [0, 1, 2, 2, 3, 0, 4, 2]
        val = 2
        expected_nums = [0, 1, 3, 0, 4]
        k = self.solution.removeElement(nums, val)
        self.assertEqual(k, 5)
        self.assertCountEqual(nums[:k], expected_nums)

    def test_all_elements_removed(self):
        nums = [1, 1, 1, 1]
        val = 1
        k = self.solution.removeElement(nums, val)
        self.assertEqual(k, 0)
        self.assertEqual(nums[:k], [])

    def test_no_elements_removed(self):
        nums = [4, 5, 6]
        val = 3
        k = self.solution.removeElement(nums, val)
        self.assertEqual(k, 3)
        self.assertCountEqual(nums[:k], [4, 5, 6])

    def test_empty_array(self):
        nums = []
        val = 0
        k = self.solution.removeElement(nums, val)
        self.assertEqual(k, 0)
        self.assertEqual(nums[:k], [])

    def test_single_element_remove(self):
        nums = [5]
        val = 5
        k = self.solution.removeElement(nums, val)
        self.assertEqual(k, 0)
        self.assertEqual(nums[:k], [])

    def test_single_element_keep(self):
        nums = [5]
        val = 3
        k = self.solution.removeElement(nums, val)
        self.assertEqual(k, 1)
        self.assertEqual(nums[:k], [5])

if __name__ == '__main__':
    unittest.main()