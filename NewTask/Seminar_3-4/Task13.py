#Пользователь задаёт две строки. Определить количество вхождений одной строки в другой.


def String(a,b): 
    сount = 0
    c = a.intersection(b)
    return len(c)

a = {1,2,3}
b = {2}
    
print(String(a,b))