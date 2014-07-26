"""Little Parser Problem Challenge: Matching Pairs Validation

Check if an input string has mismatched curly braces.

For example,
s = "{}" is valid.
s = "{}}" is invalid.
"""

def check_curlies_stack(s):
    "Check if all curly braces are paired."
    stack = []
    for l in s:
        if l == "{":
            stack.append("{")
        elif l == "}":
            try:
                stack.pop()
            except IndexError:
                return False
    return len(stack) == 0 # If stack is empty, curlies check passes.

def check_curlies_counter(s):
    "Check if all curly braces are paired."
    counter = 0
    for l in s:
        if l == "{":
            counter += 1
        elif l == "}":
            counter -= 1
    return counter == 0