class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        def backtracking(i,subset):
            res.append(subset.copy())
            for j in range(i,len(nums)):
                if j>i and nums[j]==nums[j-1]:
                    continue
                subset.append(nums[j])
                backtracking(j+1,subset)
                subset.pop()
        backtracking(0,[])
        return res
        