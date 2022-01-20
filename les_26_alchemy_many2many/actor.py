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




