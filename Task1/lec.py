#1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
#Пример:
# 6 -> да
# 7 -> да
# 1 -> нет

day = int(input('Put any number: '))
if day > 7 or day < 1:
    print('Repeat the input')
elif day == 6 or day == 7:
    print("Yes")
else:
     print("No, it's not weekend")