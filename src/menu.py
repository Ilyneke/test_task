from .settings import MENU


welcome_message = 'Введите номер из меню:'


def show_menu() -> int | None:
    """Выводит меню в консоль и возвращает выбранный пользователь пункт"""
    menu = '\n'.join(MENU)
    print(menu)
    print(welcome_message)
    command = input()
    if command.isdigit():
        command = int(command)
        if 0 < command < len(MENU) + 1:
            return int(command)
    return
