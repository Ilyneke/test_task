import csv
import os

from .settings import FIELD_NAMES


not_found_message = "Файл phonebook.csv не найден, поэтому был создан новый"


def _create() -> csv.DictReader:
    pass


def read() -> csv.DictReader:
    if os.path.isfile('phonebook.csv'):
        with open('phonebook.csv') as csv_file:
            reader = csv.DictReader(f=csv_file, fieldnames=FIELD_NAMES)
        return reader


def write():
    pass
