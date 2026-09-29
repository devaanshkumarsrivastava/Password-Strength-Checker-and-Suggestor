storage.py

import json
from datetime import datetime

def save_history(password, score):
    """
    so we will save masked password history to JSON file.
    """
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
    """
    here we'll Display last 5 history entries.
    """
    try:
        with open("history.json", "r") as f:
            data = json.load(f)
        for item in data[-5:]:
            print(item)
    except FileNotFoundError:
        print("No history yet.")
