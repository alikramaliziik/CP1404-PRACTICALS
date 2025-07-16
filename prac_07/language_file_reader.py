"""
CP1404/CP5632 Practical
File reader that loads programming language details from a CSV file into ProgrammingLanguage objects.
Includes alternative versions using csv module and namedtuple for demonstration.
"""

import csv
from collections import namedtuple
from programming_language import ProgrammingLanguage

def main():
    """Read file of programming language details, save as ProgrammingLanguage objects, and display."""
    languages = []
    try:
        # Open the file for reading
        with open('languages.csv', 'r', encoding='utf-8', newline='') as in_file:
            # File format: Language,Typing,Reflection,Year,Pointer Arithmetic
            in_file.readline()  # Skip header
            # Process all other lines as language data
            for line in in_file:
                # Strip newline and split into parts (CSV)
                parts = line.strip().split(',')
                if len(parts) < 5:  # Ensure all fields are present
                    print(f"Warning: Skipping invalid row: {parts}")
                    continue
                # Convert Reflection and Pointer Arithmetic to Boolean
                reflection = parts[2] == "Yes"
                pointer_arithmetic = parts[4] == "Yes"
                try:
                    # Construct a ProgrammingLanguage object
                    language = ProgrammingLanguage(parts[0], parts[1], reflection, int(parts[3]), pointer_arithmetic)
                    languages.append(language)
                except ValueError as e:
                    print(f"Error processing row {parts}: {e}")
    except FileNotFoundError:
        print("Error: File 'languages.csv' not found.")
        return
    except Exception as e:
        print(f"Error reading file: {e}")
        return

    # Display all languages using their str method
    for language in languages:
        print(language)

def using_csv():
    """Read and display language data using the csv module (for demonstration)."""
    try:
        with open('languages.csv', 'r', encoding='utf-8', newline='') as in_file:
            in_file.readline()  # Skip header
            reader = csv.reader(in_file)
            for row in reader:
                print(row)
    except FileNotFoundError:
        print("Error: File 'languages.csv' not found.")
    except Exception as e:
        print(f"Error reading file: {e}")

def using_namedtuple():
    """Read and display language data using a named tuple (for demonstration)."""
    try:
        with open('languages.csv', 'r', encoding='utf-8', newline='') as in_file:
            file_field_names = in_file.readline().strip().split(',')
            Language = namedtuple('Language', 'name, typing, reflection, year, pointer_arithmetic')
            reader = csv.reader(in_file)
            for row in reader:
                language = Language._make(row)
                print(f"Language(name='{language.name}', typing='{language.typing}', "
                      f"reflection='{language.reflection}', year='{language.year}', "
                      f"pointer_arithmetic='{language.pointer_arithmetic}')")
    except FileNotFoundError:
        print("Error: File 'languages.csv' not found.")
    except Exception as e:
        print(f"Error reading file: {e}")

def using_csv_namedtuple():
    """Read and display language data using csv and named tuple (for demonstration)."""
    try:
        Language = namedtuple('Language', 'name, typing, reflection, year, pointer_arithmetic')
        with open('languages.csv', 'r', encoding='utf-8', newline='') as in_file:
            in_file.readline()  # Skip header
            for language in map(Language._make, csv.reader(in_file)):
                print(f"{language.name} was released in {language.year}")
                print(f"Language(name='{language.name}', typing='{language.typing}', "
                      f"reflection='{language.reflection}', year='{language.year}', "
                      f"pointer_arithmetic='{language.pointer_arithmetic}')")
    except FileNotFoundError:
        print("Error: File 'languages.csv' not found.")
    except Exception as e:
        print(f"Error reading file: {e}")

if __name__ == "__main__":
    main()
    
