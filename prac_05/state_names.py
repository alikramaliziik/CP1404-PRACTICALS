"""
CP1404/CP5632 Practical
State names in a dictionary
reformatted to follow PEP 8 conventions
"""

# Dictionary of Australian state abbreviations and names (PEP 8 formatted)
CODE_TO_NAME = {
    "ACT": "Australian Capital Territory",
    "NSW": "New South Wales",
    "NT": "Northern Territory",
    "QLD": "Queensland",
    "SA": "South Australia",
    "TAS": "Tasmania",
    "VIC": "Victoria",
    "WA": "Western Australia"
}

def main():
    """Get state abbreviation from user and print its full name, then display all states."""
    # Get user input and handle case-insensitivity
    state_code = input("Enter short state: ").upper()
    while state_code != "":
        try:
            print(f"{state_code} is {CODE_TO_NAME[state_code]}")
        except KeyError:
            print("Invalid short state")
        state_code = input("Enter short state: ").upper()

    # Print all states neatly formatted
    print("\nAustralian States:")
    max_abbrev_len = max(len(abbrev) for abbrev in CODE_TO_NAME)
    for abbrev, name in CODE_TO_NAME.items():
        print(f"{abbrev:<{max_abbrev_len}} is {name}")

if __name__ == "__main__":
    main()

