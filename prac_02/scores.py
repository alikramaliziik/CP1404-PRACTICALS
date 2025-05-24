"""Determine the result of a score between 0 and 100."""

def main():
    """Run the score evaluation program."""
    score = float(input("Enter your score (0-100): "))
    result = get_score_result(score)
    print(f"Your score of {score} is {result}")

    import random
    random_score = random.randint(0, 100)
    random_result = get_score_result(random_score)
    print(f"Random score of {random_score} is {random_result}")

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

main()
