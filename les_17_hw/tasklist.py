# Maak een takenlijst of todo_list:
# Een taak heeft een naam, omschrijving en een uiterste datum.
# Vraag de gebruiker om 1 of meerdere taken toe te voegen
from datetime import datetime, date
import json
from typing import List, Any
from files import create_json_file, read_json_file


def get_input_item(text: str, result_type: int = 0, retry_count: int = 5) -> any:
    """get the input

    Args:
        text (str) : text to display
        result_type (int, optional): used for converting the result to a type
                                     0 -> default -> string
                                     1 -> converts result to an int
                                     2 -> convert result to float

    Returns:
        any (int, str): result of the input
    """
    result = ''

    try:
        result = input(text).strip()
        if result_type == 1:
            result = int(result)
        elif result_type == 2:
            result = float(result.replace(',', '.'))
    except Exception as e:
        if retry_count < 5:
            result = get_input_item(text, result_type, retry_count + 1)

    return result


class Task:
    __name: str = ''
    __description: str = ''

    def __init__(self, name: str, description: str, year: int, month: int, day: int):
        """constructor
        """
        self.__name = name
        self.__description = description
        self.__datum = self.datum(year, month, day)

    @property
    def to_dict(self) -> dict:
        return dict(
            name=self.__name,
            description=self.__description,
            up_to_date=self.__datum,
        )

    def to_json(self):
        return json.dumps(self.to_dict)

    def from_dict(self, value):
        self.name = value["name"]
        self.description = value["description"]
        self.datum = value["up_to_date"]

    def from_json(self, value):
        d = json.loads(value)
        self.from_dict(d)

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value: str):
        self.__name = value

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, value: str):
        self.__description = value.strip()

    def datum(self, year: int, month: int, day: int) -> object:
        """set the datum through its own parts
        Args:
            year ([int]): year
            month ([int]): month
            day ([int]): day

        Raises:
            ValueError: month must be -> 1 and 12
            ValueError: day must be from 1 to 31 (not taking account special months)
            ValueError: the whole datum has to be later then now
            :rtype: object
        """
        now = datetime.now()

        if month < 1 or month > 12:
            raise ValueError('month is not in the correct range (1 -> 12')

        if day < 0 or day > 31:
            raise ValueError('day is not in the correct range (1 -> 31')

        pre_datum = datetime(year, month, day)

        if pre_datum < now:
            raise ValueError('date is not in the correct range, it has to be after now')

        self.__datum = pre_datum

    def __str__(self):
        return f'{self.__name} -- {self.__datum} \n {self.__description}'


def create_task(name: str, description: str, year: int, month: int, day: int) -> Task:
    """
    to create an instance of Task
    """
    t = Task(name, description, year, month, day)
    return t


def get_task():
    name = get_input_item('Geef een naam van uw taak: ')
    description = get_input_item('Schrijf uw taak hier: ')
    year = get_input_item('Tot welk jaar moet dat gedaan worden: ', 1)
    month = get_input_item('Tot welke maand moet dat gedaan worden: ', 1)
    day = get_input_item('Tot welke dag moet dat gedaan worden:', 1)

    return create_task(name, description, year, month, day)


class ToDoList:
    __filename = 'task.json'
    __tasks: list[Any] = []

    def __init__(self, filename: str = ''):
        if filename:
            self.__filename = filename

    @property
    def tasks(self) -> list:
        return self.__tasks

    @property
    def filename(self) -> str:
        return self.__filename

    def to_dict(self) -> dict:
        list_: list[Any] = []

        for task in self.tasks:
            list_.append(task.to_dict)

        output = {}
        output['data'] = list_

        return output

    def from_dict(self, json_dict: dict):
        mylist = json_dict["data"]
        for item in mylist:
            t = Task('', '', 2022, 1, 1)
            t.from_dict(item)
            self.tasks.append(t)

    def to_json(self) -> str:
        return json.dumps(self.to_dict())

    def from_json(self, json_text: str):
        if json_text:
            json_dict = json.loads(json_text)
            self.from_dict(json_dict)

    def save(self):
        create_json_file(self.to_json(), self.__filename)

    def load(self):
        file_contents = read_json_file(self.__filename)
        if file_contents:
            self.from_json(file_contents)


def create_todo_list() -> list:
    todo_list = ToDoList()
    todo_list.load()
    return todo_list


def add_task(todo_list: ToDoList):
    if todo_list:
        t = get_task()
        todo_list.tasks.append(t)


def print_todo_list(todo_list: ToDoList):
    print('-' * 30)
    print('uw taken')
    counter = 0
    if todo_list:
        for task in todo_list.tasks:
            counter += 1
            print(f'{counter}: {task}')

# сделать функцию с удалением
# сделать показать самое близкое задание
# посмотреть что сохраняется в джейсон

