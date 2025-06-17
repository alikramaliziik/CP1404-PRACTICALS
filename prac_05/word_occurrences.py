"""
Word Occurrences
Estimate: 30 minutes
Actual:   45 minues
"""

def main():
    """Count word occurrences in a user-input string and print sorted, aligned results."""
    # Get user input
    text = input("Text: ")
    if not text.strip():
        print("No text provided")
        return

    # Split text into words and count occurrences
    word_counts = {}
    for word in text.split():
        word = word.lower()  # Case-insensitive counting
        try:
            word_counts[word] += 1
        except KeyError:
            word_counts[word] = 1

    # Find the longest word for alignment
    max_word_len = max(len(word) for word in word_counts)

    # Print sorted results with aligned counts
    for word in sorted(word_counts.keys()):
        print(f"{word:<{max_word_len}} : {word_counts[word]}")

if __name__ == "__main__":
    main()
