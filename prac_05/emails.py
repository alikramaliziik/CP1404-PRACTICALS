"""
Emails and Names
Estimate: 20 minutes
Actual:   35 minutes
"""

def extract_name_from_email(email):
    """Extract a name from an email address by processing the local part."""
    # Get the part before '@' and split by dots or underscores
    local_part = email.split('@')[0]
    name_parts = local_part.replace('.', ' ').replace('_', ' ').split()
    # Join parts and capitalize each word
    return ' '.join(part.title() for part in name_parts)

def main():
    """Store email-to-name mappings and print them after collecting all inputs."""
    EMAIL_TO_NAME = {}
    
    while True:
        email = input("Email: ").strip()
        if email == "":
            break
            
        # Extract name and confirm with user
        suggested_name = extract_name_from_email(email)
        confirmation = input(f"Is your name {suggested_name}? (Y/n) ").strip().lower()
        
        # If user presses Enter or enters 'y', use suggested name; otherwise, ask for name
        if confirmation in ('', 'y'):
            name = suggested_name
        else:
            name = input("Name: ").strip()
            
        EMAIL_TO_NAME[email] = name
    
    # Print all email-name pairs
    if EMAIL_TO_NAME:
        print()
        for email, name in EMAIL_TO_NAME.items():
            print(f"{name} ({email})")
    else:
        print("No emails provided")

if __name__ == "__main__":
    main()
