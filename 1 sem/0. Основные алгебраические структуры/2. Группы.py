from base.algebra_structures.operations import Add, Mul
from base.algebra_structures.sets import R, Z, Q
from base.algebra_structures import structures
from base.algebra_structures.properties import *

struct = structures.Structure


# множество G называется группой
# 1. * - ассоциативна
# 2. существует нейтральный элемент. ∀a ∈ G a * e = e * a = a
# 3. существует двусторонний обратный элемент. ∃-a ∈ G: (-a) * a = a * (-a) =e
# множество G называют абелевой группой
# 4. * - коммуникативна
def check_on_abel_group(structure):
    if not check_properties(structure, associative):
        return -1, 'не ассоциативна'
    if not have_neutral_element(structure):
        return -1, 'не имеет нейтрального элемента'
    if not have_double_sided_inverse_element(structure):
        return -1, 'не имеет двойного обратного элемента'
    if not check_properties(structure, commutative):
        return 1, 'группа, не коммунитативно'
    return 0, 'абелева группа'


def pod_check(structure, out):
    if check_on_abel_group(structure)[0] != out:
        print(f'Ошибка {structure} - {check_on_abel_group(structure)[1]}')
        raise Exception
    print(f'{structure} - {check_on_abel_group(structure)[1]}')


# (Z, +) абелева группа
pod_check(struct(Z, Add), 0)

# (Z, *) не группа
pod_check(struct(Z, Mul), -1)

# (R, +) абелева группа
pod_check(struct(R, Add), 0)

# (R, +) не группа
pod_check(struct(R, Mul), -1)
print()

# множество K, с двумя бинарными операциями, называется кольцом:
K = struct(R, Add)
K2 = struct(R, Mul)
# 1. (K, +) - абелева группа
if check_on_abel_group(K)[0] != 0: raise ''

# 2
# a, b, c ∈ K a · (b + c) = (a · b) + (a · c)
# a, b, c ∈ K (a + b) · c = (a · c) + (b · c)
if not check_properties(K, distributivity, operate = (K.get_operate(), K2.get_operate())):
    raise ""
print(f'{K}+{K2} - кольцо')

# множество K, с двумя бинарными операциями, называется полем:
# 1. (K, +) - абелева группа
if check_on_abel_group(K)[0] != 0: raise ''

# 2. (K, *) - абелева группа
if check_on_abel_group(K2)[0] != -1:
    print(f'{K2} не абелевна группа')

# 3. Дистрибутивность умножения относительно сложения:  (a+b)*c = (a*с) + (b*c)
if not check_properties(K, distributivity, operate = (K.get_operate(), K2.get_operate())):
    print('нет дистрибутивности')

# примеры:
# Z - кольцо, но не полу
K = struct(Z, Add)
K2 = struct(Z, Mul)

if not check_properties(K, distributivity, operate = (K.get_operate(), K2.get_operate())):
    raise ""
else:
    print(f'{K}+{K2} - кольцо')

if check_on_abel_group(K2)[0] != 0:
    print(f'{K}+{K2} - не кольцо')

if check_on_abel_group(K2)[0] != 0:
    print(f'{K}+{K2} - не кольцо')

if not check_properties(K, distributivity, operate = (K.get_operate(), K2.get_operate())):
    print(f'{K}+{K2} - не кольцо')

# (Q, +, *) группа
K = struct(Q, Add)
K2 = struct(Q, Mul)

if not check_properties(K, distributivity, operate = (K.get_operate(), K2.get_operate())):
    raise ""
else:
    print(f'{K}+{K2} - кольцо')

if check_on_abel_group(K2)[0] != 0:
    raise ""

if check_on_abel_group(K2)[0] != 0:
    raise ""

if not check_properties(K, distributivity, operate = (K.get_operate(), K2.get_operate())):
    raise ""
else:
    print(f'{K}+{K2} - группа')

# (R, +, *) группа
K = struct(R, Add)
K2 = struct(R, Mul)

if not check_properties(K, distributivity, operate = (K.get_operate(), K2.get_operate())):
    raise ""
else:
    print(f'{K}+{K2} - кольцо')

if check_on_abel_group(K2)[0] != 0:
    raise ""

if check_on_abel_group(K2)[0] != 0:
    raise ""

if not check_properties(K, distributivity, operate = (K.get_operate(), K2.get_operate())):
    raise ""
else:
    print(f'{K}+{K2} - группа')