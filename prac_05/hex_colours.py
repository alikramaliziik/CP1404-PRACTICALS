"""
CP1404/CP5632 Practical
Hexadecimal color code lookup program
"""

# Constant dictionary of color names and hex codes (PEP 8 formatted)
COLOR_TO_HEX = {
    "ALICEBLUE": "#f0f8ff",
    "ANTIQUEWHITE": "#faebd7",
    "AQUA": "#00ffff",
    "BEIGE": "#f5f5dc",
    "BLACK": "#000000",
    "CORAL": "#ff7f50",
    "DARKGREEN": "#006400",
    "GOLD": "#ffd700",
    "LAVENDER": "#e6e6fa",
    "RED": "#ff0000"
}

def main():
    """Get color name from user and print its hex code until blank input."""
    color_name = input("Enter color name: ").upper()
    while color_name != "":
        try:
            hex_code = COLOR_TO_HEX[color_name]
            print(f"{color_name} is {hex_code}")
        except KeyError:
            print("Invalid color name")
        color_name = input("Enter color name: ").upper()

    # Print all colors neatly formatted
    print("\nAvailable Colors:")
    max_name_len = max(len(name) for name in COLOR_TO_HEX)
    for name, hex_code in COLOR_TO_HEX.items():
        print(f"{name:<{max_name_len}} is {hex_code}")

if __name__ == "__main__":
    main()
# Updated for prac_05_feedback code review
