'''Задача 1 на 10 балов'''

print('TASK 1')

age = input('Hi! Fill up your year of birth?')

if age.isnumeric():
    age = int(age)
    age = 2022 - age
    print('You are ',age, 'Y.O!')
    if age == 21:
        print("You should visit Holland")
    elif age > 21:
        print("You should visit Vietnam")
    else:
        print("Travell everywhere")
else:
    print('Please, write a number')

'''Задача 2 на 25 балов'''

print('TASK 2')

print("Hi, user!")
name: str = input("What is your name?")
gender: str = input("Your gender? M/Ж")
age_user = input("How old are you?")
age_user = int(age_user)
if name == 'admin':
    print("Привет, повелитель!")
if name == 'Женя':
    print('Советую Вам посмотреть "TENET"')
elif age_user > 10 and age_user < 14 and gender == 'М':
    print('Советую Вам посмотреть "StarWars"')
elif age_user > 30 and gender == 'М':
    print('Советую Вам посмотреть "Мандалорец"')
elif age_user > 22 and age_user < 32 and gender == 'Ж':
    print('"Советую Вам посмотреть "Трансформеры""')
elif age_user < 16 and gender == 'Ж':
    print('Советую Вам посмотреть "Инсургент"')
elif age_user < 11 and gender == 'М':
    print('Советую Вам посмотреть "TMNT"')
if name == 'Guido':
    print('Огромное спасибо!')

'''Задача 3 на 10 балов'''

print('TASK 3')

x = list ('(etnfづzxfk｡12dt◕`1ad‿6hns‿1zQY◕Cd$y｡FtSq)Ze6?づ#2)$')
print(x [5:-1:5])

'''Задача 4 на 25 балов '''

print('TASK 4')

days, hours = input("Введите дни и часы: ").split(", ")
days = float(days)
hours = float(hours)
sol = (days + hours / 24) * 1.02595675
sol = round(sol, 2)
print(f'Количество солов: {sol}')


'''Задача 5 на 25 балов '''

print('TASK 5')

damn: str = 'черт его возьми, черт его знает, Чертополох, иди к черту, черт ногу сломит, Чертеж здания в разрезе'
print(damn.replace('черт ', '#### '))

