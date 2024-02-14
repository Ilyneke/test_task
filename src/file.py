import csv
import os
import logging

from .settings import FIELD_NAMES, NOT_FOUND_MESSAGE, FILENAME, DELIMITER


def read() -> list[dict] | None:
    """Чтение файла, возвращает список записей в виде словарей"""
    if os.path.isfile(FILENAME):
        with open(FILENAME, 'r') as csv_file:
            reader = csv.DictReader(f=csv_file, fieldnames=FIELD_NAMES, delimiter=DELIMITER)
            reader = [row for row in reader]
        return reader
    else:
        logging.warning(NOT_FOUND_MESSAGE)


def write(row: list) -> None:
    """Запись в файл, добавляет строки"""
    with open(FILENAME, 'a') as csv_file:
        writer = csv.writer(csv_file, delimiter=DELIMITER)
        writer.writerow(row)


def just_read_list() -> list[list]:
    """Чтение файла, возвращает записи в виде списков"""
    with open(FILENAME, 'r') as csv_file:
        reader = csv.reader(csv_file, delimiter=DELIMITER)
        return list(reader)


def rewrite(rows: list) -> None:
    """Запись в файл, старая информация теряется"""
    with open(FILENAME, 'w') as csv_file:
        writer = csv.writer(csv_file, delimiter=DELIMITER)
        writer.writerows(rows)
