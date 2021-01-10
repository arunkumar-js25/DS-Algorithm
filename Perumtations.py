#RECURSION
ls = '123'
def permute(ls):
    if len(ls) == 0:
        return []
    if len(ls) == 1:
        return ls

    result = []
    for i in range(0, len(ls)):
        m = ls[i]
        tmp = ls[:i]+ls[i + 1:]
        for v in permute(tmp):
            result.append(m + v)
    return result

print(permute(list(ls)))


#BACKTRACKING 
def permute(a, l, r):
    if l == r:
        print(''.join(a))
    else:
        for i in range(l, r + 1):
            a[l], a[i] = a[i], a[l]
            permute(a, l + 1, r)
            a[l], a[i] = a[i], a[l]  # backtrack

string = "ABC"
n = len(string)
a = list(string)
permute(a, 0, n - 1)


#ITERTOOLS
from itertools import permutations 
print(list(permutations(range(1, 4))))
