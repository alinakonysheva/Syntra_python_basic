from datetime import datetime
import json


class Song:
    __title: str = ''
    __artist: str = ''
    __year: int = datetime.now().year
    __album: str = ''

    def __init__(self, title: str, artist: str, year: int, album: str):
        """constructor
        """
        self.__title = title
        self.__artist = artist
        self.__year = year
        self.__album = album

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, value: str):
        self.__title = value

    @property
    def artist(self) -> str:
        return self.__artist

    @artist.setter
    def artist(self, value: str):
        self.__artist = value

    @property
    def album(self) -> str:
        return self.__album

    @album.setter
    def album(self, value: str):
        self.__album = value

    @property
    def year(self) -> int:
        return self.__year

    @year.setter
    def year(self, value: int):
        self.__year = value

    @property
    def to_dict(self) -> dict:
        return dict(
            title=self.__title,
            artist=self.__artist,
            year=self.__year,
            album=self.__album,
        )

    def to_json(self):
        return json.dumps(self.to_dict)

    def from_dict(self, value):
        self.title = value["title"]
        self.artist = value["artist"]
        self.year = value["year"]
        self.album = value["album"]

    def from_json(self, value):
        d = json.loads(value)
        self.from_dict(d)

    def __str__(self):
        return f'{self.__title} -- {self.__artist} -- {self.__album} -- {self.__year}'

    @classmethod
    def createNewSong(cls, title: str, artist: str, year: int, album: str):
        return cls(title, artist, year, album)


import os

C_FILE = 'test.json'


def __get_filename(name: str):
    filename = name.strip()
    if filename == '':
        filename = C_FILE
    return filename


def create_json_file(contents: str, name: str = ''):
    try:
        with open(__get_filename(name), 'w') as f:
            f.write(contents)
    except Exception as e:
        print('create_json_file: {}'.format(e))
        return False

    return True


def read_json_file(name: str = '') -> str:
    filename = __get_filename(name)
    contents = ''
    if os.path.exists(filename):
        try:
            with open(filename, 'r') as f:
                contents = str(f.read())
        except Exception as e:
            print('read_json_file: {}'.format(e))

    return contents


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


def get_song() -> Song:
    title = get_input_item('Geef naam van een liedje: ')
    artist = get_input_item('Geef een naam van een artiest: ')
    album = get_input_item('Geef een album: ')
    year = get_input_item('Geef een jaar  ', 1)
    s = Song.createNewSong(title, artist, year, album)
    return s


class MediaLibrary:
    __songs_list = []
    __filename = 'songs.json'

    def __init__(self, filename: str = ''):
        self.__songs_list = []
        if filename != '':
            self.__filename = filename

    @property
    def songs_list(self) -> list:
        return self.__songs_list

    @property
    def filename(self) -> str:
        return self.__filename

    def to_dict(self) -> dict:
        list_ = []

        for song in self.__songs_list:
            list_.append(song.to_dict)

        output = {'data': list_}

        return output

    def from_dict(self, json_dict: dict):
        list_ = json_dict["data"]
        for item in list_:
            s = Song('', '', datetime.now().year, '')
            s.from_dict(item)
            self.__songs_list.append(s)

    def to_json(self) -> str:
        return json.dumps(self.to_dict())

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


def create_movie(name: str, year: int, desc: str, score: float):
    return Movie(name, desc, year, score)


def create_movielist() -> list:
    movies = MovieList()
    movies.load()
    return movies


def get_input_movie() -> Movie:
    print('-' * 30)
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
    print('-' * 30)
    print('uw filmlijst')
    counter = 0
    if movies is not None:
        for movie in movies.items:
            counter += 1
            print('{}: {}'.format(counter, movie))
    print('totaal: {}'.format(counter))
