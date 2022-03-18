"""
Линейная комбинация -
Тривиальная комбинация - все нули
Система векторов линейно независима - 0 можно выразить только через тривиальную комбинацию

Элементарные преобразования -
+- 0
смена векторов местами
* != 0
Ai = Ai+1 + Ai


rank:
1. rank A = rank At
2. rank aA = a * rank A
3. rank A+B = rankA + rankB
4. rank AB = min(rankA, rankB)
5. rank не меняется при элементарных преобразованиях


"""
a = [
    [1, 2, 1],
    [1, 1, 0],
    [3, 2, 1]
]

for i in range(len(a)):
    for ii in range(len(a)):
        if a[i][ii] == 0:
            continue
        else:
            for i3 in range(len(a)):
                if i3 == i or a[i3][ii] == 0:
                    continue
                mn = a[i3][ii] / a[i][ii]
                for i4 in range(len(a)):
                    a[i3][i4] -= a[i][i4] * mn
            break
    else:
        raise Exception
