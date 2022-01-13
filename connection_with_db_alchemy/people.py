

from sqlalchemy import Column, Integer, String
from database import session, Base
from utils import print_title
from inputs import get_input_item


class People(Base):
   __tablename__ = 'T_PEOPLE'
   
   id = Column('PK_ID', Integer, primary_key=True)
   firstname = Column('F_FIRSTNAME', String(50))
   lastname = Column('F_LASTNAME', String(50))
   age = Column('F_AGE', Integer)
   sexe = Column('F_SEXE', Integer)
   place = Column('F_PLACE', String(50))

   def __str__(self) -> str:
       return '{} - {} {} - {} - {}'.format(self.id, self.firstname, self.lastname, self.age, self.place)


def load_people(): 
   return session.query(People).all()


def show_all(do_print_title=True):
   if do_print_title:
      print_title('show all peopple')
   peoples = load_people()
   for people in peoples:
      print('{}'.format(people))



def show_with_filter():
   print_title('filter')
   peoples = None

   print('1. Alle mannen')
   print('2. Alle vrouwen')
   print('3. met minimumleeftijd')
   print('4. plaats')

   filtertype = get_input_item('Geef uw keuze: ', 1)
   if filtertype == 1:
      peoples = session.query(People).filter(People.sexe == 1).all()
   elif filtertype == 2:
      peoples = session.query(People).filter(People.sexe == 2).all()
   elif filtertype == 3:
      age_min = get_input_item('welk is de minimumleeftijd : ', 1)
      peoples = session.query(People).filter(People.age > age_min).all()
   elif filtertype == 4:
      pplace = get_input_item('place: ')
      peoples = session.query(People).filter(People.place == pplace).all()
      
   else:
      print('geen gelding type geselecteerd')

   for people in peoples:
      print('{}'.format(people))


def add_people():
   print_title('add a person')

   people = People()
   people.firstname = get_input_item('firstname: ')
   people.lastname = get_input_item('lastname: ')
   people.age = get_input_item('age: ', 1)
   people.sexe = get_input_item('sexe: ', 1)
   people.place = get_input_item('place: ')

   session.add(people)
   session.commit()


def remove_people():
   print_title('remove a person')
   show_all(False)
   id = get_input_item('geef het nummer van de persoon die u wilt wissen: ')

   people = session.query(People).get(id)
   session.delete(people)
   session.commit()


def modify_people():
   print_title('modify a person')
   show_all(False)
   id = get_input_item('geef het nummer van de persoon die u wilt wijzigen: ')

   people = session.query(People).get(id)
   if people is not None:
      people.firstname = get_input_item('new firstname: ')
      people.lastname = get_input_item('new lastname: ')
      people.age = get_input_item('new age: ', 1)
      people.sexe = get_input_item('new sexe: ', 1)
      people.place = get_input_item('new place: ')

      session.add(people)
      session.commit()
