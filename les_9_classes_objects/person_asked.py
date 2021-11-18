# Vraag aan de gebruiker zijn voornaam, familienaam en leeftijd.
# Zet dit in een object, druk nadien deze waarden af

class Person:
    '''
    class person
    to create a person
    '''
    first_name = ''
    last_name = ''
    age = 0


def get_input():
    '''
    no arguments
    :return: first_name, last_name, age
    '''
    first_name = input('your first name is >>  ')
    last_name = input('your last name is >>  ')
    age = input('your age is >>  ')
    return first_name, last_name, age


def create_pers():
    '''

    :return: class Person instance
    '''
    guy = Person()
    guy.first_name, guy.last_name, guy.age = get_input()
    return guy


def output(some_person):
    '''
    to return properties of some_person,
    :param some_person:
    :return:  first_name, last_name, age
    '''

    return some_person.first_name, some_person.last_name, some_person.age


def do_run():
    outpt_ = output(create_pers())
    for i in outpt_:
        print(i)


do_run()

