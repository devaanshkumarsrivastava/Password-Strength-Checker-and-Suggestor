
import secrets
import string

def generate(length=12, use_upper=True, use_digits=True, use_symbols=True):
    """
    Generate a random password with chosen character types.
    """
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
