#Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
#Пример:
#- 6782 -> 23
#- 0,56 -> 11


""" num = input('Введите число: ')
sum = 0
for i in num:
    if i != ',':
        sum += int(i)
print(sum) """
num = input('Введите число: ')
new_sum = sum(map(int, str(num).replace('.', '')))
print(f"Сумма цифр вещественного числа равна = {new_sum}")