# Phase-1
# Project Title: Calculator


# Printed a welcome message for the user.
print('''
        *****************************Welcome to My Calculator********************************************
''')

# Started an infinite loop to continuously ask for user input until they decide to exit
while True:
    n = input("Enter 7 to Continue & Enter any other to Exit :: ")

    # If the user enters "7", proceed with the calculator operations
    if n == "7":

        # Asked the user for input
        num1 = int(input("Enter the First Number: "))
        num2 = int(input("Enter the Second Number: "))
        operation = input('''        
                Press--1 For Addition
                Press--2 For Substraction
                Press--3 For Multiplication
                Press--4 For Division
                Press--9 For Exit\n''')

 # Performed the operation based on user input
        if operation == "1":
            print(num1+num2)
        elif operation == "2":
            print(num1-num2)
        elif operation == "3":
            print(num1*num2)
        elif operation == "4":
            print(num1/num2)
        elif operation == "9":
            print("---------------------------------------------Exiting the Application---------------------------------------------------")
            break
    else:
        print("-----------------------------------------------End of Application-------------------------------------------------------------")

        # Exit the loop and stop the program
        break
