
def add_tasks(task, date_due):
    tasks.append((task, date_due))

def update_task(index, updated_task, updated_date_due):
    if 0 <= index < len(tasks):
        tasks[index] = (updated_task, updated_date_due)

def delete_task(index):
    if 0 <= index < len(tasks):
        del tasks[index]

def save_task_to_file(file_name):
    with open(file_name, "w") as file:
        for task, date_due in tasks:
            file.write(f"{task},{date_due}\n")

def load_task_to_file(file_name):
    try:
        with open(file_name, "r") as file:
            lines = file.readlines()
        return [line.strip().split(",") for line in lines]
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
            date_due = input("Enter the due date in the form of mm-dd-yyyy: ")
            add_tasks(task, date_due)
        elif userChoice == "2":
            for i, (task, date_due) in enumerate(tasks):
                print(f"{i + 1}. {task} (Date Due: {date_due})")   
        elif userChoice == "3":
            index = int(input("Enter the number of the task you want to update: ")) -1
            updated_task = input("Enter the updated task: ")
            updated_due_date = input("Enter the new due date in the form of mm-dd-yyyy: ")
            update_task(index, updated_task, updated_due_date)
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