#Показать четные числа от 1 до N

from re import S


def ShowNum(n):
    s=' '
    for i in range(1,n+1):
        if i % 2 ==0:
            s =s+'\n'+str(i)
    return s 
        
print(ShowNum(10))