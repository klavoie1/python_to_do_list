
def add_tasks(task):
    tasks.append(task)

def update_task(index, updated_task):
    if 0 <= index < len(tasks):
        tasks[index] = update_task

def delete_task(index):
    if 0 <= index < len(tasks):
        del tasks[index]

if __name__ == "__main__":
    tasks = []

    while True:
        print("---Todo List---\n")
        print("  Options")
        print("  -------  ")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Quit")
        print("----------------")

        userChoice = input("Select which choice you would like: ")

        if userChoice == "1":
            task = input("Enter your task: ")
            add_tasks(task)
        elif userChoice == "2":
            for i, task in enumerate(tasks):
                print(f"{i + 1}. {task}")
                if tasks == []:
                    print("There are no tasks. Try adding one!")
        elif userChoice == "3":
            index = int(input("Enter the number of the task you want to update: ")) -1
            updated_task = input("Enter the updated task: ")
            update_task(index, update_task)
        elif userChoice == "4":
            index = int(input("Enter the task you wish to remove: ")) -1
            delete_task(index)
        elif userChoice == "5":
            break
        else:
            print("That's an invalid option. Please reenter a value.")