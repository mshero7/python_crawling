import os

test = set()

print(test.add('1'))
print(test.add('1'))

print(test.add(('1', '2')))
print(test.add(('1', '2')))
print(test)

for item in test:
    print(item)

tol = ( ['a','b'], ['c','d'])
dict1 = dict(tol)
print(dict1)

dict2 = {'a':'워어어', 'e':'f'}

print(dict1)
########################################################################################

drinks = {
    'martini' : {'vodka', 'vermouth'},
    'black russian' : {'vodka', 'kahlua'},
    'white russian' : {'cream', 'kahlua', 'vodka'},
    'manhanttan' : {'rye', 'vermouth', 'bitters'},
    'screwdriver' : {'orange juice', 'vodka'}
}

# 보드카가 포함된 음료

for key, val in drinks.items():
    if 'vodka' in val:
        print(key, val)

# 보드카가 들어있고 베르무트가 빠진 음료
print('# 보드카가 들어있고 베르무트가 빠진 음료')
for key, val in drinks.items():
    if 'vodka' in val and not ('vermouth' in val):
        print(key, val)

# 오렌지 주스 혹은 베르무트가 들어 있는 음료
print('# 오렌지 주스 혹은 베르무트가 들어 있는 음료')
for key, val in drinks.items():
    if val & {'vermouth', 'orange juice'}:
        print(key, val)

print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))