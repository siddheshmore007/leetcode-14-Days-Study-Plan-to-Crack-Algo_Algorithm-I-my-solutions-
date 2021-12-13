class Solution:
  def search(self, nums: List[int], target: int) -> int:
    n = len(nums)
    i = 0
    j = n-1
    
    if i==0 and j==0:
      if nums[i] == target:
        return 0
    while(i<j):
      mid = floor((i+j+1)/2) - 1
      if target<nums[mid]:
        j=mid-1
        if nums[j] == target:
          return j
      elif target>nums[mid]:
        i=mid+1
         if nums[i] == target:
           return i
      elif target==nums[mid]:
        return mid
      else:
        return -1
    
    return -1
    
