'''Задача 1
С помощью функции input считайте с входящей строки
два целых числа и выведите их сумму, разность, произведение.'''
a = int(input("первое число: "))
b = int(input('второе число:'))
print(a+b)
print(a-b)
print(a*b)

'''Задача 2
Дан ряд целых чисел от 10 до 25 включительно. Используя цикл for, 
выведите на экран сумму двух последовательно идущих чисел.
Пример:

для ряда от 2 до 6 включительно выдача выглядит так:
5
7
9
11
'''

for i in range (10, 26):
    a = 2 * i + 1
    i += 1
    print(a)
'''Задача 3
Для ряда целых чисел от 100 до 150 включительно выведите на экран только те, 
что делятся на 5 без остатка.
'''
for i in range (100, 151):
    if i % 5 == 0:
        print(i)
'''
Задача 4
С помощью функции input считайте с входящей строки целое положительное число и 
сохраните его в переменную N. Используя конструкцию if...else, 
выведите на экран результат в зависимости от условий:

Если N нечетное, то выведите на экран "N нечетное"
Если N четное и входит в интервал от 5 до 10 включительно, выведите на экран "N четное и принадлежит интервалу [5, 10]"
Если N четное и больше 10, выведите на экран "N четное и N > 10"
Если N четное и меньше 5, выведите на экран "N четное и N < 5"
'''
N = int(input("Число: "))
if N % 2 !=0:
  print("N нечетное")
elif 5 < N < 10:
  print("N четное и принадлежит интервалу [5, 10]")
elif N > 10 and N //2:
  print("N четное и N > 10")
elif N // 2 and N < 5:
  print("N четное и N < 5")
'''
Задача 5
Используя цикл while, посчитайте и выведите на экран сумму 
всех целых чисел от 15 до 22
включительно.
'''
x = 15
y = 0
while x <= 22:
  y = y + x
  x = x + 1
print(y)
'''
Задача 6
Используя цикл for, найдите сумму всех элементов заданного списка 
без использования встроенных функций sum, len, sort и т.д.).
'''
my_list = [56, 23, 67, 45, 67, 2, 47, 158, 31, 34, 78, 23, 78, 23, 89, 23, 36]
x = 0
for i in my_list:
  x += i
print(x)
'''
Задача 7
Используя цикл (любой), найдите значение максимального элемента 
списка из предыдущего задания 
(без использования встроенных функций max и т.д.). 
Можно использовать встроенные методы списков (любые).
P.S. Не стесняйтесь гуглить :)
P.S. 2 Гуглить нужно фразу "алгоритм поиска 
максимального элемента массива".
Пример: для списка [3, 4, 1, 7, 2] значением 
максимального элемента является число 7.
'''
my_list = [56, 23, 67, 45, 67, 2, 47, 158, 31, 34, 78, 23, 78, 23, 89, 23, 36]
kh_z = 0
for x in my_list:
  if x > kh_z:
    kh_z = x
print('kh_z равно: ', kh_z)
'''Задача 8
Создайте словарь, соответствующий следующему описанию.

В честь 8 марта начальник отдела Валера решил принести 
на работу коробку конфет и угостить коллег :) 
Красотка Наташа съела две конфеты, ее подруга Алина - целых три, 
разработчик Марат унес с собой в соседний опен-спейс целых пятнадцать, 
чтобы поделиться со своей командой, менеджер проекта Лев проходил мимо и 
съел одну конфету, а сам Валера, будучи сторонником здорового образа жизни, 
не съел ни одной.

P.S. Все совпадения случайны :)'''
подгон_от_Валеры_dictionary = {'Pretty Natasha' : 2, 'Alina' : 3, 'Marat WTF' : 15, 'Lev PM' : 1, 'Valera ЗОЖник' : 0}
print(подгон_от_Валеры_dictionary)
{'Pretty Natasha': 2, 'Alina': 3, 'Marat WTF': 15, 'Lev PM': 1, 'Valera ЗОЖник': 0}
'''Задача 9
Добавьте в словарь из предыдущего задания данные для студента Ромы, 
который работает неполный рабочий день, и, придя на работу после экзамена, 
с удовольствием съел 4 конфеты.
P.S. Используйте встроенный метод .update
'''
подгон_от_Валеры_dictionary.update({'Roma student' : 4})
print(подгон_от_Валеры_dictionary)

# Pro-версия

'''Задача 1
Выведите на экран следующий паттерн:

@

@ @

@ @ @

@ @ @ @ @

Обратите внимание на пробел между символами. 
Рекомендуется использовать циклы (любые) для решения данного задания.
'''
a = '@'
for p in range (1, 6):
  if p != 4:
    print()
    print((a + ' ') * p)

