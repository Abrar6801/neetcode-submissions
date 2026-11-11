class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        used = set()
        n = len(nums)
        def dfs(currList):
            if len(currList) == n:
                res.append(currList.copy())
                return
            for num in nums:
                if num not in used:
                    currList.append(num)
                    used.add(num)
                    dfs(currList)
                    currList.pop()
                    used.remove(num)
        dfs([])
        return res
        

        