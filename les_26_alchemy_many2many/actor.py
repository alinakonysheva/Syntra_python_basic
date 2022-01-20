from inputs import GetInput
from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship
from database import session, BaseTest
from utils import print_title


# We gaan acteurs en films bijhouden. Leg een link tussen beide.
# Maak een overzicht van films en acteurs, zoekmogelijheden op jaar,
# naam, score. Maar ook gebruik van een base klasse.


class Actor(BaseTest):
    __tablename__ = 'T_ACTOR'
    name = Column('F_NAME', String(200))
    films = relationship('FilmActor', back_populates='actor')

    def __str__(self) -> str:
        return f'{self.id} - {self.name} '


def load_actors() -> list[Actor]:
    return session.query(Actor).all()


def show_all_actors(do_print_title=True):
    if do_print_title:
        print_title('All actors')
        list_with_actors = load_actors()
        for a in list_with_actors:
            print(a.id, a.name)


def search_actor():
    inp = GetInput.get_text('name of an actor:')
    qry = session.query(Actor)
    if inp:
        qry.filter(Actor.name.like(f'%{inp}%'))
        actors = qry.all()

        for actor in actors:
            films = actor.films
            if len(films) > 0:
                for f in actor.films:
                    print(f'{actor.name}: his/her film: {f.film.name} in {f.film.year}')
            else:
                print(f'{actor.name} has no films yet. Go get them girl/boy!')

        row_count = len(actors)
        if row_count == 0:
            print("no results found")
        else:
            print(f'{row_count} results were found')


def add_change_actor(create_new=False):
    if create_new:
        print_title('add a new actor')
        a = Actor()
        a.name = GetInput.get_text('name of the actor: ')
        session.add(a)
        session.commit()

    else:
        print_title('choose an actor first')
        inp = GetInput.get_int('id of an actor')
        a = session.query(Actor).get(inp)
        if a:
            a.name = GetInput.get_text('name ')
            session.add(a)
            session.commit()


class Film(BaseTest):
    __tablename__ = 'T_FILM'
    name = Column('F_NAME', String(200))
    year = Column('F_YEAR', Integer)
    score = Column('F_SCORE', Float)
    actors = relationship('FilmActor', back_populates='film')


""" @property
 def year(self):
     return self._year

 @year.setter
 def year(self, value):
     if 1895 < value < 2022:
         self._year = value
     else:
         raise ValueError

 @property
 def name(self):
     return self._name

 @year.setter
 def name(self, value):
     if 1 <= len(value):
         self._name = value
     else:
         raise ValueError

 def __str__(self) -> str:
     return f'{self.id} - {self.name} {self.year} - {self.score}'"""


def load_films() -> list[Film]:
    return session.query(Film).all()


def show_all_films(do_print_title=True, films=None):
    if do_print_title:
        print_title('All films')
    if films is None:
        films = load_films()
    for film in films:
        if len(film.actors) > 0:
            actors_ = list(map(lambda x: x.actor.name, film.actors))
        else:
            actors_ = []
        print(f'Title: {film.name}, actors: {actors_}')

    row_count = len(films)
    if row_count == 0:
        print("no results found")
    else:
        print(f'{row_count} results were found')


def search_film(choice):
    """

    :param choice:
    1 - search by name,
    2 - search between year1 and year2
    3 - search between score1 and score2
    :return:
    """

    if choice == 1:
        inp = GetInput.get_text('title of a film: ')
        qry = session.query(Film)
        if inp:

            films = qry.filter(Film.name.like(f'%{inp}%')).all()

            for film in films:
                actors = film.actors
                if len(actors) > 0:
                    for a in film.actors:
                        print(f'{film.name}: {a.actor.name} ')
                else:
                    print(f'{film.name} has no actors yet.')

            row_count = len(films)
            if row_count == 0:
                print("no results found")
            else:
                print(f'{row_count} results were found')
    elif choice == 2:
        min_year = GetInput.get_int('min year: ')
        max_year = GetInput.get_int('max year: ')
        qry = session.query(Film)
        if min_year and max_year:
            films = qry.filter((Film.year >= min_year), (Film.year <= max_year)).all()
            for film in films:
                print(f'{film.name}')
            row_count = len(films)
            if row_count == 0:
                print("no results found")
            else:
                print(f'{row_count} results were found')
        else:
            print('something wrong with your inputs, dear')

    elif choice == 3:
        min_score = GetInput.get_int('min score: ')
        max_score = GetInput.get_int('max score: ')
        qry = session.query(Film)
        if min_score and max_score:
            films = qry.filter((Film.score > min_score), (Film.score < max_score)).all()
            for film in films:
                print(f'{film.name}')
            row_count = len(films)
            if row_count == 0:
                print("no results found")
            else:
                print(f'{row_count} results were found')
        else:
            print('something wrong with your inputs, dear')


def add_change_film(create_new=False):
    if create_new:
        print_title('add a new film')
        f = Film()
        f.name = GetInput.get_text('title of the film: ')
        f.score = GetInput.get_float('score of the film: ')
        f.year = GetInput.get_int('year of the film: ')
        session.add(f)
        session.commit()

    else:
        print_title('choose a film first')
        inp = GetInput.get_int('id of a film')
        f = session.query(Film).get(inp)
        if f:
            f.name = GetInput.get_text('title of the film: ')
            f.score = GetInput.get_float('score of the film: ')
            f.year = GetInput.get_int('year of the film: ')
            session.add(f)
            session.commit()
        else:
            print(f'there is no film with id {inp}')


def add_actors_to_film():
    inp_f = GetInput.get_int('id of a film')
    inp_a = True
    f = session.query(Film).get(inp_f)
    if f:
        while inp_a:
            inp_a = GetInput.get_int('id of an actor or enter if it is enough: ')
            if inp_a:
                a = session.query(Actor).get(inp_a)
                if a:
                    fa = FilmActor()
                    fa.id_actor = a.id
                    fa.id_film = f.id
                    session.add(fa)
                    session.commit()
                else:
                    print(f'There is no actor with id {inp_a}')


class FilmActor(BaseTest):
    __tablename__ = 'T_FILMACTOR'
    id_actor = Column('id_actor', ForeignKey(Actor.id))
    id_film = Column('id_film', ForeignKey(Film.id))

    actor = relationship(Actor, back_populates='films')
    film = relationship(Film, back_populates='actors')

    def __str__(self) -> str:
        return f'{self.id} - {self.id_actor} - {self.id_film} '


def load_film_actor() -> list[FilmActor]:
    return session.query(FilmActor).all()
