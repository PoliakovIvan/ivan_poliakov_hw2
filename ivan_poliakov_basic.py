""" Завдання 1. Создать файл (модуль) с примерами всех методов строк."""

list_example: list = ['a', '5', 'a7']
str_example: str = "Something for Example"

# method upper
print(str_example.upper())

# method lower
print(str_example.lower())

# method capitalize
print(str_example.capitalize())

# method title
print(str_example.title())

# method count
print(str_example.count('o'))

# method replace
print(str_example.replace('t', '#', 1))

# method swapcase
print(str_example.swapcase())

# method lstrip
print(str_example.lstrip('S'))

# method rstrip
print(str_example.rstrip('ple'))

# method strip
print(str_example.strip('Something Example'))

# method lstrip
print(str_example.lstrip('S'))

# method split
print(str_example.split(' '))

# method join
print('/'.join(list_example))

""" Завдання 2. Создать по 3 варинта всех уже изученных объектов в Пайтоне."""

# Строки
str1: str = "abs"
str2: str = "567"
str3: str = "abc293"
# Числа
int1: int = 12
float1: float = 14.3
float2: float = 1.0
# Списки
list1: list = ['A', 'B', 'C']
list2: list = [1, 2, 3]
list3: list = ['2a', 3, [3, 'w']]
# Словари
dict1: dict = {'Ukraine': 'Dnipro', 'Poland': 'Warshava'}
dict2: dict = {'32': '30+2', '14': '10+4'}
dict3: dict = {'A1': 'a1', 'B1': 'b1' }
# Кортежи
tuple1: tuple = (1, 2, 3, 4, 5)
tuple2: tuple = ('a', 'abc', '2a')
tuple3: tuple = ('abc', [1, 2, 3], '2a')

""" Завдання 3. Написать 3 примера использования max(), min() """
print(min(list2), max(list2))
print(min(55, 7, 44), max(55, 7, 44))
print(min('x', 't', 'o'))

""" Завдання 5. Написать 3 примера различных с оператором in """
print('A' in 'Abs')
print('123' in '12345678')
print('p' in 'Hello')

""" Завдання 5.Написать 3 примера условия if elif else. """

# Приклад 1
if 1 != 1:
    print('Hi')
elif  2 == 2:
    print('Hello')
else:
    print('Holla')
# Приклад 2
if dict1 == dict1:
    print(dict1)
elif dict1 == dict3:
    print(dict3)
else:
    print(dict2)
# Приклад 3
if list1 == list2:
    print(list2)
elif list1 == list3:
    print(list3)
else:
    print(list1)
