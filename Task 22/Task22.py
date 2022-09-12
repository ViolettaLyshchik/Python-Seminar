#В текстовом файле посчитать количество строк, а также для каждой отдельной строки определить количество в ней символов и слов.

f = open('textfile.txt','r')
countLines = 0
countwordsInLines = []
countCharsInLines = []
for line in f:
    countLines+=1
    if line != '\n':
        countwordsInLines.append(line.count(' ') + 1)
    else:
        countwordsInLines.append(0)
    countCharsInLines.append(line.count('') -2)
f.close()
print(countLines)
print(countwordsInLines)
print(countCharsInLines)


# f = open('article.txt','r')
# line = 0
# for i in f:
# line += 1
#
# flag = 0
# word = 0
# for j in i:
# if j != ' ' and flag == 0:
# word += 1
# flag = 1
# elif j == ' ':
# flag = 0
#
# print(len(i), 'симв.', word, 'сл.')
# print(line, 'стр.')
# f.close()