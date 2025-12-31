class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        """
        U array of nums and k 0s could be replaced by 1s
        M 
        special cases 
            not list
            empty list
        P 
        1. sliding window approach with two pointers left and right
        2. iterate through nums with right pointer
            a. if nums[right] is 0, decrement k
            b. if k < 0, move left pointer to the right until k >= 0
        
        """
        best = left = 0
        for right, n in enumerate(nums):
            if n == 0:
                k -= 1
            if k < 0:
                if nums[left] == 0:
                    k += 1
                left += 1
            best = max(best, right - left + 1)
        return best