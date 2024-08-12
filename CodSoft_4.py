def task():
    tasks=[]
    print("------------Welcome to my To-Do-List------------------------------")

    total=int(input("Number of task or tasks you want to add? = "))
    for i in range(1, total+1):
        task_name= input(f"Provide task name {i} = ").lower()
        tasks.append(task_name)
        # print(task_name)

    print(f"Today's task are\n{tasks}")

    while True:
        operation= int(input("Enter\n1-Add\n2-Update\n3-Delete\n4-View\n5-Stop\n"))

        if operation==1:
            add=input("Enter Tasks for the Day= ").lower()
            tasks.append(add)
            print(f"Task {add} has been added...........")

        elif operation==2:
            update=input("Enter task You want to Update= ").lower()
            if update in tasks:
                new=input("Enter New task: ").lower()
                ind= tasks.index(update)
                tasks[ind]=new
                print(f"Updated task is {update}")
            else:
                print("The value is not there!!!!!!!!")
        
        elif operation==3:
            del_val= input("Enter value to Delete: ").lower()
            if del_val in tasks:
                ind=tasks.index(del_val)
                del tasks[ind]
                print(f"TASK {del_val} has been deleted.............")

        elif operation==4:
            print(f"Today's Task or Tasks= {tasks}")
        elif operation==5:
            print("Closing the Program........")
            break
        else:
            print("Invalid Entry")

task()
