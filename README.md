## Password Complexity Checker

This repository contains a Python function to assess password strength based on various criteria. 

**Features:**

* Evaluates password length, character types (uppercase, lowercase, digits, special characters)
* Assigns scores based on these criteria
* Provides feedback on overall password strength ("Strong", "Medium", "Weak", or "Very Weak")

**Usage:**

1. Clone this repository.
2. Run the script using Python (e.g., `python password-complexity-checker.py`).
3. The script will prompt you to enter a password.
4. It will then analyze the password and print the corresponding strength feedback.

**Example:**

```
Enter your password: examplePassword123!
Password strength: Strong
```

**Limitations:**

* The current implementation uses a basic penalty system for weak criteria. 
* It doesn't check for repeated characters or common dictionary words, which are easily guessable.

**Future Improvements:**

* Implement a more granular penalty system for weaker password characteristics.
* Integrate logic to detect and penalize repeated characters.
* Consider incorporating a dictionary check to identify weak passwords based on common words.


**How to Contribute**

We welcome contributions to improve this project. Feel free to submit a pull request with your enhancements!
