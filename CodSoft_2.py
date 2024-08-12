import random
letter=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's','t', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B','C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O','P', 'Q', 'S', 'T', 'U', 'V','W', 'X', 'Y', 'Z', 'R']
number= ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
character=['@', '#', '$', '%', '&', '*', '!']
print("*********************************WELCOME TO PASSWORD GENERATOR APPLICATION****************************************************")
let=int(input("Enter HOW many LETTERS to use:\n"))
num=int(input("Enter HOW many NUMBERS to use:\n"))
char=int(input("Enter HOW many CHARACTERS to use:\n"))

password=[]

for i in range(1,let+1):
    sym=random.choice(letter)
    password +=sym

for i in range(1,num+1):
    sym=random.choice(number)
    password +=sym

for i in range(1,char+1):
    sym=random.choice(character)
    password +=sym

random.shuffle(password)
new=""
for j in password:
    new+=j

print("Your strong password for your convenience is:\n", new)






