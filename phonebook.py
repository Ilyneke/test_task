import logging
import sys

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
            logging.info(exit_message)
            return
        case None:
            logging.warning(command_error_message)
    start()


if __name__ == '__main__':
    """Старт программы"""
    logging.basicConfig(stream=sys.stdout, level=logging.INFO, format='%(levelname)s %(message)s')
    start()
