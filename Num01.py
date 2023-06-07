# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, 
# и возводит число А в целую степень B с помощью рекурсии.
# *Пример:*
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8 

def power(number, extent):
    if number == 0 or extent == 0 or number == 1:
        return 1
    if extent == 1:
        return number
    return (number * (power(number, extent - 1)))

num = int(input('Введите число: '))
ext = int(input('Введите значеие степени: '))
print(f' {num} в степени {ext} равно {power(num, ext)}.')