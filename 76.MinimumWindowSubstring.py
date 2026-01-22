class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        t_count = Counter(t)
        window = {}
        have = 0
        need = len(t_count)

        left = 0
        res = [-1,-1]
        res_len = float('inf')

        for right, ch in enumerate(s):
            window[ch] = window.get(ch,0)+1

            if ch in t_count and window[ch] ==t_count[ch]:
                have += 1
            
            while have == need:
                #update
                if (right - left +1) < res_len:
                    res = [left,right]
                    res_len = right - left +1

                #shrink from left
                window[s[left]] -= 1
                if s[left] in t_count and window[s[left]] < t_count[s[left]]:
                    have -=1 
                left +=1

        l, r = res
        return s[l:r+1] if res_len !=float('inf') else ""
