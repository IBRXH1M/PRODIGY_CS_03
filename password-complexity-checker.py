import re

def password_strength(password):
    score = 0
    length = len(password)
    
    # Criteria for password strength
    has_upper = bool(re.search(r'[A-Z]', password))
    has_lower = bool(re.search(r'[a-z]', password))
    has_digit = bool(re.search(r'\d', password))
    has_special = bool(re.search(r'[^A-Za-z0-9]', password))
    
    # Assign scores based on criteria
    score += length * 4
    if has_upper:
        score += 10
    if has_lower:
        score += 10
    if has_digit:
        score += 10
    if has_special:
        score += 20
    
    # Penalty for weak criteria
    if length < 8:
        score -= 20
    if length < 6:
        score -= 20
    if not has_upper:
        score -= 10
    if not has_lower:
        score -= 10
    if not has_digit:
        score -= 10
    if not has_special:
        score -= 20
    
    # Feedback based on score
    if score >= 80:
        return "Strong"
    elif score >= 60:
        return "Medium"
    elif score >= 40:
        return "Weak"
    else:
        return "Very Weak"

# Test the function
password = input("Enter your password: ")
strength = password_strength(password)
print("Password strength:", strength)
