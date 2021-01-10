#RECURSION
def combine(lst, n):
    if n == 0:
        return [[]]

    l = []
    for i in range(0, len(lst)):

        m = lst[i]
        remLst = lst[i + 1:]

        for p in combine(remLst, n - 1):
            l.append([m] + p)

    return l

arr ="abc"
for x in range(1,len(arr)+1):
    print(combine(list(arr), x))
    
        
#ITERTOOLS
import itertools

arr = list('abc')
n = 2
print(list(itertools.combinations(arr, n)))
print(list(itertools.combinations_with_replacement(arr, 2)))


#GENERATOR - ITERATIONS
def combine(iterable, r):
    char = tuple(iterable)
    n = len(char)

    if r > n:
        return

    index = [x for x in range(r)]
    yield tuple(char[i] for i in index) # retruns the first sequence

    while True:

        for i in reversed(range(r)):
            if index[i] != i + n - r:
                break
        else:
            return

        index[i] += 1
        for j in range(i + 1, r):
            index[j] = index[j - 1] + 1

        yield tuple(char[i] for i in index)

print([x for x in combine("abc", 2)])
