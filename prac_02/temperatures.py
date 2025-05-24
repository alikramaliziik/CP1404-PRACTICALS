"""Convert temperatures between Celsius and Fahrenheit."""

def main():
    """Run the temperature conversion program."""
    choice = input("Convert (C)elsius to Fahrenheit or (F)ahrenheit to Celsius? ").upper()
    if choice == "C":
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = convert_celsius_to_fahrenheit(celsius)
        print(f"{celsius}°C is {fahrenheit:.2f}°F")
    elif choice == "F":
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = convert_fahrenheit_to_celsius(fahrenheit)
        print(f"{fahrenheit}°F is {celsius:.2f}°C")
    else:
        print("Invalid choice.")

def convert_celsius_to_fahrenheit(celsius):
    """Convert a Celsius temperature to Fahrenheit."""
    return celsius * 9 / 5 + 32

def convert_fahrenheit_to_celsius(fahrenheit):
    """Convert a Fahrenheit temperature to Celsius."""
    return (fahrenheit - 32) * 5 / 9

main()
