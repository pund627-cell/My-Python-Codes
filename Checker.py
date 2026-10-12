# Simple Password Strength Checker - Created by Shubham
# A beginner-friendly Python project to check password strength

def check_password_strength(password):
    score = 0
    feedback = []

    # Check length
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters")

    # Check for uppercase
    if any(c.isupper() for c in password):
        score += 1
    else:
        feedback.append("Add at least one Uppercase letter")

    # Check for lowercase
    if any(c.islower() for c in password):
        score += 1
    else:
        feedback.append("Add at least one Lowercase letter")

    # Check for numbers
    if any(c.isdigit() for c in password):
        score += 1
    else:
        feedback.append("Add at least one Number")

    # Check for special character
    if any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?/" for c in password):
        score += 1
    else:
        feedback.append("Add at least one Special character (!@#$%)")

    # Result
    print("\n--- Password Analysis ---")
    if score == 5:
        print("✅ Strong Password!")
    elif score >= 3:
        print("⚠️ Medium Password - Can be improved")
    else:
        print("❌ Weak Password!")

    print(f"Score: {score}/5")
    
    if feedback:
        print("\nSuggestions:")
        for tip in feedback:
            print(f" - {tip}")

# Main Program
print("=== Password Strength Checker ===")
user_password = input("Enter your password to check: ")
check_password_strength(user_password)