#Building a TO DO LIST in Python

#declaring a function TASK
def task():
    tasks = []   #empty list
    print("---Welcome to the To Do List---")

    total_tasks = int(input("Enter number of tasks you want to add:"))
    for i in range(1,total_tasks+1):
        task_name = input(f"Enter task {i} :")
        tasks.append(task_name)
    print(f"Today's tasks are\n {tasks}")

    while True:
        #taking operation(opr) input
        opr = int(input(
            "\nEnter:\n"
            "1 - Add\n"
            "2 - Update\n"
            "3 - Delete\n"
            "4 - View\n"
            "5 - Exit\n"
        ))

        #adding the task to the TO DO LIST
        if opr == 1 :
            add = input("Enter the task you want to add:")
            tasks.append(add)
            print(f"Task {add} has been successfully added to the TO DO LIST...")
            print("The New To Do List after adding the task is",tasks)

        #updating the TO DO LIST    
        elif opr == 2 :
            task_to_be_upd = input("Enter the task to be updated:")
            #nested conditional statements
            if task_to_be_upd in tasks :
                updated_task = input("Enter the new task:")
                ind = tasks.index(task_to_be_upd)  #returns the index
                tasks[ind] = updated_task
                print(f"Task {task_to_be_upd} has been successfully updated...")
                print("The new updated To Do List is:",tasks)

            else :
                print("Task not found")
        
        #deleting the task from the TO DO LIST
        elif opr == 3 :
            task_to_be_del = input("Enter the task yo want to delete:")
            if task_to_be_del in tasks :
                ind = tasks.index(task_to_be_del)  #returns the index
                del tasks[ind]  #deletes the task present at returned index
                print(f"Task {task_to_be_del} has been deleted from the TO DO LIST...")
                print("The modified To Do List after deleting is:",tasks)

        #viewing the final TO DO LIST
        elif opr == 4 :
            print(f"The TO DO LIST is {tasks}")

        #exiting the TO DO LIST
        elif opr ==5 :
            print("Exiting the TO DO LIST...")

        else :
            print("INVALID INPUT.\n ENTER THE CORRECT INPUT:")

#calling the function TASK
task()
