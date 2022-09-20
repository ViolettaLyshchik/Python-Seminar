#НОД
#while a != b:
#    if a > b:
#       a -= b
#    else:
#        b -= a

#print(a)
a=123
b=23
if a < b :
    a, b = b, a

while b!=0:
    a, b = b, a % b

print(a)