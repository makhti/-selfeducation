'''
Оператор            Проверяемое условие
    ==             Равенство
    !=             Неравенство
    >              Больше
    <              Меньше
    >=             Больше либо равно
    <=             Меньше либо равно
 '''
# Пять переменных для сравнения
nil = 0
num = 0
max = 1
cap = 'A'
low = 'a'
# Добавляем инструкцию для вывода результатов числового и символьного сравнения с помощью оператора равенства.
print('Equality :\t' , nil , '==' , num , nil == num )
print('Equality :\t' , cap , '==' , low , cap == low )
# Добавляем инструкцию для вывода результата с помощью оператора неравенства.
print('Inequality :\t' , nil , '!=' , max , nil != max )
# Добавляем инструкцию для вывода результата с помощью оператора больще и меньше.
print('Greater :\t' , nil , '>' , max , nil > max )
print('Lesser :\t' , nil , '<' , max , nil < max )
# Добавляем инструкцию для вывода результата с помощью оператора больще либо равно  или меньше либо равно.
print('More ore Equal :\t' , nil , '>=' , num , nil >= num )
print('Less ore Equal :\t' , max , '=<' , num , max <= num )