text = open("text3.txt")

textreader = text.read()

print(textreader)

list_for_delete_symbols = ['(' , ')' , '"']

for i in list_for_delete_symbols:
    textreader = textreader.replace(i , '')

print("text after deleting symbols\n")

print(textreader)


print("\n")


text2 = textreader.split()

print(text2)

#use join method

new_text = "_$_".join(text2)

print(new_text)