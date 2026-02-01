def is_valid_parentheses(s: str) -> bool:
    """
    Return True if the string contains valid, balanced parentheses.
    Only (), {}, and [] are considered valid.

    Uses a stack (LIFO) to ensure each closing bracket
    matches the most recent opening bracket.
    """
    stack = []

    # Mapping of closing to opening brackets
    pairs = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    for char in s:
        # Push opening brackets onto the stack
        if char in pairs.values():
            stack.append(char)

        # For closing brackets, check for a match
        elif char in pairs:
            if not stack or stack.pop() != pairs[char]:
                return False

    # If stack is empty, all brackets were balanced
    return len(stack) == 0


# -----------------------------
# Demonstration / Output
# -----------------------------
if __name__ == "__main__":
    print("STACK DEMONSTRATION: Parentheses Validation\n")

    test_cases = [
        "()",
        "{[()]}",
        "([]{})",
        "(",
        "([)]",
        "(()"
    ]

    for case in test_cases:
        result = is_valid_parentheses(case)
        print(f"Input: {case} -> Valid: {result}")
