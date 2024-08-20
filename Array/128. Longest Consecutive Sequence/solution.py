class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_len = 0
        for i in range(len(nums)):
            if nums[i]-1 not in nums_set:
                temp_len = 1
                a = nums[i]
                while a + 1 in nums_set:
                    temp_len += 1
                    a += 1
                max_len = max(temp_len,max_len)
        return max_len