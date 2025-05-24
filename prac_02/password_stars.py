"""Check password length and print a asterisk sequence for its length."""

MINIMUM_LENGTH = 8

def main():
    """Run the password check program."""
    password = get_password()
    print_asterisks(password)

def get_password():
    """Get a password that is at least 8 characters long and non-empty."""
    while True:
        password = input("Enter your password: ")
        if not password:
            print("Password cannot be empty.")
            continue
        if len(password) < MINIMUM_LENGTH:
            print(f"Password must be at least {MINIMUM_LENGTH} characters long.")
            continue
        return password

def print_asterisks(password, symbol="*"):
    """Print a sequence of symbols equal to the password length."""
    print(symbol * len(password))

main()
