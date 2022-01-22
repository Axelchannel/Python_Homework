#Подсчитать сумму цифр в числе

def SumNumbers(a):
    s=0
    while a!=0:
        i= a % 10
        s=s+i
        a=a//10
    return s



print(SumNumbers(251))
