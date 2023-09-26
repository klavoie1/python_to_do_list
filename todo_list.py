
def add_tasks(task):
    tasks.append(task)

def update_tasks(index, updated_task):
    if 0 <= index < len(tasks):
        tasks[index] = update_task

def remove_task(index):
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
        print("4. Remove Task")
        print("5. Quit")
        print("----------------")

        userChoice = input("Select which choice you would like: ")

        