# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать
# в неограниченном кол-ве классов свой определенный предмет.
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе

from student_class import Person


class Teacher(Person):
    __class_number_teaching = []
    __subject = ''

    def __init__(self, first_name: str, last_name: str, third_name: str, subject: str):
        """

        :rtype: object
        """
        super(Teacher, self).__init__(first_name, last_name, third_name)
        self.__subject = subject

    @property
    def class_number_teaching(self):
        return self.__class_number_teaching

    @class_number_teaching.setter
    def class_number_teaching(self, value):
        self.__class_number_teaching = value

    @property
    def subject(self):
        return self.__subject

    @subject.setter
    def subject(self, value):
        self.__subject = value

    def __add__(self, other):
        self.__class_number_teaching.append(other)

    def add_class_number_teaching(self, value):
        """
        to add stuffing in a bun (of Bun)
        :param value: type: Stuffing
        """
        self.__class_number_teaching.append(value)

    def add_subject(self, value):
        self.__subject = value

    def __str__(self):
        return f'{self.full_name} {self.__class_number_teaching} {self.__subject}'


t = Teacher('Maria', 'Petrenko', 'Ivanovna', 'math')

print(t)
t + '5b'
print(t)

t + '6b'
print(t)
