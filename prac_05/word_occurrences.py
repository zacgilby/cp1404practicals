"""
P1404/CP5632 - Practical
This program will count the occurrences of the words present in a string.
"""


unique_words = {}
text = input("Enter some text: ")
words = text.split()
for word in words:
    frequency = unique_words.get(word, 0)
    unique_words[word] = frequency + 1

words = list(unique_words.keys())
words.sort()

max_length = max((len(word)  for word in words))
for word in words:
    print("{:{}} : {}".format(word, max_length, unique_words[word]))
