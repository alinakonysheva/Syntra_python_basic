# Maak een object student, geef deze een naam en adres, vraag de naam en het volledige adres en druk deze af

class Student:
    '''
    class student
    to create a student
    '''
    first_name = ''
    last_name = ''
    address = ''


def get_input():
    '''
    no arguments
    :return: first_name, last_name, course
    '''
    first_name = input('your first name is >>  ')
    last_name = input('your last name is >>  ')
    address = input('your address >>  ')

    return first_name, last_name, address


def create_srudent():
    '''

    :return: class Student instance
    '''
    student = Student()
    student.first_name, student.last_name, student.address = get_input()
    return student


def output(student):
    '''
    to return properties of student,
    :param student: obj of class Student
    :return:  first_name, last_name, adress
    '''

    print(f'full name: {student.first_name} {student.last_name}, address: {student.address}')


def do_run():
    student = create_srudent()
    output(student)
