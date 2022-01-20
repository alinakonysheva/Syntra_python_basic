from sqlalchemy import Column, Integer, String, ForeignKey
from database import session, Base
from sqlalchemy.orm import relationship
from utils import print_title
from inputs import GetInput
from course import Course
from datetime import date
from dateutil.relativedelta import relativedelta


class Student(Base):
    __tablename__ = 'T_STUDENT'

    id = Column('PK_ID', Integer, primary_key=True)
    firstname = Column('F_FIRSTNAME', String(50))
    lastname = Column('F_LASTNAME', String(50))
    course_id = Column('F_COURSE_ID', ForeignKey(Course.id), index=True)
    course = relationship(Course, lazy='subquery', foreign_keys='Student.course_id', back_populates='students')

    def __str__(self) -> str:
        return f'{self.id} - {self.firstname} {self.lastname} - {self.course_id}'


def load_students() -> list[Student]:
    return session.query(Student).all()


def show_all_students(do_print_title=True, students=None):
    if do_print_title:
        print_title('All students')
    if students is None:
        students = load_students()
    for student in students:
        course_id = student.course_id
        course = session.query(Course).get(course_id)
        print(f'{student.firstname} {student.lastname}: his/her courses: {course.name}')

    row_count = len(students)
    if row_count == 0:
        print("no results found")
    else:
        print(f'{row_count} results were found')


def add_student():
    print_title('add student')

    s = Student()

    s.firstname = GetInput.get_text('firstname: ')
    s.lastname = GetInput.get_text('lastname: ')
    s.course_id = GetInput.get_int('course id: ')

    session.add(s)
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


def remove_student():
    print_title('remove a client')
    show_all_students(False)
    id_ = GetInput.get_int('give the ID of a student to delete: ')

    student = session.query(Student).get(id_)
    session.delete(student)
    session.commit()


def modify_student():
    print_title('modify a student')
    show_all_students(False)
    id_ = GetInput.get_int('give the ID of a student to change: ')

    student = session.query(Student).get(id_)
    if student:
        student.firstname = GetInput.get_text('firstname: ')
        student.lastname = GetInput.get_text('lastname: ')
        student.course_id = GetInput.get_int('course ID (number): ')

        session.add(student)
        session.commit()
