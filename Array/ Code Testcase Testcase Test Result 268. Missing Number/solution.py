class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return int((len(nums)+1)*(len(nums))/2-sum(nums))