import random
import math


class NullSets:
    name = 'нулевое множество'

    @staticmethod
    def element():
        return None

    @staticmethod
    def check(a):
        return a is None

    def __repr__(self):
        return self.name


class Numbers(NullSets):
    name = 'нулевое множество чисел'

    @staticmethod
    def check(a):
        return type(a) not in [int, float]

    def __repr__(self):
        return self.name


class N(Numbers):
    name = 'N'

    @staticmethod
    def element():
        return random.randint(1, 100)

    @staticmethod
    def check(a):
        return a == int(a) and a > 0

    def __repr__(self):
        return self.name


class Z(N):
    name = 'Z'

    @staticmethod
    def element():
        return random.randint(-100, 100)

    @staticmethod
    def check(a):
        return a == int(a)

    def __repr__(self):
        return self.name


class Q(Z):
    name = 'Q'

    @staticmethod
    def element():
        return round(random.randint(-100, 100) / random.randint(1, 100), 3)

    @staticmethod
    def check(a):
        return a == float(a)

    def __repr__(self):
        return self.name


class R(Q):
    name = 'R'

    @staticmethod
    def element():
        return round(random.randint(-100, 100) / random.randint(1, 100), 3)

    @staticmethod
    def check(a):
        return type(a) in [int, float]

    def __repr__(self):
        return self.name


class C(R):
    name = 'C'

    @staticmethod
    def element():
        return complex(random.randint(-100, 100), random.randint(-100, 100))

    @staticmethod
    def check(a):
        return type(a) == complex

    def __repr__(self):
        return self.name


class V:
    def __init__(self, size):
        self.v = [random.randint(1, 10) for i in range(size)]

    def __mul__(self, other):


class Vec:
    name = 'Вектор'

    @staticmethod
    def element():
        return random.randint(1, 10), random.randint(1, 10), random.randint(1, 10)

    @staticmethod
    def check(a):
        return type(a) == tuple

    def __repr__(self):
        return self.name
