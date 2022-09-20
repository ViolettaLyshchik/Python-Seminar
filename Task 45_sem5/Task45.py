#Напишите программу, удаляющую из текста все слова, содержащие "абв".
with open("words45.txt", "r") as fin:
    for line in fin:
        words = line.split()
        for word in words:
            if "абв" in word:
                words.remove(word)
        sentence = " ".join(words)
        print(sentence)
        