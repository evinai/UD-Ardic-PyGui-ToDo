
FILEPATH = "todos.txt"




def enumerate_list(to_dos):
    """Prints a list of todos with numbers"""
    for index, item in enumerate(to_dos):
        new_item = item.strip("\n")
        row = f"{index + 1}-{new_item}"
        print(row)



def get_todos(filepath=FILEPATH):
    """Returns a list of todos from a file"""
    with open(filepath, "r") as file:
        to_dos = file.readlines()
    return to_dos



def write_todos(todos_arg, filepath=FILEPATH):
    """Writes a list of todos to a file"""
    with open(filepath, "w") as file:
        file.writelines(todos_arg)



if __name__ == "__main__":
    print("Hello from functions")
    print(get_todos())
