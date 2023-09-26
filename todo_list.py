
def add_tasks(task):
    tasks.append(task)

def update_tasks(index, updated_task):
    if 0 <= index < len(tasks):
        tasks[index] = update_task

def remove_task(index):
    if 0 <= index < len(tasks):
        del tasks[index]

if __name__ = __main__:
