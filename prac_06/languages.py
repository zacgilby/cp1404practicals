"""
CP1404/CP5632 Practical
Tests the ProgrammingLanguage class created in programming_language.py
"""
from prac_06.programming_language import ProgrammingLanguage

ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

languages = [ruby, python, visual_basic]
print(python)

print("The dynamically typed languages are:")
for language in languages:
    if language.is_dynamic():
        print(language.field)
