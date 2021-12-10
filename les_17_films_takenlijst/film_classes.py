# Maak een filmlijst van de films die je bekeken hebt:
# Elke film heeft de volgende eigenschappen, naam, titel, jaar. score Vraag om deze gegevens in te geven
# Pas je programma aan zodat dit nu een lijst kan worden van meerdere films
# Pas je programma nu aan dat als je stop alles zal worden opgeslagen in een json.
# Pas je programma nu aan dat als je opstart de opgeslagen gegevens gelezen worden Toon nu een menu “film uit lijst kiezen”, “film toevoegen”, “stoppen”
# 16
import json
from typing import Dict, List, Any

from inputs import get_input_item
from datetime import datetime
from process_files import create_json_file, read_json_file


class Film:
    __title = ''
    __description = ''
    __year = None
    __score = 0.00

    def __init__(self, title: str, description: str, year: int, score: str):
        """constructor
        """
        self.__title = title
        self.__description = description
        self.__year = year
        self.__score = score

    def __str__(self):
        return f'{self.__title} \n {self.__description} - {self.__year} - {self.__score}'

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, value: str):
        self.__title = value

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, value: str):
        self.__description = value.strip()

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, value: int):
        my_val = value
        try:
            if type(my_val) != int:
                my_val = int(str(my_val).strip())
                if my_val < 1888 and my_val <= datetime.now().year:
                    self.__year = my_val
                else:
                    raise ValueError('film date has to be in between 1888 and year of today')
        except Exception as e:
            raise TypeError('please provide a valid string to convert to an integer', e)

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, value: str):
        my_val = value
        try:
            my_val = float(my_val)
        except Exception as e:
            raise ValueError('the score has to be a number', e)
        self.__score = my_val

    @property
    def to_dict(self) -> dict:
        return dict(
            title=self.title,
            description=self.description,
            year=self.year,
            score=self.score,
        )

    @property
    def to_json(self):
        return json.dumps(self.to_dict)

    def from_dict(self, value):
        self.title = value["title"]
        self.description = value["description"]
        self.year = value["year"]
        self.score = value["score"]

    def from_json(self, value):
        d = json.loads(value)
        self.from_dict(d)


def create_film(title: str, description: str, year: int, score: str) -> Film:
    """
    to create an instance of Film
    """
    return Film(title, description, year, score)


def get_film() -> Film:
    title = get_input_item('Geef een titel van uw film: ')
    description = get_input_item('Geef een korte omschrijving van de film: ')
    year = get_input_item('Geef jaar van de film: ', 1)
    score = get_input_item('Geef uw score: ')

    return create_film(title, description, year, score)


class Media_library:
    __filename = 'films.json'
    __movies = []

    def __init__(self, filename: str = ''):
        if filename:
            self.__filename = filename

    @property
    def items(self) -> list:
        return self.__movies

    @property
    def items(self) -> list:
        return self.__movies

    # разобраться что за рекурсивная фигня
    def to_dict(self):
        my_list = []
        for movie in self.items():
            my_list.append(movie.to_dict)
        output: dict[str, list[Any]] = {'data': my_list}
        return output

    def from_dict(self, jsondict: dict):
        my_list = jsondict["data"]
        for item in my_list:
            f = Film('', '', 0, '')
            f.from_dict(item)
            self.items.append(f)

    def to_json(self) -> str:
        return json.dumps(self.to_dict())

    def from_json(self, json_text: str):
        if json_text:
            json_dict = json.loads(json_text)
            self.from_dict(json_dict)

    def save(self):
        create_json_file(self.to_json(), self.__filename)

    def load(self):
        file_content = read_json_file(self.__filename)
        if file_content:
            self.from_json(file_content)


def add_movie(movies):
    if movies:
        movie = get_film()
        movies.items.append(movie)


def print_movies(movies):
    print('-' * 30)
    print('uw filmlijst')
    counter = 0
    if movies:
        for movie in movies.items:
            counter += 1
            print(f'{counter}: {movie}')
    print(f'totaal: {counter}')
