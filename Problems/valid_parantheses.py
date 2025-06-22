class Solution:
    def isValid(self, s: str) -> bool:
        """
        Check if the input string s containing only '(', ')', '{', '}', '[' and ']' is valid.
        A string is valid if:
        1. Open brackets must be closed by the same type of brackets.
        2. Open brackets must be closed in the correct order.
        """
        assert isinstance(s, str), "Input must be a string"
        if not s:
            return AssertionError("Input string cannot be empty")
        stack = []
        bracket_map = {')': '(', ']': '[', '}': '{'}
        for char in s:
            if char in bracket_map.values():
                stack.append(char)
            elif char in bracket_map:
                if not stack or stack[-1] != bracket_map[char]:
                    return False
                stack.pop()
            else:
                continue
        return len(stack) == 0
    
# Example usage
print(Solution().isValid("()"))          # Output: True
print(Solution().isValid("(]"))          # Output: False
print(Solution().isValid("([)]"))        # Output: False
print(Solution().isValid("{[]}"))        # Output: True
print(Solution().isValid(""))            # Output: False