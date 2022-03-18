
# a * b = b * a
def commutative(operate, element, check):
    a = element()
    b = element()

    c1 = operate(a, b)
    c2 = operate(b, a)
    return ans_prop(check, c1, c2)


# (a * b) * c == a * (b * c)
def associative(operate, element, check):
    a = element()
    b = element()
    c = element()

    c1 = operate(operate(a, b), c)
    c2 = operate(a, operate(b, c))

    return ans_prop(check, c1, c2)


# (a + b) * c = (a * с) + (b * c)
def distributivity(operate, element, check):
    operate_add, operate_mul = operate
    a = element()
    b = element()
    c = element()

    c1 = operate_mul(operate_add(a, b), c)
    c2 = operate_add(operate_mul(a, c), operate_mul(b, c))

    return ans_prop(check, c1, c2)


def ans_prop(check, c1, c2):
    if not (check(c1) and check(c2)):
        return False
    return abs(c1 - c2) < 0.001


# a * e = e * a = a
def have_neutral_element(structure):
    e = structure.get_element('neutral')
    for i in range(100):
        a = structure.get_element()
        operate = structure.get_operate()
        if not structure.get_check()(e):
            return False
        if not operate(a, e) == operate(e, a) == a:
            return False
    return True


# ∃-a ∈ G: (-a) * a = a * (-a) = e
def have_double_sided_inverse_element(structure):
    e = structure.get_element('neutral')
    a = structure.get_element()
    _a = structure.get_element('double_sided_inverse', element = a)
    if not (structure.get_check()(e) and structure.get_check()(_a)):
        return False
    operate = structure.get_operate()
    return operate(_a, a) == operate(_a, a) == e


def check_properties(structure, _property, operate=None):
    if operate is None:
        operate = structure.get_operate()
    for i in range(1000):
        if not _property(operate, structure.get_element, structure.get_check()):
            return False
    return True



