""" with open("words45.txt", "r") as fin:
    for line in fin:
        words = line.split()
        for word in words:
            if "абв" in word:
                words.remove(word)
        sentence = " ".join(words)
        print(sentence) """


text = 'Напишите абв программу программу, удаляющую из этого абв текста все вабвс слова, содерабващие содержащие "абв"'

def del_abv_words(text):
    text = list(filter(lambda x: 'абв' not in x, text.split()))
    return " ".join(text)

text = del_abv_words(text)
print(text)