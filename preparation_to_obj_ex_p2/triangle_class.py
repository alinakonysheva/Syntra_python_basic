# # Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# # Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.
#


class Triangle:
    def __init__(self, a: tuple, b: tuple, c: tuple):
        self._a = a
        self._b = b
        self._c = c
        self._first_side, self._second_side, self._third_side = self.lengths

    @property
    def lengths(self):
        first_side = ((self._a[0] - self._b[0]) ** 2 + (self._a[1] - self._b[1]) ** 2) ** 0.5
        second_side = ((self._c[0] - self._b[0]) ** 2 + (self._c[1] - self._b[1]) ** 2) ** 0.5
        third_side = ((self._a[0] - self._c[0]) ** 2 + (self._a[1] - self._c[1]) ** 2) ** 0.5
        return first_side, second_side, third_side

    @property
    def square(self):
        s = 0
        try:
            s = 0.5 * abs((((self._a[0] - self._c[0]) * (self._b[1] - self._c[1])) - (
                    (self._b[0] - self._c[0]) * (self._a[1] - self._c[1]))))

            if s > 0:
                return s
            else:
                print('coordinates are not correct, there is no triangle')
                raise ValueError
        except Exception as e:
            print('that have to be numbers', e)
            raise ValueError

    @property
    def perimeter(self):
        return self._first_side + self._second_side + self._third_side


t = Triangle((-3, 0), (0, 0), (0, 5))
print(t.square)
print(t.perimeter)
