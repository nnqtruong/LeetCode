class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if not s1 or not s2:
            return False

        m = len(s1)
        n = len(s2)
        if m > n:
            return False

        s1_counter = Counter(s1)
        window = Counter(s2[:m])

        if s1_counter == window:
            return True
        for i in range(1,n-m+1):
            left_char = s2[i-1]
            window[left_char] -= 1
            if window[left_char] == 0:
                del window[left_char]
            right_char =s2[i+m-1]
            window[right_char]+=1
            if window == s1_counter:
                return True

        return False
            
        