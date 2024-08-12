import random
while True:
    n=input("Press 1 to Continue and 2 to Exit:")
    if n=="1":
        u_choice=int(input('Enter your Choice: Press 1 for ROCK, 2 for Paper, 3 for SCISSOR: '))
        if u_choice>=4 or u_choice<0:
            print("Invalid Input")
        else:
            c_choice=random.randint(1,3)
            print("Computer Choice: ", c_choice)
            if c_choice==u_choice:
                print("DRAW\n")

            elif c_choice==1 and u_choice==3:
                print("You Lose\n")

            elif u_choice==3 and c_choice==1:
                print("You Won\n")

            elif c_choice > u_choice:
                print("You Lose\n")

            elif u_choice > c_choice:
                print("You Won\n")
    else:
        print("Exit the Application")
        break


