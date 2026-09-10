class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        numpad = {
            '2':'abc',
            '3':'def',
            '4':'ghi',
            '5':'jkl',
            '6':'mno',
            '7':'pqrs',
            '8':'tuv',
            '9':'wxyz'
        }
        def backtracking(index,comb):
            if len(comb) == len(digits):
                ans.append(comb[:])
                return
            for letter in numpad[digits[index]]:
                backtracking(index+1,comb+letter)
        ans = []
        if digits == "":
            return []
        backtracking(0,"")
        return ans
        