class Operation:
    name = 'операция'

    @staticmethod
    def operate(a, b):
        raise

    @staticmethod
    def neutral_element():
        raise

    @staticmethod
    def double_sided_inverse_element(a):
        raise

    def __repr__(self):
        return self.name


class BinOperate(Operation):
    name = 'бинарная операция'


class Add(BinOperate):
    name = '+'

    @staticmethod
    def operate(a, b):
        return round(a + b, 5)

    @staticmethod
    def neutral_element():
        return 0

    @staticmethod
    def double_sided_inverse_element(a):
        return -a

    def __repr__(self):
        return self.name


class Sub(BinOperate):
    name = '-'

    @staticmethod
    def operate(a, b):
        return round(a - b, 5)

    @staticmethod
    def neutral_element():
        return 0

    @staticmethod
    def double_sided_inverse_element(a):
        return -a

    def __repr__(self):
        return self.name


class Mul(BinOperate):
    name = '*'

    @staticmethod
    def operate(a, b):
        return round(a * b, 5)

    @staticmethod
    def neutral_element():
        return 1

    @staticmethod
    def double_sided_inverse_element(a):
        return 1 / a

    def __repr__(self):
        return self.name


class Div(BinOperate):
    name = '/'

    @staticmethod
    def operate(a, b):
        return round(a / b, 5)

    @staticmethod
    def neutral_element():
        return 1

    @staticmethod
    def double_sided_inverse_element(a):
        return 1 / a

    def __repr__(self):
        return self.name
