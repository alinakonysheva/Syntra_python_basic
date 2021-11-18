
# Vraag de gebruiker om een paar studenten in te geven.
# Een student kan kiezen uit een paar richtingen : programmeren, bouw, electriciteit.
# Druk dan alle studenten en hun richting af
# 15

class Student:
    '''
    class student
    to create a student
    '''
    first_name = ''
    last_name = ''
    course = ''


def get_input():
    '''
    no arguments
    :return: first_name, last_name, course
    '''
    first_name = input('your first name is >>  ')
    last_name = input('your last name is >>  ')
    while course not in {'programmeren', 'bouw', 'electriciteit'}:
        course = input('you follow the course (programmeren, bouw, electriciteit) >>  ').strip().lower()

    return first_name, last_name, course


def create_srudent():
    '''

    :return: class Student instance
    '''
    student = Student()
    student.first_name, student.last_name, student.course = get_input()
    return student


def output(student):
    '''
    to return properties of student,
    :param student: obj of class Student
    :return:  first_name, last_name, course
    '''

    return student.first_name, student.last_name, student.course


def do_run():
    number_of_students = 2
    list_of_created_students = []
    for i in range(number_of_students):
        student = create_srudent()
        list_of_created_students.append(student)

    for student in list_of_created_students:
        for atr in student:
            print(atr)
        print('-'*10)


do_run()