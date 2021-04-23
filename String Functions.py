"""
Python contains many useful built-in functions and methods to accomplish common tasks.
join - joins a list of strings with another string as a separator.
replace - replaces one substring in a string with another.
startswith and endswith - determine if there is a substring at the start and end of a string, respectively.
To change the case of a string, you can use lower and upper.
The method split is the opposite of join turning a string with a certain separator into a list.
"""

print(",".join(["spam", "eggs", "ham"]))

print("Hello Me".replace("Me","World"))

print("This is a sentence".startswith("This"))

print("This is a sentence".startswith("is"))

print("This is a sentence".endswith("sentence"))

print("This is a sentence".endswith("is"))

print("This is a sentence".upper())

print("THIS IS A SENTENCE".lower())

print("spam, eggs, ham".split(", "))