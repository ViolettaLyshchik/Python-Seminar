#Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
""" my_list = [1, 15, 2, 3, 7, 5, 5, 3, 10]
result_list = []
for i in my_list:
    if my_list.count(i) == 1:
        result_list.append(i)
print(result_list) """


""" def elements(nums):
    nums = [int(i) for i in nums.split()]
    return list(set(nums))

numbers = '1 1 2 2 3 455 66 66 2 1'
print(elements(numbers)) """

my_list= [1, 15, 2, 3, 7, 5, 5, 3, 10]

res = list(filter(lambda x: my_list.count(x)==1, my_list))
#res = [x for x in my_list if my_list.count(x)==1]

print(res)