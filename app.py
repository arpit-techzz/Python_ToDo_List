class total_task:
    """Small task manager that provides the application's task operations."""

    def __init__(self, tasks=None):
        self.tasks = list(tasks or [])

    def add(self, task_name):
        self.tasks.append(task_name)

    def update(self, old_task, new_task):
        if old_task not in self.tasks:
            return False
        self.tasks[self.tasks.index(old_task)] = new_task
        return True

    def delete(self, task_name):
        if task_name not in self.tasks:
            return False
        self.tasks.remove(task_name)
        return True

    def view(self):
        return self.tasks.copy()


def task():
    print("----Welcome To The Management App----")

    while True:
        try:
            task_count = int(input("Enter how many task you want to add = "))
            if task_count < 0:
                raise ValueError
            break
        except ValueError:
            print("Please enter a non-negative whole number.")

    manager = total_task()
    for i in range(1, task_count + 1):
        task_name = input(f"Enter task {i} = ")
        manager.add(task_name)

    print(f"Today's tasks are\n{manager.view()}")

    while True:
        try:
            operation = int(input("Enter 1-Add\n2-Update\n3-Delete\n4-View\n5-Exit/Stop/ "))
        except ValueError:
            print("Please enter a number from 1 to 5.")
            continue

        if operation == 1:
            add = input("Enter task you want to add = ")
            manager.add(add)
            print(f"Task {add} has been successfully added...")

        elif operation == 2:
            updated_val = input("Enter the task name you want to update = ")
            new_task = input("Enter new task = ")
            if manager.update(updated_val, new_task):
                print(f"Updated task {new_task}")
            else:
                print("Task not found.")

        elif operation == 3:
            del_val = input("Which task you want to delete = ")
            if manager.delete(del_val):
                print(f"Task {del_val} has been deleted...")
            else:
                print("Task not found.")

        elif operation == 4:
            print(f"Total Tasks = {manager.view()}")

        elif operation == 5:
            print("Closing the program....")
            break

        else:
            print("Invalid Input")


if __name__ == "__main__":
    task()