'''Задача 2
Выведите на экран следующий паттерн:

1

2 2

3 3 3

4 4 4 4

5 5 5 5 5

6 6 6 6

7 7 7

8 8

9

Обратите внимание на пробел между символами. 
Обратите внимание на пробел между символами. 
Рекомендуется использовать циклы (любые) для решения данного задания.
'''
for i in range(1, 10):
  if i < 6:
    print((str(i) + ' ')*i)
  else:
    print((str(i) + ' ')*(10 - i))
  print()

'''Задача 3
Используя цикл while, выведите на экран таблицу умножения для числа 7.

Пример:

Для числе 5 выдача выглядит так:

5 * 1 = 5

5 * 2 = 10

5 * 3 = 15

5 * 4 = 20

5 * 5 = 25

...

5 * 9 = 45
'''
X = 7
i = 0
while i in range(0, 10):
  i += 1
  print(X, '*', i, '=', X*i)
  print()

'''
Задача 4
Представьте, что вы подбрасываете два кубика одновременно. 
Считайте с входящей строки два целых числа d1 и d2. 
Проверьте, соответсуют ли введенные числа интервалу значений для кубика.
Если нет, то выведите на экран строку 
"Ошибка! Значение на кубике (1 или 2, вставьте подходящее значение) 
не входит в интервал [1, 6]". В противном случае посчитайте сумму выпавших значений. 
Если сумма равна 7 или 11, выведите на экран "Я победил!!!". 
Если сумма равна 2, 3 или 12, то выведите на экран "Я проиграл :(". 
Во всех остальных случаях выведите на экран сумму значений.
'''
d1 = int(input('Значение кубика № 1: '))
d2 = int(input('Значение кубика № 2: '))
if d1 < 1 or d1 > 6:
  print('Ошибка! Значение на кубике №1 не входит в интервал [1, 6]')
if d2 < 1 or d2 > 6:
  print('Ошибка! Значение на кубике №2 не входит в интервал [1, 6]')
else:
  if d1 + d2 ==7 or d1 + d2 == 11:
    print('Я победил!!!')
  elif d1 + d2 ==2 or d1 + d2 == 3 or d1 + d2 == 12:
   print('Я проиграл :(')
  else:
    print('Сумма выпавших значений', d1 + d2)

'''
Задача 5
Напишите код, который ищет все числа в интервале от 3000 до 4300 включительно, 
делящиеся на 11, но не делящиеся на 5. Выведите на экран все найденные числа.
'''
for q in range(3000, 4301):
  if q % 11 == 0 and q % 5 !=0:
    print(q)

'''Задача 6
Используя циклы, напишите код, который создает список (list) 
путем конкатенации значений данного листа с целыми числами от 1 до (произвольного) 
n включительно.

Пример:

для списка ["сосиски", "горчица"] при n = 3 результат должен выглядеть так:

['сосиски$\_$1', 'горчица$\_$1', 'сосиски$\_2$', 'горчица$\_$2', 'сосиски$\_$3', 'горчица$\_$3']
'''
sample_list = ["мандаринки", "киви", "лимон"]
n = int(input('Введите число '))
my_list = []
a = 1
while a <= n:
  for i in sample_list:
    my_list.append(str(i + '_' + str(a)))
  a += 1
print(my_list)

'''
Задача 7
Напишите код, который считает количество элементов 
в заданном списке до тех пор, пока не встретится элемент типа словарь.

Пример:

для списка [3, "котики", 0.45, 5, {'котики' : 2, 'слоники' : 9}, "слоники", 34] на выходе должны получить число 4
'''
list_for_pro_task_2 = [35, 0.24, 3 + 4j, "котики", 0.45, (8, 9), "слоники", {"Мадрид": 3, 'Лондон':5}, 23498]
print(list_for_pro_task_2)
i = 0
while type(list_for_pro_task_2[i]) != dict:
   i += 1
print(i)

'''Задача 8
Создайте словарь (dict) c ключами, 
соответствующими числам от 1 до 20 включительно и значениями, 
соответствующими квадратам ключей.
P.S. Используйте циклы или функции, прямое "ручное" присваивание не допускается (!!!)
Пример:
для чисел от 1 до 3 включительно словарь должен выглядеть так: {1 : 1, 2 : 4, 3 : 9}
'''
my_dict = {}
for i in range (1, 21):
  my_dict.update({i : i ** 2})
print(my_dict)
