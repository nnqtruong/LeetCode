# #Array

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = curr = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                curr+=1
                if curr > count:
                    count = curr
            else:
                curr = 0
        return count