class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        """
        u nums is a int array, minK is lower bound, maxK is upper bound
        m sliding window (subarray)
        p 
        
        compare each subarray to minK and maxK high complexity 

        start <= last_min
        start <= last_max

        so: start <= min(last_min,last_max)

        (last_bad + 1) <= start <= min(last_min,last_max)
        
        """
        last_min = -1 
        last_max = -1
        last_bad = -1
        ans = 0

        for i, n in enumerate(nums):
            if n < minK or n > maxK:
                last_bad = i
            if n == minK:
                last_min = i
            if n == maxK:
                last_max = i
            ans += max(0,min(last_min, last_max)-last_bad)

        return ans 
                
                

