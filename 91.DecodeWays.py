class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == "0":
            return 0
        
        #dp[i-2], dp[i-1]
        two_back = 1 #dp[0]
        one_back = 1 #dp[1]


        for i in range(1,len(s)):
            current = 0
            
            #One digit decode:
            if s[i] != "0":
                current += one_back

        
            #Two-digit decode:
            two_digit = int(s[i-1:i+1])
            if 10 <= two_digit <= 26:
                current += two_back
            
            #Shift window
            two_back = one_back
            one_back = current

        return one_back

