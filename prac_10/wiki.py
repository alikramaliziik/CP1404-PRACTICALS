import wikipedia
from wikipedia.exceptions import DisambiguationError, PageError


def main():
    """Prompt user for Wikipedia page titles and display page details until blank input."""
    while True:
        title = input("Enter page title: ").strip()
        if not title:  # Exit on blank input
            print("Thank you.")
            break

        try:
            # Get page with auto_suggest disabled to avoid automatic suggestions
            page = wikipedia.page(title, auto_suggest=False)
            # Print title, summary, and URL
            print(page.title)
            print(page.summary)
            print(page.url)
            print()  # Blank line for readability

        except PageError:
            print(f'Page id "{title}" does not match any pages. Try another id!')
            print()

        except DisambiguationError as e:
            print("We need a more specific title. Try one of the following, or a new search:")
            print(e.options)
            print()


if __name__ == "__main__":
    main()
