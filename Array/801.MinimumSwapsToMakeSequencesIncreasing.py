class Solution:
    def minSwap(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        #keep = min swaps if we do NOT swap at i
        #swap = min swaps if we DO swap at i
        keep = 0
        swap = 1 

        for i in range(1,n):
            new_keep = new_swap = float('inf')

            #both already stricly increasing
            if nums1[i]>nums1[i-1]and nums2[i] > nums2[i-1]:
                new_keep = min(new_keep,keep)
                new_swap =min(new_swap,swap+1)

            #swapping makes them strictly increasing
            if nums1[i] > nums2[i-1] and nums2[i]>nums1[i-1]:
                new_keep = min (new_keep,swap)
                new_swap=min(new_swap,keep+1)
            
            keep, swap = new_keep, new_swap
        return min(keep,swap)
