#Написать программу преобразования десятичного числа в двоичное

def Change(number):
    list = []
    while number > 0 :
        list.insert(0,number % 2 )
        number = number // 2
    return list

print(Change(222))
        

        

    