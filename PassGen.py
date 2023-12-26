import secrets
import string
import tkinter as tk

class SecurePasswordGenerator:
    def __init__(self):
        # Initialize default values for password configuration
        self.password_length = 12
        self.include_special_chars = True
        self.include_numbers = True
        self.include_uppercase = True

    def generate_password(self):
        # Generate a secure password using the configured settings
        chars = self.get_character_set()
        generated_password = ''.join(secrets.choice(chars) for _ in range(self.password_length))
        return generated_password

    def get_character_set(self):
        # Define the character set based on configuration
        chars = string.ascii_letters if self.include_uppercase else string.ascii_lowercase
        chars += string.digits if self.include_numbers else ''
        chars += string.punctuation if self.include_special_chars else ''
        return chars

    def copy_to_clipboard(self, text):
        # Copy the generated password to the clipboard using Tkinter
        root = tk.Tk()
        root.withdraw()

        root.clipboard_clear()
        root.clipboard_append(text)
        root.update()

        print("Password copied to clipboard: {}".format(text))
        root.destroy()  # Close the Tkinter window

    def configure_password_preferences(self):
        # Configure password preferences interactively
        print("\nQuick Password Configuration:")
        try:
            self.password_length = int(input("Password length: "))
        except ValueError:
            print("Please enter a valid number.")

        self.include_special_chars = input("Include special characters? (y/n): ").lower() == 'y'
        self.include_numbers = input("Include numbers? (y/n): ").lower() == 'y'
        self.include_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'

    def main(self):
        # Main loop for user interaction
        while True:
            print("\nSecure Password Generator")
            print("1. Quick Configuration")
            print("2. Generate Password")
            print("3. Exit")

            choice = input("Select an option: ")

            if choice == '1':
                self.configure_password_preferences()
            elif choice == '2':
                generated_password = self.generate_password()
                print("Generated Password: {}".format(generated_password))
                self.copy_to_clipboard(generated_password)
            elif choice == '3':
                break
            else:
                print("Invalid option. Please try again.")

if __name__ == "__main__":
    # Instantiate the password generator and start the main loop
    password_generator = SecurePasswordGenerator()
    password_generator.main()

