class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        positive_nums = [num for num in nums if num > 0]
        
        # Convert the list to a set for O(1) lookups
        positive_set = set(positive_nums)
        
        # Check for the first missing positive integer
        for i in range(1, len(positive_nums) + 2):  # +2 to include the case where all positives are present
            if i not in positive_set:
                return i