alphabet = "qwertzuiopasdfghjklyxcvbnm"
text = input("Please write the text : ")

for x in alphabet:
    count = 0
    for r in text:
        if x == r:
            count += 1
    if count > 0 :
        print("Character " , x , " have text : " , count)