class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []
        def backtracking(openBrackets,closedBrackets):
            if openBrackets == closedBrackets == n:
                res.append("".join(stack))
                return
            if openBrackets < n:
                stack.append("(")
                backtracking(openBrackets+1,closedBrackets)
                stack.pop()
            if closedBrackets < openBrackets:
                stack.append(")")
                backtracking(openBrackets,closedBrackets+1)
                stack.pop()
        backtracking(0,0)
        return res


        