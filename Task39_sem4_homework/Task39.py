#Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
my_list = [1, 15, 2, 3, 7, 5, 5, 3, 10]
result_list = []
for i in my_list:
    if my_list.count(i) == 1:
        result_list.append(i)
print(result_list)