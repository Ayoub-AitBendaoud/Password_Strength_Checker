import re
import time

def strong_pass_checker(password):
    if len(password) < 8:
        return "Weak password: Password must be at least 8 characters long."
    # Check for lowercase letters
    if not re.search("[a-z]", password):
        return "Weak password: Password must contain at least one lowercase letter."
    # Check for uppercase letters
    if not re.search("[A-Z]", password):
        return "Weak password: Password must contain at least one uppercase letter."
    # Check for digits
    if not re.search("[0-9]", password):
        return "Medium password: Password must contain at least one digit."    
    # Check for special characters
    if not re.search("[!@#$%^&*(),.?\":{}|<>]", password):
        return "Medium password: Password must contain at least one special character."
    # If all checks are passed
    return "Your password is strong."

# Main function to prompt user for password and check its strength
def main():
    password = input("Enter your password: ")
    for _ in range(6):
        print(".", end="")
        time.sleep(1)
    print(" progress is Done")
    result = strong_pass_checker(password)
    print(result)

if __name__ == "__main__":
    main()

# password-strength-checker V1.2.0 by Ayoub Aitbendaoud
# LinkedIn: @ayoub_aitbendaoud
# YouTube and GitHub: @Ayoub_aitbendaoud
