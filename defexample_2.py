def exclusive_item(*args , key = False):
    newlist = []
    for i in args:
        for y in i:
            if y not in newlist:
                newlist.append(y)
    if key == True:
        newlist.sort()
    else:
        print("key is False and tuple coming with out sorting")
    return newlist




z = [9 , 8 , 7 ]
x = [8 , 8 , 9 , 7 , 6 , 5 ]
c  = [1 , 2 , 3 , 4 , 5 , 6 , 7 , 7]

t = exclusive_item(z , x , c , key = True)

print(t)