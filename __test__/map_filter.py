# 각각의 요소들에 대해 f를 가져다가 씀
def f(x):
    return x**2

# map은 iterate 객체
# it = list(map(lambda x: x*x, [1, 2, 3, 4]))
it = map(lambda x: print(x, end=''), [1, 2, 3, 4])

# it2 = list(map(lambda x: print(x, end=''), [1, 2, 3, 4]))

# print(it2)

# list(map(lambda x: print(x, end=' '), [1, 2, 3, 4]))

# filter
lst = list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4]))
print(lst)

