def valid_parentheses(s, stack = 0, i=0):
    if i == len(s):
        return stack == 0
    if s[i] == '(':
        stack += 1
    if s[i] == ')':
        stack -= 1
    if stack < 0:
        return False
    return valid_parentheses(s, stack, i+1) 
