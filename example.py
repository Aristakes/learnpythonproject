
text = open('text.txt')
text1 = set(text.read().split())
text.close()

text = open('text2.txt')
text2 = set(text.read().split())
text.close()

#совподаушие слова
new = text1.intersection(text2)
print(new)

#не совпадаушие
new2 = text1.difference(text2)
print(new2)