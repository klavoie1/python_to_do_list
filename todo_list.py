
def add_tasks(task):
    tasks.append(task)

def update_task(index, updated_task):
    if 0 <= index < len(tasks):
        tasks[index] = updated_task

def delete_task(index):
    if 0 <= index < len(tasks):
        del tasks[index]

def save_task_to_file(file_name):
    with open(file_name, "w") as file:
        for task in tasks:
            file.write(f"{task}\n")

def load_task_to_file(file_name):
    try:
        with open(file_name, "r") as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
            return []

if __name__ == "__main__":
    file_name = "todolist.txt"

    # file is loaded before program runs
    tasks = load_task_to_file(file_name)

    while True:
        print("\n---Todo List---\n")
        print("  Options")
        print("  -------  ")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Save and Exit")
        print("6. Exit without Saving")
        print("----------------")

        userChoice = input("Select which choice you would like: ")

        if userChoice == "1":
            task = input("Enter your task: ")
            add_tasks(task)
        elif userChoice == "2":
            for i, task in enumerate(tasks):
                print(f"{i + 1}. {task}")   
        elif userChoice == "3":
            index = int(input("Enter the number of the task you want to update: ")) -1
            updated_task = input("Enter the updated task: ")
            update_task(index, updated_task)
        elif userChoice == "4":
            index = int(input("Enter the task you wish to remove: ")) -1
            delete_task(index)
        elif userChoice == "5":
            save_task_to_file(file_name)
            break
        elif userChoice == "6":
            break
        else:
            print("That's an invalid option. Please reenter a value.")