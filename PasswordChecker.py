import re

class PasswordComplexityChecker:
    def __init__(self, password):
        self.password = password
        self.strength = self.check_complexity()

    def check_complexity(self):
        score = 0

        # Check for length
        if len(self.password) >= 8:
            score += 1

        # Check for uppercase
        if re.search(r"[A-Z]", self.password):
            score += 1

        # Check for lowercase
        if re.search(r"[a-z]", self.password):
            score += 1

        # Check for numbers
        if re.search(r"[0-9]", self.password):
            score += 1

        # Check for special characters
        if re.search(r"[^A-Za-z0-9]", self.password):
            score += 1

        return score

    def get_feedback(self):
        if self.strength == 0:
            return "Very Weak: Password is too short and lacks complexity."
        elif self.strength == 1:
            return "Weak: Password is too short and lacks variety."
        elif self.strength == 2:
            return "Fair: Password is of medium length but needs more complexity."
        elif self.strength == 3:
            return "Good: Password has decent length and complexity."
        elif self.strength == 4:
            return "Strong: Password is long and has high complexity."

# Example usage:
password = input("Enter a password: ")
checker = PasswordComplexityChecker(password)
print("Password strength:", checker.strength)
print(checker.get_feedback())
