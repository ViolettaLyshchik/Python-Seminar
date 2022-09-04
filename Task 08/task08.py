#Напишите программу, которая принимает на вход координаты точки (X и Y), 
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
#    Пример:
#- x=34; y=-30 -> 4
#- x=2; y=4-> 1
#- x=-34; y=-30 -> 3
x, y = int(input('Введите координату x: ')), int(input('Введите координату y: '))
if x > 0 and y > 0:
    print('Точка в 1-ой четверти координатной плоскости')
elif x < 0 and y > 0:
    print('Точка во 2-ой четверти координатной плоскости')
elif x < 0 and y < 0:
    print('Точка в 3-ей четверти координатной плоскости')
elif x > 0 and y < 0:
    print('Точка в 4-ой четверти координатной плоскости')
else:
    print('Неверно введены данные. X ≠ 0 и Y ≠ 0')