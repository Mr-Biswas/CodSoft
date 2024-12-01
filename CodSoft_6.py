# Phase-2
# Project Title: Timer Based Math Test

# Imported the time module for tracking time
import time
import random
# Imported the random module for generating random numbers


# List of operators that can be used in the math problems
OPERATORS = ['+', '-', '*']
# Set the minimum and maximum range for the operands (numbers in the problem)
MIN_OPERAND = 11
MAX_OPERAND = 22

# Prompted the user to input the number of problems they want to solve
TOTAL_PROBLEMS = int(input(
    '''-----------------------------------------------------------------------------------------------------------------------------------------\nNumber of problems you want to take for the test?:'''))

# Function to generate a random math problem


def generate_problem():
    # Generated two random numbers between MIN_OPERAND and MAX_OPERAND
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)
    # Randomly choose an operator from the OPERATORS list
    operator = random.choice(OPERATORS)

    # Created a string expression of the math problem
    expr = str(left) + " " + operator + " " + str(right)
    # Calculated the correct answer by evaluating the expression
    answer = eval(expr)
    # Returned both the expression and the correct answer
    return expr, answer


# Variable to track the number of wrong answers given by the user
wromg = 0

# Prompted the user to press Enter to start the timer
input("\nPress 'Enter' to start the timer! ")
print("---------------------------------------------------------------------------------------------------------------------------")

# Started the timer to track how long it takes the user to complete the quiz
start_time = time.time()

# Ran a Loop through the number of problems specified by the user
for i in range(TOTAL_PROBLEMS):
    # Generated a new problem (expression) and the correct answer
    expr, answer = generate_problem()

# Ran a Loop until the user gives the correct answer
    while True:
        # Prompted the user to solve the problem
        guess = input("Problem #" + str(i + 1) + ": " + expr + " = ")

# Checked if the user's guess is correct
        if guess == str(answer):
            break  # Exit the loop if the answer is correct
# If the guess is incorrect, increment the "wrong" answer counter
        wromg += 1

# End the timer once all problems are solved
end_time = time.time()
# Calculated the total time taken by subtracting the start time from the end time
total_time = round(end_time - start_time, 2)

# Printed the total time it took to complete the quiz
print("---------------------------------------------------------------------------------------------------------------------------------------")
print("Nice work!! \n**************You have completed in ",
      total_time, "seconds****************************")
