#Найти сумму чисел от 1 до А


def Sum(a):
    s=0
    for i in range(1,a+1):
        s=s+i
    return s

print(Sum(5))