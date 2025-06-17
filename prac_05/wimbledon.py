"""
Wimbledon Champions Processing
Estimate: 40 minutes
Actual:   1 hour
"""

def read_wimbledon_data(filename):
    """Read CSV file and return list of lists with champion and country data."""
    data = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        next(in_file)  # Skip header
        for line in in_file:
            parts = line.strip().split(',')
            champion = parts[2]  # Champion name
            country = parts[1]  # Champion country
            data.append([champion, country])
    return data

def count_champions(data):
    """Count wins for each champion using a dictionary."""
    champion_counts = {}
    for champion, _ in data:
        champion_counts[champion] = champion_counts.get(champion, 0) + 1
    return champion_counts

def get_unique_countries(data):
    """Get unique countries in alphabetical order using a set."""
    countries = set(country for _, country in data)
    return sorted(countries)

def display_results(champion_counts, countries):
    """Display champions with win counts and sorted countries."""
    print("Wimbledon Champions:")
    max_name_len = max(len(name) for name in champion_counts)
    for champion in sorted(champion_counts.keys()):
        print(f"{champion:<{max_name_len}} {champion_counts[champion]}")
    
    print(f"\nThese {len(countries)} countries have won Wimbledon:")
    print(', '.join(countries))

def main():
    """Process Wimbledon data and display champions and countries."""
    filename = "wimbledon.csv"
    data = read_wimbledon_data(filename)
    champion_counts = count_champions(data)
    countries = get_unique_countries(data)
    display_results(champion_counts, countries)

if __name__ == "__main__":
    main()
