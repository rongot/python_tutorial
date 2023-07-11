def valid_parentheses(parens:str):
    count = 0
    i = 0
    while i < len(parens):
        if (parens[i] == '('):
            count += 1
        if (parens[i] == ')'):
            count -= 1
        if (count < 0):
            return False
        i += 1
    return count == 0

print(valid_parentheses("()")) # True 
print(valid_parentheses(")(()))")) # False 