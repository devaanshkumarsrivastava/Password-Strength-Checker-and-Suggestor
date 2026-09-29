suggest.py

import secrets
import string
from strength import analyze

def suggest(password):
    #Suggest a stronger password by adding missing character types and extending length until it scores higher.
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
        return suggest(new_pass)  # re-check until stronger
    return new_pass
