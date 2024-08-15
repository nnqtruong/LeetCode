class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        index = 0
        for i in range(0,len(nums)):
            if nums[i] != 0:
                if index != i:
                    nums[index]=nums[i]
                    nums[i]=0
                index +=1
        """
        Do not return anything, modify nums in-place instead.
        """