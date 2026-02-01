def is_valid_parentheses(s: str) -> bool:
    """
    Return True if the string contains valid, balanced parentheses.
    Only (), {}, and [] are considered valid.
    """
    stack = []
    pairs = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    for char in s:
        # If opening bracket, push to stack
        if char in pairs.values():
            stack.append(char)

        # If closing bracket, check match
        elif char in pairs:
            if not stack or stack.pop() != pairs[char]:
                return False

    # Valid only if no unmatched brackets remain
    return len(stack) == 0
