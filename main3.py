# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

N = int(input("Введите число N: "))
count = 2
while N > count:
    print(count, end=" ")
    count = count * 2
