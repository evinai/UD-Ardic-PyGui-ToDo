from functions import *
import time


now = time.strftime("%b %d, %Y - %H:%M:%S")



print("It is: ", now)
while True:
    # get user input and strip space chars from it
    user_action = input("Type add, show, complete editor exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        try:
            todo = user_action[4:] + "\n"
            if todo[4:] == "":
                raise ValueError("You must enter a todo.")
            else:
                todos = get_todos()
                todos.append(todo)
                write_todos(todos)

        except ValueError:
            print("Your command is not valid. Please try again.")
            continue


    elif user_action.startswith("show") or user_action.startswith("display"):

        todos = get_todos()

        enumerate_list(todos)

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = get_todos()

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + "\n"

            write_todos(todos)

        except ValueError:
            print("Your command is not valid. Please try again.")
            continue  # goes to the beginning of the loop



    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])

            todos = get_todos()

            index = number - 1
            todo_to_remove = todos[index].strip("\n")
            todos.pop(index)

            write_todos(todos)
            enumerate_list(todos)
            message = f"Todo {todo_to_remove} was removed from the list."
            print(message)

        except IndexError:
            print("There is no item with that number. Please try again.")
            continue

    elif 'exit' in user_action:
        break

    else:
        print("Unknown command")
