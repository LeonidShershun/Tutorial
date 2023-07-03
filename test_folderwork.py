def capital_text(s):
    result =''
    capitalize = True
    for i in range(len(s)):
        char = s[i]
        if i == 0 or s[i-1] in ['.', '!', '?',] or s[i-1].isspace():
            char = char.upper()
        # elif char == char.upper():
        #     continue
        else:
            char = char.lower()
        result += char
    return result







a = '   молоко пити можна!    і порібно.  але як часто? скільки хочеш.'

print(capital_text(a))
