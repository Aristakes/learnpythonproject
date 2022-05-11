d1 = {}
d2 = dict()
d3 = dict.fromkeys('1')

price = {'meat': 3 , 'bread': 1, 'potato': 0.5 , 'water':0.2 }

users = {
    'Alex7': {'password': 123456, 'id' : 1234},
    'Jimmy99': {'password ' : 654321 , 'id' : 4563},
    'Aris' : {'password' : 567890 , 'id' : 4563}
    }

def buy() :
    pay = 0
    while True :
        enter = input("We buy something : ")
        if enter == "end":
            break
        pay += price[enter]
    return pay

