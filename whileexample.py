x = ''

while len(x) < 5:
    y = input('enter date ')
    if y == 'o':
        continue
    elif y == 'exit':
        break

    x += y

else:
    print(x)
