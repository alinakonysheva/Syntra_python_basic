from inputs import GetInput
from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship
from database import session, BaseTest
from film import Film
from actor import Actor
from utils import print_title


# We gaan acteurs en films bijhouden. Leg een link tussen beide.
# Maak een overzicht van films en acteurs, zoekmogelijheden op jaar,
# naam, score. Maar ook gebruik van een base klasse.

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


def add_actors_to_film():
    inp_f = GetInput.get_int('id of a film')
    inp_a = True
    f = session.query(Film).get(inp_f)
    if f:
        while inp_a != '':
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
