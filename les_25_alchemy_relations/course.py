from sqlalchemy import Column, Integer, String, Date, Boolean
from database import session, Base
from utils import print_title
from inputs import GetInput
from sqlalchemy.orm import relationship

from datetime import date
from dateutil.relativedelta import relativedelta


# Studenten volgen een cursus. Elke student kan zich inschrijven voor 1 cursus.
# Toon welke studenten een bepaalde cursus volgen. Geef ook een overzicht van alle studenten en voorzie zoek mogelijkheden op student en cursus

class Course(Base):
    __tablename__ = 'T_COURSE'

    id = Column('PK_ID', Integer, primary_key=True)
    name = Column('F_NAME', String(50))
    students = relationship('Student', back_populates='course')

    def __str__(self) -> str:
        return f'{self.id} - {self.name}'


def load_courses() -> list[Course]:
    return session.query(Course).all()


def show_all_courses(do_print_title=True, courses=None):
    if do_print_title:
        print_title('All courses')
    if courses is None:
        courses = load_courses()
    for course in courses:
        print(f'{course}')

    row_count = len(courses)
    if row_count == 0:
        print("no results found")
    else:
        print(f'{row_count} results were found')


def add_course():
    print_title('add course')

    c = Course()

    c.name = GetInput.get_text('name: ')
    session.add(c)
    session.commit()


def show_with_filter():
    pass
    """print_title('Filter')
    clients = None

    print('1 Find a client via name')
    print('2 Find a company via vat')
    print('3 Find a company via name')
    print('4 Find clients who more the ... years clients are')
    print('5 Find clients whose age is more than ... years')

    filter_type = GetInput.get_int('your choice ')
    if filter_type == 1:
        search = f"%{GetInput.get_text('name of a client: ')}%"
        clients = session.query(Client).filter((Client.firstname.like(search)) | (Client.lastname.like(search))).all()
    elif filter_type == 2:
        search = GetInput.get_text('vat of a client: ').strip()
        clients = session.query(Client).filter(Client.company_btw == search).all()
    elif filter_type == 3:
        search = f"%{GetInput.get_text('company name: ')}%"
        clients = session.query(Client).filter(Client.company_name.like(search)).all()
    elif filter_type == 4:
        years_number = GetInput.get_int('How many (minimum) years client with us? ')
        min_date = date.today() - relativedelta(years=years_number)
        clients = session.query(Client).filter(Client.start_date <= min_date).order_by(Client.firstname.asc(),
                                                                                       Client.lastname.asc()).all()
    elif filter_type == 5:
        years_number = GetInput.get_int('How old should be the client (minimum age)? ')
        max_date_birth = date.today() - relativedelta(years=years_number)
        clients = session.query(Client).filter(Client.cursus <= max_date_birth).order_by(Client.firstname.asc(),
                                                                                         Client.lastname.asc()).all()
    else:
        print('there is not a right choice')

    for client in clients:
        print(f'{client}')
"""
    """
    ?: как сделать из это метод класса, а не метод экземляра класса
    elif filter_type == 5:
        min_number_years_as_client = f"%{GetInput.get_int('minimum number of years together: ')}%"
        clients = session.query(Client).filter(Client.years_together() >= min_number_years_as_client).all()
    """


def remove_course():
    print_title('remove a client')
    show_all_courses(False)
    id_ = GetInput.get_int('give the ID of a course to delete: ')

    course = session.query(Course).get(id_)
    session.delete(course)
    session.commit()


def modify_course():
    print_title('modify a course')
    show_all_courses(False)
    id_ = GetInput.get_int('give the ID of a course to change: ')

    course = session.query(Course).get(id_)
    if course:
        course.name = GetInput.get_text('name: ')
        session.add(course)
        session.commit()
