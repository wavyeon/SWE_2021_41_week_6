from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
  ret = []
  for i in range (0, len(nums) - 1):
    for j in range (i+1, len(nums)):
      if(nums[i] + nums[j] == target):
        ret.append(i)
        ret.append(j)
  return ret
  