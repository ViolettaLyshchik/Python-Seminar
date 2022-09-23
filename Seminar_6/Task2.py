#Дан список, вывести отдельно буквы и цифры.
#a = ( "a", 'b', '2', '3' ,'c')
#b = ( 'a' , 'b' , 'c')
#c = ( '1', '2', '3')
import numbers


lst = ["a", 'b', '2', '3', 'c']
word = list(filter(lambda x: x.isdigit(), lst))
number = list(filter(lambda x: x.isalpha(), lst))
print(word, number)