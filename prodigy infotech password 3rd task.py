import re

def check_password_strength(password):
    # Minimum length
    if len(password) < 8:
        return "Password is too short, it must be at least 8 characters long."
    
    # Check for uppercase and lowercase letters
    if not re.search(r"[A-Z]", password) or not re.search(r"[a-z]", password):
        return "Password must contain both uppercase and lowercase letters."
    
    # Check for numbers
    if not re.search(r"\d", password):
        return "Password must contain at least one number."
    
    # Check for special characters
    if not re.search(r"[!@#$%^&*()-+=]", password):
        return "Password must contain at least one special character: !@#$%^&*()-+=."
    
    return "Password is strong."

# Continuously prompt the user until a strong password is entered
while True:
    password = input("Enter your password: ")
    strength = check_password_strength(password)
    if strength == "Password is strong.":
        print(strength)
        break
    else:
        print(strength)
