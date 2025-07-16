import csv
from guitar import Guitar


def load_guitars(filename):
    """Load guitars from a CSV file into a list of Guitar objects."""
    guitars = []
    with open(filename, 'r', newline='') as in_file:
        reader = csv.reader(in_file)
        for row in reader:
            name, year, cost = row
            guitars.append(Guitar(name, int(year), float(cost)))
    return guitars


def save_guitars(filename, guitars):
    """Save guitars to a CSV file."""
    with open(filename, 'w', newline='') as out_file:
        writer = csv.writer(out_file)
        for guitar in guitars:
            writer.writerow([guitar.name, guitar.year, guitar.cost])


def get_new_guitar():
    """Get new guitar details from user input."""
    name = input("Name: ")
    if not name:
        return None
    year = int(input("Year: "))
    cost = float(input("Cost: "))
    guitar = Guitar(name, year, cost)
    print(f"{guitar} added.\n")
    return guitar


def display_guitars(guitars):
    """Display all guitars, sorted by year."""
    guitars.sort()  # Sort by year using __lt__
    print("\nThese are my guitars:")
    for i, guitar in enumerate(guitars, 1):
        vintage_string = " (vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")


def main():
    """Main program to manage guitar collection."""
    filename = "guitars.csv"
    guitars = load_guitars(filename)
    display_guitars(guitars)

    # Add new guitars
    print("\nEnter new guitars (blank name to finish):")
    adding_guitars = True
    while adding_guitars:
        guitar = get_new_guitar()
        if guitar is None:
            adding_guitars = False
        else:
            guitars.append(guitar)

    # Display sorted guitars
    display_guitars(guitars)

    # Save to file
    save_guitars(filename, guitars)
    print(f"\nGuitars saved to {filename}")


if __name__ == "__main__":
    main()
