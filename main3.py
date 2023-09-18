# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

user_number = int(input("Введите число N: "))
count = 2
while user_number > count:
    print(count, end=" ")
    count = count * 2
