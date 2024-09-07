# String Methods
fruit = "Banana"

# The center() method will center align the string, using a specified character (space is default) as the fill character.
print(fruit.center(14))
print(fruit.center(14, "x"))
print(fruit.center(15, "x"))

# the ljust() method will left align the string, using a specified character (space is default) as the fill character.
print(fruit.ljust(14, "o"))

# the rjust() method will left align the string, using a specified character (space is default) as the fill character.

print(fruit.rjust(14, "o"))

# the count() method returns the number of times a specified value appears in the string
text = "I love apples. apples are my favorite fruit."
print(text.count("a"))
print(text.count("apples"))

# the startswith() method returns True if the string starts with the specified value, otherwise returns False
x = "A quick brown FOX jumps over A lazy DOG"
print(x.startswith("A"))
print(x.startswith("B"))
print(x.startswith("A qui"))

print(len(x))
print(x.startswith("A", 0, 25)) # True
print(x.startswith("A", 1, 40)) # False
print(x.startswith("q", 2, 40)) # True
print(x.startswith("Q", 2, 40)) # False, string is case sensitive

print(x.endswith("DOG")) # True
print(x.endswith("G")) # True
print(x.endswith("G", 2, 39)) # True
print(x.endswith("G", 2, 30)) # False

# the find() method finds the first occurence of the specified value
# indexing start from 0
txt = "Pack My Box With Five Liquor Jugs"
print(txt.find("a"))
print(txt.find("o"))
print(txt.find("S"))
print(txt.find("Box"))
print(txt.find("Box", 10, 30))
print(txt.find("a", 10, 39))

# the index()method finds the first occurence of the specified value
# the index() method is almost the same as the find() method. The only difference is that the find() method returns -1 if the value isn't found, while the index() method makes an exception if the value isn't found
# print(index("a", 10, 39))
print(txt.find("o"))

x = "A quick brown FOX jumps over A lazy DOG"
print(x.isalnum())

fruit = "Apple483"
print(fruit.isalnum())

fruit = "483Apple"
print(fruit.isalpha()) # false because numeric number present

fruit = "Apple"
print(fruit.isalpha()) # True

fruit = "483Apple"
print(fruit.isnumeric()) # False

fruit = "483"
print(fruit.isnumeric()) # True

print("--------------------------------------")
# The replace() method replaces a string with another string [single character, partial word, full STring]
x = "   Olive      Garden   "
print(x.replace("G", "K"))
print(x.replace("Garden", "Color"))
print(x.replace("      Garden", " Garden")) # if there is a space in the middle, we can use replace()
print(x.replace("      ", " "))

x = "Hello World!"
