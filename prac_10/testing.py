import doctest
from car import Car


def repeat_string(s, n):
    """Repeat string s, n times, with spaces in between."""
    return " ".join([s] * n)


def is_long_word(word, length=5):
    """
    Determine if the word is as long or longer than the length passed in
    >>> is_long_word("not")
    False
    >>> is_long_word("supercalifrag")
    True
    >>> is_long_word("Python", 6)
    False
    """
    return len(word) > length


def format_sentence(phrase):
    """
    Format a phrase as a sentence, starting with a capital and ending with a single full stop.
    >>> format_sentence("hello")
    'Hello.'
    >>> format_sentence("It is an ex parrot.")
    'It is an ex parrot.'
    >>> format_sentence("no full stop here")
    'No full stop here.'
    """
    cleaned_phrase = phrase.rstrip(".")
    return cleaned_phrase[0].upper() + cleaned_phrase[1:] + "."


def run_tests():
    """Run the tests on the functions."""
    assert repeat_string("Python", 1) == "Python"
    assert repeat_string("hi", 2) == "hi hi"

    car = Car()
    assert car._odometer == 0, "Car does not set odometer correctly"

    # Test fuel initialization
    car = Car(fuel=10)
    assert car.fuel == 10, "Car does not set fuel correctly when specified"
    car = Car()
    assert car.fuel == 100, "Car does not set default fuel correctly"


run_tests()

doctest.testmod()
