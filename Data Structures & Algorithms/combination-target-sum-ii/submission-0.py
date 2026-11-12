class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def backtracking(index, currList, currSum):
            if currSum == target:
                res.append(currList.copy())
                return
            for i in range(index,len(candidates)):
                if i>index and candidates[i] == candidates[i-1]:
                    continue
                if currSum + candidates[i] > target:
                    break
                currList.append(candidates[i])
                backtracking(i+1,currList,currSum+candidates[i])
                currList.pop()
        backtracking(0,[],0)
        return res

        