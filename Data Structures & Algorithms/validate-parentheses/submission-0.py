class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        hash_map = {')': '(', ']': '[', '}': '{'}

        for e in s:
            # if top value of stack is the open bracket of this bracket
            if stack and stack[-1] == hash_map.get(e):
                stack.pop()
            else:
                stack.append(e)

        return not stack # if stack empty -> true

        