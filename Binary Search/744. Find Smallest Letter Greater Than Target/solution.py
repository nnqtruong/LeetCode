class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left, right = 0, len(letters) - 1
    
        # If target is greater or equal to the last element, we return the first element
        if target >= letters[right]:
            return letters[0]
        
        while left < right:
            mid = left + (right - left) // 2
            if letters[mid] > target:
                right = mid  # Search on the left half
            else:
                left = mid + 1  # Search on the right half
        
        return letters[left]