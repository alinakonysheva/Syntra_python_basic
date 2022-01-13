from sqlalchemy import Column, Integer, String, Date, Boolean, Float
from database import session, Base
from utils import print_title
from inputs import GetInput
from datetime import date
from dateutil.relativedelta import relativedelta

# We gaan films ingeven met een score. Elke film heeft een naam, jaar, korte omschrijving, omschrijving,
# score, speelduur, genre
# Voeg standaard acties toe zoals, alles bekijken, toevoegen, wissen, updaten.
# Voeg ook nog het volgende toe
# - bekijk films van jaar x
# - sorteer films van oud naar nieuw & nieuw naar oud - zoek films met naam X
# - sorteer films op speelduur oplopend en aflopend
# - toon alle films tussen jaar x en jaar y
# - toon alle films van genre X
# Voeg nu toe bekeken of niet. DOE DIT NIET IN HET BEGIN ! En voeg een optie toe om een film te markeren
# als gekeken of niet gekeken
# Voeg toe, alle bekeken films, alle niet bekeken films

genres = {1: 'Action', 2: 'Anime', 3: 'Blockbuster', 4: 'Family', 5: 'Comedy', 6: 'Crime', 7: 'Documentary',
          8: 'Fantasy', 9: 'Horror', 10: 'Music', 11: 'Romance', 12: 'Reality', 13: 'Sci-Fi', 14: 'Stand-Up',
          15: 'Thriller'}


class Film(Base):
    __tablename__ = 'T_FILM'

    id = Column('PK_ID', Integer, primary_key=True)
    name = Column('F_NAME', String(50))
    year = Column('F_YEAR', Integer)
    description = Column('F_SHORT_DESCRIPTION', String(250))
    full_description = Column('F_FULL_DESCRIPTION', String(250))
    score = Column('F_SCORE', Float)
    genre_id = Column('F_GENRE', Integer, default=0)
    duration = Column('F_DURATION', Integer)

    def __str__(self) -> str:
        return f'{self.name} - {self.year} {self.description} - {self.score} - {self.duration}'

    def set_year(self, value: int) -> any:
        today_year = date.today().year
        try:
            year = int(value)
            # 1895 is a year of the very first movie
            if year > today_year or year < 1895:
                raise ValueError('impossible year')
            else:
                self.year = year

        except Exception as e:
            print(f'Incorrect input ({value}):', e)
            self.year = None

    def set_duration(self, value: int) -> any:
        try:
            if value < 0:
                raise ValueError('impossible duration')
            self.duration = value
        except Exception as e:
            print(f'Incorrect input ({value}):', e)
            self.duration = None

    def set_genre_id(self, value: int) -> any:
        if value in genres.keys():
            self.genre_id = value
        else:
            self.genre_id = None

    def set_score(self, value: float) -> any:
        if 0 <= value <= 10:
            self.genre_id = value
        else:
            self.genre_id = None


def load_films():
    return session.query(Film).all()


def show_all(do_print_title=True, films=None):
    if do_print_title:
        print_title('show the whole media')
    if films is None:
        films = load_films()
    for film in films:
        print(f'{film}')

    row_count = len(films)
    if row_count == 0:
        print("no results found")
    else:
        print(f'{row_count} results were found')


def add_film() -> None:
    print_title('add film')

    f = Film()
    f.name = GetInput.get_text('Title: ')
    f.year = GetInput.get_int('Year of creation: ')
    f.description = GetInput.get_text('Description: ')
    f.full_description = GetInput.get_text('Full description: ')
    f.score = GetInput.get_float('score [from 0 to 10] ')
    f.genre_id = GetInput.get_int(f'genre: {genres}: ')
    f.duration = GetInput.get_int('duration in minutes: ')

    session.add(f)
    session.commit()


def show_with_filter():
    print_title('Filter')
    films = None

    print('1 Find films with year of creation')
    print('2 Show all films, from newest to oldest')
    print('3 Show all films, from oldest to newest')
    print('4 Find films by title')
    print('5 Show all films, from longest to shortest')
    print('6 Show all films, from shortest to longest')
    print('7 Show all films, from longest to shortest')
    print('8 Show all films, by genre')
    print('9 Show all films in between .... year en .... year')

    filter_type = GetInput.get_int('your choice ')
    if filter_type == 1:
        search = GetInput.get_int('we will be looking films by the year (9999): ')
        films = session.query(Film).filter(Film.year == search).all()
    elif filter_type == 2:
        films = session.query(Film).order_by(Film.year.desc()).all()
    elif filter_type == 3:
        films = session.query(Film).order_by(Film.year.asc()).all()
    elif filter_type == 4:
        search = f"%{GetInput.get_text('Title of the film: ')}%"
        films = session.query(Film).filter(Film.name.like(search)).all()
    elif filter_type == 5:
        films = session.query(Film).order_by(Film.duration.desc()).all()
    elif filter_type == 6:
        films = session.query(Film).order_by(Film.duration.asc()).all()
    elif filter_type == 8:
        search = GetInput.get_int(f'all films by a genre, {genres}, your choice (number): ')
        films = session.query(Film).filter(Film.genre_id == search).all()
    elif filter_type == 9:
        year_min = GetInput.get_int(f'earliest year: ')
        year_max = GetInput.get_int(f'latest year: ')
        films = session.query(Film).filter(Film.year <= year_max, Film.year >= year_min).all()
    else:
        print('there is not a right choice')

    for film in films:
        print(f'{film}')


def remove_film():
    print_title('remove a film')
    show_all(False)
    id_ = GetInput.get_int('give the ID of a film to delete: ')
    film = session.query(Film).get(id_)
    session.delete(film)
    session.commit()


def modify_film():
    print_title('modify a film')
    show_all()
    id_ = GetInput.get_int('give the ID of a film to change: ')

    f = session.query(Film).get(id_)

    if f:
        f.name = GetInput.get_text('Title: ')
        f.year = GetInput.get_int('Year of creation: ')
        f.description = GetInput.get_text('Description: ')
        f.full_description = GetInput.get_text('Full description: ')
        f.score = GetInput.get_float('score [from 0 to 10] ')
        f.genre_id = GetInput.get_int(f'genre: {genres}: ')
        f.duration = GetInput.get_int('duration in minutes: ')
        session.add(f)
        session.commit()
