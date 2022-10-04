
# Типы данных перменных
'''
M = [1, 2.3, '4', True, 1+3j, 3+4, 7/2, '5'*3, 1<10,  1+3j + 3-5j]
for i in M:
    print(i, type(i))
'''


'''
print()
# Натуральные < Целые числа < Рациональные < Иррациональные < Вещественные < Комплексные числа

# Типы данных коллекций
A = [[1, 2, 3], (1, 2, 3), {1, 2, 3}, {1: 'один', 2: "два", 3: "три"}]
for i in A:
    print(i, type(i))
'''


# Можно менять типы данных
'''
print()

x = 5
print(x, type(x))

x = str(x)
print(x, type(x))

x = float(x)
print(x, type(x))

x = int(x)
print(x, type(x))
# Из int и float легко переводить в другие типы данных
# А из str можно переводить, если строка состоит только лишь из цифр

print()

M = [1, 2, 3]
print(M, type(M))

M = tuple(M)
print(M, type(M))

M = set(M)
print(M, type(M))

M = list(M)
print(M, type(M))
'''


""" 
TuesdayStudents = {1949653479: 'Yanina.py', 1891281816: 'ilandroxy', 438879394: 'ilandroxxy', -726393257: "Homework", -647660626: "Lessons"}

'''
for key in TuesdayStudents.keys():  # бежим по ключам
    print(key)

for key in TuesdayStudents.values():  # бежим по значениям 
    print(key)

for key in TuesdayStudents.items():   # бежим по всем записям
    print(key)
    
for key in TuesdayStudents:  # бежим по ключам
    print(key)
'''

for key in TuesdayStudents:
    if key == 1949653479:
        print(f'Привет! {TuesdayStudents[key]}')
"""



TuesdayStudents = {1949653479: ['Yanina.py', '10:00', 4080//8]}

for key in TuesdayStudents:
    print(f'Имя файла: {TuesdayStudents[key][0]}\nВремя урока: {TuesdayStudents[key][1]}\nТип абонемента: {TuesdayStudents[key][2]}')