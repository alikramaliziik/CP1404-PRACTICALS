"""
CP1404/CP5632 Practical - Client code to use ProgrammingLanguage class
Estimated time: 8 minutes
Actual time: 11 minutes
"""

from programming_language import ProgrammingLanguage


def main():
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    
    print(python)
    print(ruby)
    print(visual_basic)

    languages = [python, ruby, visual_basic]
    
    print("\nThe dynamically typed languages are:")
    for language in languages:
        if language.is_dynamic():
            print(language.name)


main()
