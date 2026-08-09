class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i=0
        j=i+1
        res = 0
        temp_res = 1
        n = len(s)
        if n>0: 
            se = {s[0]}
            res =1 
        while i<j and i<n-1 and j<n:
            if s[j] not in se:
                se.add(s[j])
                temp_res+=1
                res= max(res,temp_res)
                j+=1
            else:
                i+=1
                j=i+1
                se = {s[i]}
                temp_res=1
        return res
        