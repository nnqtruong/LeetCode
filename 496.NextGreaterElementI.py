class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        next_greater = {}

        for x in nums2:
            while stack and x>stack[-1]:
                next_greater[stack.pop()]=x
            stack.append(x)

        for x in stack:
            next_greater[x] = -1
        
        return [next_greater[x] for x in nums1]#Array #HashTable #Stack #MonotonicStack #Easy