class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        nums_set = set()
        ans = []
        for num in nums:
            if num in nums_set:
                ans.append(num)
            nums_set.add(num)
        return ans