# Phase-2
# Project Title: Typing Speed Check Game


# Imported random module with alias 'r' to use random.choice() for selecting random sentences
import random as r
# Imported all functions from the time module (specifically, time() for timing)
from time import *


# Function to calculate the number of mistakes the user made while typing

def mistake(partest, usertest):
    error = 0  # Initialize the error counter
    # Iterate through each character of the test sentence
    for i in range(len(partest)):
        try:
            # Check if the character typed by the user matches the original
            if partest[i] != usertest[i]:
                error += 1
                # If it doesn't match, incremented the error counter
        # If the user types fewer characters than the test sentence
        except:
            error += 1
            # Incremented the error counter for missing characters
    return error

# Function to calculate the typing speed in words per second


def speed_time(time_st, time_en, userinput):
    # Calculated the time taken by the user to type the sentence
    time_delay = time_en - time_st
    # Rounded the time to two decimal places
    time_R = round(time_delay, 2)
    # Calculated speed (characters per second)
    speed = len(userinput)/time_R
    return round(speed)
# Returned the speed rounded to the nearest whole number


# Main loop for the typing test game
while True:

    # Asked the user if they are ready to start the typing test
    ck = input("""\n-----------------------------------Typing Speed Check Game ----------------------------------\nAre you Ready?? yes/no: """)
# If the user says 'yes'
    if ck == "yes":
        # Predefined test sentences
        test = [
            "The national animal of India is Tiger.",
            "The national bird of India is Peacock.",
            "What is the ratio of width of our national flag to its length?",
            "National Vegetable of India is Pumpkin."
        ]

# Selected a random sentence from the list
        test1 = r.choice(test)
        print("************ Please be Carefull !! ******************")
        print(test1)  # Display the selected test sentence
        print()
        print()

# Started the timer and record the time when the user starts typing
        # Found the current time before user starts typing
        time1 = time()
        testinput = input("Enter: ")
        time2 = time()
        # Captured the time after the user finishes typing

        # Calculated and display the typing speed in words per second
        print('Speed:', speed_time(time1, time2, testinput), "w/sec")

        # Calculated and display the number of mistakes made
        print("Error: ", mistake(test1, testinput))

# If the user says 'no', exit the loop
    elif ck == "no":
        print("-----------------------------------------------------Thank You!! See You Again-------------------------------------------------")
        break

# If the user inputs anything other than 'yes' or 'no'
    else:
        print("You Pressed something Wrong..Sorry for the inconvenience, Test again!")
