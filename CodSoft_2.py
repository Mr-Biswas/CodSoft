# Phase-1
# Project Title: PassWord Generator

# Imported the random module
import random

# Defined the list of characters to choose from for letters, numbers, and special characters
letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
          'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'R']
number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
character = ['@', '#', '$', '%', '&', '*', '!']

# Printed a welcome message to the user
print("*********************************WELCOME TO PASSWORD GENERATOR APPLICATION****************************************************")

# Collected user input for how many letters, numbers, and characters to include in the password
let = int(input("Enter HOW many LETTERS to use:\n"))
num = int(input("Enter HOW many NUMBERS to use:\n"))
# Number of special characters
char = int(input("Enter HOW many CHARACTERS to use:\n"))

# Initialized an empty list to hold the components of the password
password = []

for i in range(1, let + 1):
    # Selected a random letter from the letter list
    sym = random.choice(letter)
# Added the letter to the password list
    password += sym

# Added 'num' number of random numbers to the password
for i in range(1, num + 1):
    sym = random.choice(number)
    password += sym

# Added 'char' number of random characters to the password
for i in range(1, char + 1):

    # Selected a random special character from the character list
    sym = random.choice(character)
# Added the character to the password list
    password += sym

# Shuffled the password list to mix up the characters, making the password more random
random.shuffle(password)

# Joined all the elements in the password list to form a single string
new = ""
for j in password:
    # Concatenated each character into a new string
    new += j

# Displayed the generated password to the user
print("---------------------------------The Generated password below:-----------------------------------------\n", new)
