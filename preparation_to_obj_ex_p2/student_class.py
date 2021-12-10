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

class Person:

    def __init__(self, first_name: str, last_name: str, third_name: str):
        self.__full_name = f'{first_name} {last_name} {third_name}'
        self.__first_name = first_name
        self.__last_name = last_name
        self.__third_name = third_name

    @property
    def full_name(self):
        return self.__full_name

    @property
    def first_name(self):
        return self.__first_name

    @first_name.setter
    def first_name(self, value):
        self.__first_name = value

    @property
    def last_name(self):
        return self.__last_name

    @last_name.setter
    def last_name(self, value):
        self.__last_name = value

    @property
    def third_name(self):
        return self.__third_name

    @third_name.setter
    def third_name(self, value):
        self.__third_name = value

    def __str__(self):
        return f'{self.__full_name}'


class Student(Person):
    # приписать родителей
    # вписать обратно класс
    # у класса есть предметы а у предмета есть учитель
    def __init__(self, first_name: str, last_name: str, third_name: str):
        """

        :rtype: object
        """
        super(Student, self).__init__(first_name, last_name, third_name)

    def __str__(self):
        return f'{self.full_name}'


student_1 = Student('anna', 'boes', 'olegovna')


class Parent(Person):
    __children = []

    def __init__(self, first_name: str, last_name: str, third_name: str):
        super(Parent, self).__init__(first_name, last_name, third_name)

    @property
    def children(self):
        return self.__children

    @children.setter
    def children(self, value):
        self.__children = value

    def add_child(self, value: Student):
        self.__children.append(value)

    def remove_child(self):
        pass

    def __str__(self):
        return f'{self.full_name} {self.__children}'


class Mother(Parent):
    pass


class Father(Parent):
    pass


m = Mother('Alla', 'Borisovna', 'Poegacheva')
f = Father('Grisha', 'Vasil', 'Vasechkin')
m.add_child(Student)

print(f, m)
