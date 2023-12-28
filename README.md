# Secure Password Generator

This Python script provides a simple and secure password generation tool with an interactive command-line interface. The generator allows users to configure password preferences and generate strong passwords based on those preferences.

## Features
- **Quick Configuration:** Set password length and choose whether to include special characters, numbers, and uppercase letters.
- **Generate Password:** Create a secure password based on the configured settings.
- **Copy to Clipboard:** Easily copy the generated password to the clipboard for convenient use.

## How to Use
1. Run the script.
2. Choose from the following options:
    - **Quick Configuration (Option 1):** Set password preferences interactively.
    - **Generate Password (Option 2):** Generate a secure password and copy it to the clipboard.
    - **Exit (Option 3):** End the program.

## Example Usage
```bash
$ python PassGen.py


1. Quick Configuration
2. Generate Password
3. Exit

Select an option: 1
Password length: 16
Include special characters? (y/n): y
Include numbers? (y/n): y
Include uppercase letters? (y/n): n


1. Quick Configuration
2. Generate Password
3. Exit

Select an option: 2
Generated Password: p@ssw0rd1234
Password copied to clipboard: p@ssw0rd1234
```

## Dependencies
- Python 3.x
- Tkinter (included in most Python installations)

## Notes
- This script uses the `secrets` module for secure random number generation.
- The Tkinter library is employed to copy the generated password to the clipboard.

Feel free to use, modify, and contribute to this password generator script for your secure password needs. If you encounter any issues or have suggestions, please create an issue or submit a pull request.

**Disclaimer:** Ensure the security of generated passwords by keeping the script and generated passwords in a secure environment. Do not share generated passwords in insecure ways.

**Author:** @ConteZoller

**License:** None

