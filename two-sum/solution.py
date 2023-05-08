from typing import List

class Solution(object):
  def twoSum(self, nums: List[int], target: int) -> List[int]:
    """
    Solution in Square Time: O(n²)
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
    """
    for i in range(len(nums)):
      for j in range(i+1, len(nums)):
          if nums[i] + nums[j] == target:
            return [i,j]
    return []

  def twoSumHashMap(self, nums: List[int], target: int) -> List[int]:
    """
      Solution in Linear Time: O(n)
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
    """
    hash_map = {}
    for i in range(len(nums)):
      sub = target - nums[i]
      if sub in hash_map.keys():
        return [hash_map[sub], i]
      else:
        hash_map[nums[i]] = i
    return []


solution = Solution()
print(solution.twoSum([2,7,11,15], 9))
print(solution.twoSum([3,2,4], 6))
print(solution.twoSumHashMap([3,2,4], 6))