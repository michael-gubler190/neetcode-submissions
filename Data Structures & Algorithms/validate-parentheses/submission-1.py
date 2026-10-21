class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open_brackets = ["(", "[", "{"]
        bracket_mappings = {
            "(": ")",
            "[": "]",
            "{": "}"
        }

        for bracket in s:
            if bracket in open_brackets:
                stack.append(bracket)
            else:
                if len(stack) == 0:
                    return False

                top_bracket = stack.pop()
                if bracket_mappings[top_bracket] != bracket:
                    return False
        
        return len(stack) == 0