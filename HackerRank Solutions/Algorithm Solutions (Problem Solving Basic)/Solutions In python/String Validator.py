if __name__ == '__main__':
    s = input()

    print(any(c.isalnum() for c in s))   # Alphanumeric
    print(any(c.isalpha() for c in s))   # Alphabetical
    print(any(c.isdigit() for c in s))   # Digits
    print(any(c.islower() for c in s))   # Lowercase
    print(any(c.isupper() for c in s))   # Uppercase

or 

if __name__ == '__main__':
    s = input()

    has_alnum = False
    has_alpha = False
    has_digit = False
    has_lower = False
    has_upper = False

    for char in s:
        if char.isalnum():
            has_alnum = True
        if char.isalpha():
            has_alpha = True
        if char.isdigit():
            has_digit = True
        if char.islower():
            has_lower = True
        if char.isupper():
            has_upper = True

    print(has_alnum)
    print(has_alpha)
    print(has_digit)
    print(has_lower)
    print(has_upper)


