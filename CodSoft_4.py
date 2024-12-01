# Phase-1
# Project Title: To-Do-List


# Defined a function
def task():
    # Initialized an empty list to hold tasks
    tasks = []

# Printed a welcome message or header for the to-do list
    print("------------------------------------------------------To-Do-List---------------------------------------------")

# Asked the user how many tasks they want to add at the beginning
    total = int(input("Number of task or tasks you want to add?: "))

# Ran a Loop to add multiple tasks (as per the user's input)
    for i in range(1, total+1):
        # Prompted the user to input a task name
        task_name = input(f"Provide task name {i} = ").lower()

# Added the task name to the list of tasks (convert input to lowercase)
        tasks.append(task_name)

# Printed the list of tasks
    print(f"Today's task are\n{tasks}")

# Started an infinite loop to continuously perform operations
    while True:
        # Asked the user to choose an operation from the menu
        operation = int(
            input("\nEnter\n1-Add\n2-Update\n3-Delete\n4-View\n5-Stop\n"))

# Asked the user to add a new task
        if operation == 1:
            # Prompted the user to enter a new task to add
            add = input("Enter Tasks for the Day= ").lower()

# Appended the new task to the list
            tasks.append(add)

# Printed a confirmation message
            print(f"Task {add} has been added...........")

# Ask the user to update an existing task
        elif operation == 2:
            # Asked the user for the task they want to update
            update = input("Enter task You want to Update= ").lower()

# Checked if the task exists in the list
            if update in tasks:
                # If the task is found, ask the user for the new task description
                new = input("Enter New task: ").lower()

                ind = tasks.index(update)

# Updated the task at the found index with the new task
                tasks[ind] = new

# Printed a confirmation message
                print(f"Updated task is {update}")
            else:
                # If the task does not exist, printed an error message
                print("The value is not there!!!!!!!!")

# If the user chooses to delete an existing task
        elif operation == 3:
            # Prompted the user for the task they want to delete
            del_val = input("Enter value to Delete: ").lower()

# Checked if the task exists in the list
            if del_val in tasks:
                # Found the index of the task to delete
                ind = tasks.index(del_val)

 # Deleted the task at the found index
                del tasks[ind]

# Print a confirmation message
                print(f"TASK {del_val} has been deleted.............")

# If the user chooses to view the current list of tasks
        elif operation == 4:
            # Printed all the current tasks
            print(f"Today's Task or Tasks= {tasks}")

# If the user chooses to stop the program
        elif operation == 5:
            # Printed a message indicating the program is closing
            print("Closing the Program........")
            break
# Break the loop and end the program

# If the user enters an invalid option
        else:
            # Printed an error message for invalid input
            print("Invalid Entry")


# Called the function to start the to-do list program
task()
