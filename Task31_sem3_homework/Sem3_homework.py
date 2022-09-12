#Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
#- для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] 


n = int(input('Введите число: '))
neg_fib = [1,-1]
fib = [1,1]
for i in range(2,n):
    list = fib[i-1]+fib[i-2]
    fib.append(list)
    list_neg = neg_fib[i-2] - neg_fib[i-1]
    neg_fib.append(list_neg)
neg_fib.reverse()
neg_fib.append(0)

print(f'Список чисел Фибоначчи: {neg_fib+fib}')