# # Description: This file is for the second day of the python workshop


# # create variables for the following :
# # 1. age
# # 2. name
# # 3. song
# # 4. food
# # 5. number
# # #now include the variables you just made print in the following...
# # Once upon a time, there was a [age] old coder named [name].
# # [name] liked to hum the song [song] while coding. It was so annoying that their teammates would
# # throw [food] until [name] would stop singing.
# # Still, [name] was the best coder on the team and could write [number] lines of code every day.
# # Maybe [song] was [name]’s secret power?
# # No one will ever know.


# # What is syntax ? What is an algorithm?
# # what is a variable? What is a string?

# # strings are nothing but plain text
# # what does this do?
# print("Giraffe \n academy")

# # or this
# phrase = "python learning"
# print(phrase + "is cool")
# #what does the + sign do? What is it called?


# #what if I wanted to get the length of a phrase?


# #what if I wanted to make the letters in the variable upper case or lower?




# #what if I wanted to check and see if the phrase was all lower or upper?


# #What if I wanted to get one letter of the phrase
new_phrase = "welcome to day 2 part 3"
print(len(new_phrase.))
print(new_phrase.upper())
#.upper is a method that makes the string all upper case
#parenthesis are used to call methods
print(new_phrase.lower())
#.lower is a method that makes the string all lower case\
print(new_phrase.islower())
#what if I wanted to check and see if the phrase was all lower or upper?
print(new_phrase[0])
print(new_phrase[1])
print(new_phrase[11])
print(new_phrase[-1])

# # The names you use when creating these labels need to follow a few rules:
# # 1. Names can not start with a number.
# # 2. There can be no spaces in the name, use _ instead.
# # 3. Can't use any of these symbols :'",<>/?|()!@#$%^&*~-+
# # 4. It's considered best practice (PEP8) that names are lowercase.
# # 5. Avoid using the characters 'l' (lowercase letter el), 'O' (uppercase letter oh), or 'I' (uppercase
# # letter eye) as single character variable names.



# # Working with numbers bold text
# # We'll learn about the following topics:
# # 1. Types of Numbers in Python
# # 2. Basic Arithmetic
# # 3. Differences between classic division and floor division


# # Addition
print(2+2)

# # Subtraction
print(2-5)
# # Multiplication
print(2*3)
# # Division
print(10/2)
# # Modulus
print(10%3)
# # Exponentiation
print (2**3)
# # Floor Division
print(10//3)
# # Order of Operations followed in Python
print(2*3+1)
# # You can use parentheses to specify the order in which you want operations to be performed.

# #to do more you need to import special math libraries from python
# #from math import *
# #this goes out and grabs some different math functions we can use
# #floor method
# #ceil method
# #sqrt method
# from math import * #import everything
# print(floor(95.76666))
# print(ceil(98.3333))
# print(sqrt(54))


# # Python has various "types" of numbers (numeric literals).
# # 1. We'll mainly focus on integers and floating point numbers. Integers are just whole numbers,
# # positive or negative. For example: 2 and -2 are examples of integers.
# # 2. Floating point numbers in Python are notable because they have a decimal point in them, or
# # use an exponential (e) to define the number. For example 2.0 and -2.1 are examples of
# # floating point numbers. 4E2 (4 times 10 to the power of 2) is also an example of a floating
# # point number in Python.



# # challenge exerces... 
# #create a program that asks for the user's name and age and then prints out the user's name and age

# # create a program that asks for the user's name and then prints out the user's name in all caps

# # create a program that asks for the user's name and then prints out the user's name in all lower case

# # create a program that asks for price and then prints out the price with a 10% discount

# # Given the phrase "Hancock High School", perform the following operations:
# # Print the phrase with a newline character to separate "Hancock" and "High" and "School".
# # Concatenate the phrase with " is cool", and print the result.
# # Print the length of the phrase.
# # Convert and print the phrase in uppercase and lowercase.
# # Check if the phrase is all lower or all upper and print the result.
# # Print the first and the last letter of the phrase.

# age = 25 #this is an integer

# name = "John" #this is a string

# song = "Happy Birthday" #this is a string

# food = "bananas" #this is a string

# number = 100 #this is an integer

# priceOfMovie = 10.99 #this is a float

# print(f'''Once upon a time, there was a {age} old coder named {name} liked to hum the song {song} while coding. It was so awesome to throw {food} until {name} would stop singing.
# Still, {name} was the best coder on the team and could write.
# Maybe {song} was the {name}'s secret power?
# No one will ever know.''')