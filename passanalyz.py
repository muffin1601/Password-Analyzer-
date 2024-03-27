import re

def analyze_password(password):
    # Define password criteria
    min_length = 8
    min_uppercase = 1
    min_lowercase = 1
    min_digits = 1
    min_special = 1
    common_passwords = ["password", "123456", "qwerty", "abc123"]  # Replace with actual common passwords list
    
    # Check length
    if len(password) < min_length:
        return "Password is too short. Minimum length is {} characters.".format(min_length)
    
    # Check uppercase letters
    if not any(char.isupper() for char in password):
        return "Password must contain at least {} uppercase letter(s).".format(min_uppercase)
    
    # Check lowercase letters
    if not any(char.islower() for char in password):
        return "Password must contain at least {} lowercase letter(s).".format(min_lowercase)
    
    # Check digits
    if not any(char.isdigit() for char in password):
        return "Password must contain at least {} digit(s).".format(min_digits)
    
    # Check special characters
    if not any(char in "!@#$%^&*()_+-=[]{}|;:,.<>?/" for char in password):
        return "Password must contain at least {} special character(s).".format(min_special)
    
    # Check against common passwords list
    if password.lower() in common_passwords:
        return "Password is too common. Choose a more unique password."
    
    # Password meets all criteria
    return "Password is strong."

if __name__ == "__main__":
    # Input password to analyze
    password = input("Enter a password to analyze: ")
    result = analyze_password(password)
    print(result)
