#Показать четные числа от 1 до N
from random import randint
def Randomize():
    return randint(1,22)

def ShowNum(n):
    r=range(1,n+1)
    for i in r:
        if n % 2 ==0:
            return n

n = Randomize
print(n)





