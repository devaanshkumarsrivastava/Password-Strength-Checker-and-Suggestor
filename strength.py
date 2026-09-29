strength.py

import string

def analyze(password):
    """
    Analyze password strength using entropy-style scoring.
    Returns a dictionary with score, issues, and crack time estimate.
    """
    if not password:
        return {"score": 0, "issues": ["Password cannot be empty"], "crack_time": 0}

    pool = 0
    if any(ch.islower() for ch in password):
        pool += 26
    if any(ch.isupper() for ch in password):
        pool += 26
    if any(ch.isdigit() for ch in password):
        pool += 10
    if any(ch in string.punctuation for ch in password):
        pool += len(string.punctuation)

    pool = max(pool, 1)
    combinations = pool ** len(password)
    guesses_per_second = 1e9
    crack_seconds = combinations / guesses_per_second

    # here i calculated Score thresholds
    if crack_seconds < 1e3:
        score = 1
    elif crack_seconds < 1e6:
        score = 4
    elif crack_seconds < 1e9:
        score = 7
    else:
        score = 10

    issues = []
    if len(password) < 8:
        issues.append("shorter than 8 characters")
    if not any(ch.isupper() for ch in password):
        issues.append("no uppercase letters")
    if not any(ch.isdigit() for ch in password):
        issues.append("no numbers")
    if not any(ch in string.punctuation for ch in password):
        issues.append("no symbols")

    return {"score": score, "issues": issues, "crack_time": crack_seconds}
