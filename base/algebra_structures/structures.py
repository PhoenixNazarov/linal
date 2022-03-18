from base.algebra_structures.properties import *
from base.algebra_structures.operations import *
from base.algebra_structures.sets import *


class Structure:
    def __init__(self, A: NullSets, U: Operation):
        """
        A - носитель структуры
        U - сигнатура - все операции и отношения

        :param A:
        :param U:
        """
        self.A = A
        self.U = U

    def get_element(self, _type='', element=None):
        if _type == 'neutral':
            return self.U.neutral_element()
        if _type == 'double_sided_inverse':
            if self.U is Mul and (self.A is R):
                return 123
            return self.U.double_sided_inverse_element(element)
        return self.A.element()

    def get_check(self):
        return self.A.check

    def get_operate(self):
        return self.U.operate

    def __repr__(self):
        return f'Структура({self.A.name}, {self.U.name})'


class Algebra(Structure):
    """
    U - только операции
    """


class Model(Structure):
    """
    U - только отношения
    """


class Group(Structure):
    """
    U - бинарная операция
    """
    def check_self(self):
        # 1. U - ассоциативна
        if not check_properties(self, associative):
            return False

        # 2. существует нейтральный элемент. ∀a ∈ G a * e = e * a = a
        if not have_neutral_element(self):
            return False

        # 3. существует двусторонний обратный элемент. ∃-a ∈ G: (-a) * a = a * (-a) =e
        if not have_double_sided_inverse_element(self):
            return False

        return True

    def __repr__(self):
        return f'Структура({self.A.name}, {self.U.name})'


class AbelianGroup(Group):
    def check_self(self):
        # 4. U - коммутативно
        if not check_properties(self, commutative):
            return False
