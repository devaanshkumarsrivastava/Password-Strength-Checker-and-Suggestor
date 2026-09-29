import secrets
import string
import json
from datetime import datetime

def analyze(password):
    if not password:
        return {"score": 0, "issues": ["Password cannot be empty"]} #like code tells that password holder cant be empty

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

def suggest(password):
    suggestion = list(password)
    if not any(ch.isupper() for ch in suggestion):
        suggestion.append(secrets.choice(string.ascii_uppercase))
    if not any(ch.isdigit() for ch in suggestion):
        suggestion.append(secrets.choice(string.digits))
    if not any(ch in string.punctuation for ch in suggestion):
        suggestion.append(secrets.choice(string.punctuation))
    while len(suggestion) < 12:
        suggestion.append(secrets.choice(string.ascii_letters + string.digits))

    new_pass = "".join(suggestion)
    if analyze(new_pass)["score"] <= analyze(password)["score"]:
        return suggest(new_pass)
    return new_pass

def generate(length=12, use_upper=True, use_digits=True, use_symbols=True):
    pool = string.ascii_lowercase
    if use_upper:
        pool += string.ascii_uppercase
    if use_digits:
        pool += string.digits
    if use_symbols:
        pool += string.punctuation

    if length < 4:
        raise ValueError("Length too short for secure password")

    return "".join(secrets.choice(pool) for _ in range(length))

def save_history(password, score):
    masked = password[0] + "***" + password[-1] if len(password) > 2 else "***"
    entry = {
        "timestamp": datetime.now().isoformat(),
        "password": masked,
        "length": len(password),
        "score": score
    }
    try:
        with open("history.json", "r") as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        data = []
    data.append(entry)
    with open("history.json", "w") as f:
        json.dump(data, f, indent=2)

def view_history():
    try:
        with open("history.json", "r") as f:
            data = json.load(f)
        for item in data[-5:]:
            print(item)
    except FileNotFoundError:
        print("No history yet.")
#i put CLI in simplified manner below
def main():
    print("=== Password Strength Checker ===")
    choice = input("Choose: check / suggest / generate / history: ").strip().lower()

    if choice == "check":
        pwd = input("Enter password: ")
        result = analyze(pwd)
        print("Score:", result["score"], "/10")
        print("Issues:", result["issues"])
        save_history(pwd, result["score"])
    elif choice == "suggest":
        pwd = input("Enter weak password: ")
        print("Suggested:", suggest(pwd))
    elif choice == "generate":
        print("Generated:", generate())
    elif choice == "history":
        view_history()
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
