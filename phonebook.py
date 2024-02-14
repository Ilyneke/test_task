from src import show_menu, show, new, edit, search


add_row_message = ('Введите новые данные в формате:'
                   '"фамилия, имя, отчество, название_организации, телефон_рабочий, телефон_личный"\n')
command_error_message = 'Введите число из диапазона 1-4 включительно'
exit_message = 'выход...'


def start() -> None:
    command = show_menu()
    match command:
        case 1:
            show()
        case 2:
            new()
        case 3:
            edit()
        case 4:
            search()
        case 5:
            print(exit_message)
            return
        case None:
            command_error()
    start()


def command_error() -> None:
    print(command_error_message)


if __name__ == '__main__':
    """Старт программы"""
    start()
