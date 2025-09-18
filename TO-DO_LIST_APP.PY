tasks = []

print("=== Simple To-Do List ===")

choice = "0"
while choice != "4":
    print("\n1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        if len(tasks) == 0:
            print("No tasks found!")
        else:
            print("\nYour Tasks:")
            for i in range(len(tasks)):
                print(i+1, ".", tasks[i])

    if choice == "2":
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added!")

    if choice == "3":
        if len(tasks) == 0:
            print("No tasks to remove!")
        else:
            for i in range(len(tasks)):
                print(i+1, ".", tasks[i])
            task_num = int(input("Enter task number to remove: "))
            if task_num > 0 and task_num <= len(tasks):
                removed = tasks[task_num-1]
                tasks.remove(removed)
                print("Task", removed, "removed!")
            else:
                print("Invalid number!")

    if choice == "4":
        print("Now you Exit")

    if choice not in ["1", "2", "3", "4"]:
        print("Invalid choice! Try again.")

