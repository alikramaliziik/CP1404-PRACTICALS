"""Manage scores with a menu-driven interface."""

def main():
    """Run the score menu program."""
    score = get_valid_score()
    while True:
        print("\nMenu:")
        print("(G)et a valid score")
        print("(P)rint result")
        print("(S)how stars")
        print("(Q)uit")
        choice = input("Choose an option: ").upper()
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            result = get_score_result(score)
            print(f"Your score of {score} is {result}")
        elif choice == "S":
            show_stars(score)
        elif choice == "Q":
            print("Farewell!")
            break
        else:
            print("Invalid choice.")

def get_valid_score():
    """Get a score between 0 and 100."""
    score = float(input("Enter a score (0-100): "))
    while not 0 <= score <= 100:
        print("Score must be between 0 and 100.")
        score = float(input("Enter a score (0-100): "))
    return score

def get_score_result(score):
    """Return the result for a score between 0 and 100."""
    if not 0 <= score <= 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

def show_stars(score):
    """Print stars equal to the score value."""
    print("*" * int(score))

main()
