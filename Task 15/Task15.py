#Напишите программу, в которой пользователь будет задавать две строки, а программа - определять количество вхождений одной строки в другой.

#str_1 = input('Введите первую строку для сравнения: ')
#str_2 = input('Введите вторую строку для сравнения: ')
#for s in str_1: 
a = 'pyt'
b = 'pythonpythonpython'
count = 0
for i in range(0, len(b) - len(a)):
    if b[i:i + len(a)] == a:
        count += 1
print(count)