class Solution:
    def numDecodings(self, s: str) -> int:
        # Not 0 or not string,check 1st character
        if not s or s[0] == "0":
            return 0
        # Define dp[i-1] (one_back) and dp[i-2] (two back)
        one_back = 1 #first number is not 0 so always at least 1 , dp[1]=1
        two_back = 1 #default, dp[0]=1, "1" is valid → one way to decode

        # Loop from 2nd character until the end of s
        for i in range(1,len(s)):
        # current is 0 every loop and adds one_back if one check is good, current += if two_back is good
            current = 0

            if s[i]!="0":
                current += one_back

            two_digits=s[i-1:i+1]
            if 10<=int(two_digits)<=26:
                current += two_back

            
        # move window: two_back = one_back, one_back = current 
            two_back = one_back #dp[i-1]
            one_back = current # dp[i]

        # return one_back
        return one_back