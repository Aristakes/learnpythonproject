swap1 = 2
swap2 = 5

print("Before swap ")
print("swap1 : " + str(swap1))
print("swap2 : " + str(swap2))

print("____________________")

swap1 , swap2 = swap2 + swap1 , swap1 - swap2

print("swap2 + swap1 : " + str(swap1))
print("swap1 - swap2 : " + str(swap2))

print("after swap : swap2 : " + str(swap2))


