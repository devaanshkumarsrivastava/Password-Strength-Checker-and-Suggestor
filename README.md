Password Strength Checker & Generator
Overview:

A command-line Python project that:

Checks password strength using entropy-based scoring.
Explains weaknesses and suggests stronger alternatives.
Generates random secure passwords.
Stores masked history of past checks.

Features:

Strength Analyzer (strength.py): Calculates character pool size, brute-force combinations, estimated crack time, score, and issues.
Stronger Password Suggester (suggest.py): Builds a stronger, similar-looking password and re-checks until it scores higher.
Random Password Generator (generator.py): Creates brand-new random passwords with chosen character types.
History Storage (storage.py): Saves masked password history in JSON.
CLI Entry Point (main.py): Provides commands (check, suggest, generate, history) for user interaction.

Installation & Running:

Clone the repo:
git clone https://github.com/yourusername/password-checker.git
cd password-checker

Run commands:

python main.py check
python main.py suggest
python main.py generate
python main.py history

 Features:
- Password scoring system (1–10 scale).
- Checks for length, uppercase letters, digits, and special characters.
- Suggests stronger passwords if score ≤ 5.
- Beginner‑friendly Python implementation with modular functions.

 Technologies:
 
Python standard library:

- argparse (CLI parsing)
- secrets (secure random generation)
- json (history storage)
- datetime (timestamps)
- unittest (testing)

3. Run the program:
python password_checker.py

Testing
Run unit tests:

python -m unittest discover -s tests
