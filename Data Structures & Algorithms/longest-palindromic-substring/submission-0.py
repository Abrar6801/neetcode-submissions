class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s)<=1:
            return s
        
        def expandFromMiddle(left,right):
            while left>=0 and right<len(s) and s[left]==s[right]:
                left-=1
                right+=1
            return s[left+1:right]
        
        maxString = s[0]

        for i in range(len(s)-1):
            odd = expandFromMiddle(i,i)
            even = expandFromMiddle(i,i+1)
            if len(odd) > len(maxString):
                maxString = odd
            if len(even) > len(maxString):
                maxString = even
        return maxString
        