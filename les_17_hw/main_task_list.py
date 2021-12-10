from tasklist import create_todo_list, add_task, print_todo_list, get_input_item


def main_menu() -> int:
    print('-' * 30)
    print('Kies maar')
    print('1. Taken bekijken')
    print('2. Taak toevoegen')
    print('3. Stopppen')
    return get_input_item('geef uw keuze: ', 1)


def main_loop(todo_list: list):
    if todo_list:
        choice = 1
        while choice in [1, 2]:
            choice = main_menu()
            if choice == 1:
                print_todo_list(todo_list)
            elif choice == 2:
                add_task(todo_list)
            else:
                todo_list.save()


def main():
    todo_list = create_todo_list()
    main_loop(todo_list)


if __name__ == '__main__':
    main()
