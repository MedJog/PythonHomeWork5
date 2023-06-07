# Задача 28: Напишите рекурсивную функцию sum(a, b), 
# возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. 
# Также нельзя использовать циклы.
# *Пример:*
#2 2
# 4 
def summa(number1, number2):
    if number1 == 0:
        return number2
    if number2 == 0:
        return number1
    return (summa(number1 - 1, number2 + 1))

num1 = int(input('Введите число: '))
num2 = int(input('Введите число: '))
print(f'Сумма числел {num1} и {num2} равна {summa(num1, num2)}')



