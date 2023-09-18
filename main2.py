# # Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике.
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать.
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.

import math

user_summ = int(input("Введите сумму чисел: "))
user_mult = int(input("Введите произведение чисел: "))
discriminant = user_summ * user_summ - 4 * user_mult
if discriminant < 0:
    first_number = user_summ / 2
else:
    first_number = (user_summ + (math.sqrt(discriminant))) / 2
second_number = user_summ - first_number
print(f"Первое число {first_number}, второе число {second_number}")
