from inputs import get_input_item
from datetime import datetime
from json import dumps, loads
from files import create_json_file, read_json_file

class Movie():
    def __init__(self, name, description, year, score):
        self.name = name
        self.description = description
        self.year = year
        self.score = score

    def __str__(self):
        return '{name} - {score} - {year} - {short}'.format(
            name=self.name,
            score=self.score,
            year=self.year,
            short='{}...'.format(self.description[0:15])
        )

    @property
    def name(self) -> str:
        return self.__name
    
    @name.setter
    def name(self, value: str):
        self.__name = value.strip()

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, value: str):
        self.__description = value.strip()

    @property
    def year(self) -> int:
        return self.__year

    @year.setter
    def year(self, value: int):
        myval = value
        try:
            if type(myval) != int:
                myval = int(str(myval).strip())    
        except:
            raise TypeError('please provide a valid a string to convert or an integer')

        if myval < 1888 and myval >= datetime.now().year:
            raise ValueError('movie date must be after 1888 or maximum now')   

        self.__year = myval

    @property
    def score(self) -> float:
        return self.__score


    @score.setter
    def score(self, value: float):
        myval = value
        try:
            if type(myval) != float:
                myval = float(str(myval).strip().replace(',', '.'))    
        except:
            raise TypeError('please provide a valid a string to convert to a score or a float')

        if myval < 0.0 or myval > 10.0:
            raise ValueError('score must be between 0 and 10')         

        self.__score = myval

    @property
    def to_dict(self) -> dict:
        return dict(
           name=self.name,
           score=self.score,
           year=self.year,
           description=self.description        
        )

    @property
    def to_json(self) -> str:
        return dumps(self.to_dict)

    def from_dict(self, jsondict: dict):
        self.name = jsondict["name"]
        self.score = jsondict["score"]
        self.year = jsondict["year"]
        self.description = jsondict["description"]

    def from_json(self, jsontext: str):
        jsondict = loads(jsontext)
        self.from_dict(jsondict)        


class MovieList():  
    __filename = 'movies.json'

    def __init__(self, filename: str =''):
        self.__movies = []
        if filename != '':
            self.__filename = filename
 
    @property
    def items(self) -> list:
        return self.__movies

    @property
    def filename(self) -> str:
        return self.__filename

    def to_dict(self) -> dict:
        mylist = []

        for movie in self.items:
            mylist.append(movie.to_dict)

        output = {}
        output['data'] = mylist

        return output

    def from_dict(self, jsondict: dict):
        mylist = jsondict["data"]
        for item in mylist:
            m = Movie('', '', 0, 0)
            m.from_dict(item)
            self.items.append(m)

    def to_json(self) -> str:
        return dumps(self.to_dict())

    def from_json(self, jsontext: str):
        if jsontext != '':
            jsondict = loads(jsontext)
            self.from_dict(jsondict)

    def save(self):
        create_json_file(self.to_json(), self.__filename)

    def load(self):
        filecontents = read_json_file(self.__filename)
        if filecontents != '':
            self.from_json(filecontents)


def create_movie(name: str, year: int, desc: str, score:float ):
    return Movie(name, desc, year, score)

def create_movielist() -> list:
    movies = MovieList()
    movies.load()
    return movies


def get_input_movie() -> Movie:
    print('-'*30)
    print('film toevoegen')
    name = get_input_item('geef de naam: ')
    year = get_input_item('geef het jaar: ', 1)
    desc = get_input_item('omschrijving: ')
    score = get_input_item('score: ', 2)

    return create_movie(name, year, desc, score)


def add_movie(movies):
    if movies is not None:
        movie = get_input_movie()
        movies.items.append(movie)

def print_movies(movies):
    print('-'*30)
    print('uw filmlijst')
    counter = 0
    if movies is not None:
        for movie in movies.items:
            counter +=1
            print('{}: {}'.format(counter, movie))
    print('totaal: {}'.format(counter))