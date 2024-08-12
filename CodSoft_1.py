print('''
        *****************************Welcome to My Calculator********************************************
''')
while True:
    n=input("Enter 7 to Continue: ")
    if n=="7":
        num1=int(input("Enter the First Number: "))
        num2=int(input("Enter the Second Number: "))
        operation=input('''        
                Press--1 For Addition
                Press--2 For Substraction
                Press--3 For Multiplication
                Press--4 For Division
                Press--9 For Exit\n''')

        if operation=="1":
            print(num1+num2)
        elif operation=="2":
            print(num1-num2)
        elif operation=="3":
            print(num1*num2)
        elif operation=="4":
            print(num1/num2)
        elif operation=="9":
            print("Exit the Application")
            break
    else:
        print("End of Application")
        break
