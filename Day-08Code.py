# Day 8 - To-Do List App
# Topic: Lists

# This Function to represent introduction of this assignment / Project. Starting with a little welcome message.
def show_intro():
    print("🔹 Welcome to Day 8 of Python 30-Day Challenge!")
    print("🔹 Topic: Lists")
    print("📝 Building a To-Do List App with basic list operations\n")

# Global todo list.
Todos = []

# function to dislay menu operations that can be performed on a to-do list.
def show_menu():
    print("\n📋 To-Do Menu:")
    print("1. Add Task")
    print("2. View All Tasks")
    print("3. Update Task")
    print("4. Remove Task")
    print("5. Pop Last Task")
    print("6. Slice Tasks")
    print("7. Exit")

# This function is used to add a task into the list.
def add_task():

    # Taking input from user and removing any extra spaces form it.
    task_text = input("🆕 Enter a task to add: ").strip()

    # We use .append() to add any task into the to-do list and displaying it.
    Todos.append(task_text)
    print(f"✅ Task added: {task_text}")

# This function is used to view the already existing tasks in to-do list.
def view_tasks():

    # If todos list is empty it alerts user that it is empty
    if len(Todos) == 0:
        print('📭 “No tasks ? No limits, Today is yours — Go make it legendary 🔥🔥🔥."')  
    # If todos isn't empty then it displays all todos in todos list
    else:
        print("🗒️ Your tasks:")
        # The for-loop iterates through the list and displays index value with task.
        for index, task in enumerate(Todos):
            print(f"{index + 1}-> {task}")

# This function is used to update the existing task
def update_task():
    # calls view_tasks() to display all existing tasks before updating one.
    view_tasks()
    try:
        # Asks user for index to update the todo, and subracts 1 from it to adjust for 0-based indexing.
        index = int(input("✏️ Enter task number to update: ")) - 1

        # This ensures that user enters a valid task index to update.
        # for example index -> 3, lengthOfTodos -> 5, then 0 <= 3 (TRUE) then 3 < 5 (TRUE); Then update task
        # for example index -> -3, lengthOfTodos -> 5, then 0 <= -3 (FALSE) then -3 < 5 (FALSE); Then don't update task instead return 
        # alert msg.
        if 0 <= index < len(Todos): # (If true prompts user to enter updated task to enter)
            updated = input("➡️ Enter new task: ")

            # Updates the Todos task at given index and displays successful msg.
            Todos[index] = updated
            print("🔁 Task updated successfully.")  

        # If false alerts user to enter valid task to update
        else:
            print("❌ That task number doesn't exist.")

        # if the user enters invalid index then display this msg.
    except ValueError:
        print("❌ Please type a valid number.")

# This function is used to remove / delete the tasks from todos
def remove_task():
    # First display all existing tasks user to choose to delete
    view_tasks()

    try:
        # This ensures that user enters a valid task index to remove / delete.
        # for example num -> 3, lengthOfTodos -> 5, then 0 <= 3 (TRUE) then 3 < 5 (TRUE); Then remove the task by using .pop(), store 
        # it in deleted variable to display what task was deleted.
        # for example num -> -3, lengthOfTodos -> 5, then 0 <= -3 (FALSE) then -3 < 5 (FALSE); Then don't remove task instead return 
        # alert msg. 
        num = int(input("🗑️ Enter task number to remove: ")) - 1
        if 0 <= num < len(Todos):

            # Here I didn't used .remove() because it removes only first occurrence of the item(Value based) in list and it doesn't 
            # returns the removed item.
            deleted = Todos.pop(num)
            print(f"✅ Removed: {deleted}")

        # If user chooses invalid task number alert user with this alert msg.
        else:
            print("❌ Invalid task number.")

    # if the user enters invalid num then display this msg.
    except ValueError:
        print("❌ That's not a number... try again?")

def PopLastTask():
    # If todo list contains todos (If true)
    if Todos:
        # Removes the last task in Todo list, stores it in removed_task and reurns it
        removed_task = Todos.pop()
        print(f"🧹 Last task popped: {removed_task}")

        # If doesn't contains any task to pop (If false)
    else:
        print("📭 Nothing to pop — list is empty!")

# This function is used to display first 3 or last 2 tasks in todo list by slicing
def slice_tasks():
    print("🔍 Slice View:")
    print("1. Show first 3 tasks")
    print("2. Show last 2 tasks")

    # Prompt user which slice view to display (1st 3 or last 2)
    view_option = input("Pick one (1/2): ")
    
    # If the option is 1, displays first 3 tasks in todo list by using slicing from 1 to 3.
    if view_option == "1":
        preview = Todos[:3]

        # If preview contains any tasks it displays them else displays None
        print(f"➡️ First 3: {preview if preview else 'None'}")

    # If the option is 2, displays last 2 tasks in todo list by using slicing from -2.
    elif view_option == "2":

        # If list gets last 2 tasks then it displays them, if there are fewer than 2 tasks then it displays all tasks in todo list.
        print(f"⬅️ Last 2: {Todos[-2:] if len(Todos) >= 2 else Todos}")

    # If user chooses invalid option it alerts the user with this alert msg.
    else:
        print("❌ Not a valid preview choice.")

# main
def main():

    # Shows introduction msg of assignment / Project to user.
    show_intro()

    # This loop runs until user chooses exit option.
    while True:

        # Shows menu to user to perform several operations on todo list.
        show_menu()

        # Taking input from user to choose any one option to perform operation on todo list. And also removing extra spaces from user 
        # input.
        Choice = input("🔢 Choose an option (1-7): ").strip()

        # Using if-elif...else to choose options (We can also use Match-case also)
        if Choice == "1":
            # If user chooses option-1 it calls add_task() to add tasks to todo list.
            add_task()

        elif Choice == "2":
            # If user chooses option-2 it calls view_task() to view existing tasks in todo list.
            view_tasks()

        elif Choice == "3":
            # If user chooses option-3 it calls update_task() to update existing tasks in todo list.
            update_task()

        elif Choice == "4":
            # If user chooses option-4 it calls remove_task() to remove tasks froms todo list.
            remove_task()

        elif Choice == "5":
            # If user chooses option-5 it calls PopLastTask() to delete recent task from todo list.
            PopLastTask()

        elif Choice == "6":
            # If user chooses option-6 it calls slice_tasks() to slice existing tasks in todo list.
            slice_tasks()

            # If user chooses option-7 it exits from loop by breaking.
        elif Choice == "7":
            print("👋 Exiting To-Do App...")  
            break

        # If user enters invalid option, alerts the user.
        else:
            print("❌ Invalid input. Try again.")


# calling main() to starting execution of program
if __name__ == "__main__":
    main()
