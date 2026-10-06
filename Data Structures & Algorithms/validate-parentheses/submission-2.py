class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for char in s:
            if char in ["(", "{", "["]:
                stack.append(char)
            else:
                if not stack:
                    return False
                used_char = stack.pop()
                if char == "}" and used_char != "{":
                    return False
                elif char == "]" and used_char != "[":
                    return False
                elif char == ")" and used_char != "(":
                    return False

        if not stack:
            return True
        return False