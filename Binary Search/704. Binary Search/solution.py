class Solution:
    def search(self, nums: List[int], target: int) -> int:
        min, max = 0, len(nums)-1
        while min<=max:
            mid = min+(max-min)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                min = mid +1
            else:
                max = mid-1
        return -1