def validate_password(password):
    if len(password) < 8:
        return "Password must be at least 8 characters long."

    has_upper = False
    has_lower = False
    has_digit = False

    for char in password:
        if char.isupper():
            has_upper = True
        if char.islower():
            has_lower = True
        if char.isdigit():
            has_digit = True

    if has_upper and has_lower and has_digit:
        return "Password is valid."
    else:
        return "Password must contain both uppercase and lowercase letters, and at least one digit."



user_password = input("Enter your password: ")

result = validate_password(user_password)

print(result)
