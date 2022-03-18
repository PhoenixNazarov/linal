from base.algebra_structures.operations import Add, Sub, Mul
from base.algebra_structures.sets import Z
from base.algebra_structures import structures
from base.algebra_structures.properties import *

struct = structures.Structure

# проверка бинарных функций на множестве Z
bin_func = [struct(Z, Add), struct(Z, Sub), struct(Z, Mul)]  #
for i in bin_func:
    print(f'{i} коммуникативно: {check_properties(i, commutative)}')
    print(f'{i} ассоциативно: {check_properties(i, associative)}')

# проверка (Z, *) имеет обратный элемент
print(f'{struct(Z, Mul)} имеет обратный элемент: {have_double_sided_inverse_element(struct(Z, Mul))}')


