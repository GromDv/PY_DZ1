#     Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
#     Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

n = int(input('Введите число: '))
if n > 0 and n <= 7:
    if n == 6 or n == 7:
        print("Да")
    else:
        print("Нет")
else:
    print("Это не день недели!")