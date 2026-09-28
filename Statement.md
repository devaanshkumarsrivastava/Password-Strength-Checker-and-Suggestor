Statement.md

# Project Statement

# Problem:

Most password strength meters only show a colored bar without explaining why a password is weak or how to improve it. Users are left guessing whether adding a number or making the password longer helps more.  
This project solves that by analyzing passwords with entropy-based scoring, listing specific weaknesses, suggesting stronger alternatives, generating random secure passwords, and keeping a masked local history of past checks.

# Scope of the Project
- Input: User interacts via a command-line interface (`main.py`) with options to check, suggest, generate, or view history.  
- Processing: Passwords are analyzed for character pool size, brute-force combinations, estimated crack time, and scored on a 1–10 scale.  
- Output: Displays score, issues, suggestions, generated passwords, and history entries.  
- Target Users: Students learning Python, general users creating secure passwords, and educators demonstrating security concepts.

# Target Users
- Beginners in programming who want a practical project.  
- Everyday users creating passwords for email or online accounts.  
- Teachers who want a simple demo project to explain password security.  

# High-Level Features
- Strength Analyzer (`strength.py`): Calculates entropy, crack time, score, and issues.  
- Stronger Password Suggester (`suggest.py`): Builds a stronger, similar-looking password and re-checks until it scores higher.  
- Random Password Generator (`generator.py`): Creates brand-new random passwords with chosen character types.  
- History Storage (`storage.py`): Saves masked password history in JSON format.  
- CLI Entry (`main.py`): Provides commands (`check`, `suggest`, `generate`, `history`) for user interaction.  

# Workflow
1. User runs `main.py` and chooses a command.  
2. For check: password is analyzed, score and issues are displayed, and entry saved to history.  
3. For suggest: a stronger password is generated and verified to score higher.  
4. For generate: a new random password is created with chosen options.  
5. For history: recent masked entries are displayed.  

# Design Decisions
- Entropy-based scoring: More realistic than simple rule-counting.  
- Masked history storage: Keeps history useful without storing full passwords.  
- Re-check loop for suggestions: Ensures suggested password is verifiably stronger.  
- Use of `secrets` module: Provides cryptographically secure random generation.  
- Modular design: Each function in its own file for clarity and maintainability.  

# Future Enhancements
- Check against breached-password datasets.  
- Detect keyboard patterns (e.g., "qwerty", "1234").  
- Add a visual strength bar in terminal output.  
- Configurable attacker guessing speed for crack-time estimates.  

- Add GUI interface for better usability.  
- Integrate with password managers or email signup forms. 
