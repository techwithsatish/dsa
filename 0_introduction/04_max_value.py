# https://www.structy.net/problems/max-value

def max_value(nums):
  max_num = float('-inf')

  for num in nums:
    if num > max_num:
      max_num = num

  return max_num


