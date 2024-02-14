import csv
import os

from .settings import FIELD_NAMES, NOT_FOUND_MESSAGE


def read() -> list[dict] | None:
    """Чтение файла, возвращает список записей в виде словарей"""
    if os.path.isfile('phonebook.csv'):
        with open('phonebook.csv', 'r') as csv_file:
            reader = csv.DictReader(f=csv_file, fieldnames=FIELD_NAMES)
            reader = [row for row in reader]
        return reader
    else:
        print(NOT_FOUND_MESSAGE)


def write(row: list) -> None:
    """Запись в файл, добавляет строки"""
    with open('phonebook.csv', 'a') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        writer.writerow(row)


def just_read_list() -> list[list]:
    """Чтение файла, возвращает записи в виде списков"""
    with open('phonebook.csv', 'r') as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        return list(reader)


def rewrite(rows: list) -> None:
    """Запись в файл, старая информация теряется"""
    with open('phonebook.csv', 'w') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        writer.writerows(rows)
