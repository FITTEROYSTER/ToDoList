todos = []

while True:
    user_action = input('Type add, show, edit or exit: ')
    match user_action.strip():
        case 'add':
            todo = input('Enter a ToDo: ')
            todos.append(todo)
        case 'show':
            for item in todos:
                print(item.title())
        case 'edit':
            number = int(input("Number of the ToDo to edit: "))
            number = number - 1
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo
        case 'exit':
            break

print("Bye!")

