class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        numZeros = 0
        for num in nums:
            if num:
                product *= num
            else:
                numZeros+=1
        if numZeros > 1: return [0]*len(nums)
        res = [0]*len(nums)        
        for i,num in enumerate(nums):
            if numZeros: 
                res[i] = 0 if num else product
            else:
                res[i] = product//num
        return res
        