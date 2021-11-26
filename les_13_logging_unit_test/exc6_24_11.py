from student_v2 import Student, Address


def main():
    adr = Address('Tramesantlei', 100, 2000, 'Schoten')
    student = Student('Student', adr)
    print(student)

if __name__ == '__main__':
    main()