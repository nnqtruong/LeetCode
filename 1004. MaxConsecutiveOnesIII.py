class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        """
        U array of nums and k 0s could be replaced by 1s
        M 
        special cases 
            not list
            empty list
        P 
        1. Count most consecutive 1s, if 0, turn 0 to 1, k -=1
        2. Find 0s then find 1s
        
        """
        if not nums or len(nums) == 0:
            return 0
        
        curr = left = 0
        for right, n in enumerate(nums):
            if n == 0:
                k -= 1
            if k < 0:
                if nums[left]==0:
                    k += 1
                left += 1
            
            curr = max(curr, right - left + 1)
        return curr 