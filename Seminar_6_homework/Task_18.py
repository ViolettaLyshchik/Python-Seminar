#Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму
n = int(input("Введите число n: "))
""" sum = 0
for i in range(1,n+1):
    sum += (1+1/i)**i
print(f"Cумма последовательности (1+1/n)^n = {round(sum,2)}") """
lst = [(1+1/i)**i for i in range(1,n+1)]
print(f"Cумма последовательности (1+1/n)^n равнна {round(sum(lst),2)}")