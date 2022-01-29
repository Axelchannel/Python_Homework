##Написать программу получающую набор произведений чисел от 1 до N.
#Пример: пусть N = 4, тогда
#[ 1, 2, 6, 24 ]

def Factorial(n):
    if n==1: return 1
    else: return n * Factorial(n-1)

def Print(n):
    return [Factorial(i) for i in range(1,n+1)]

print(Print(4))

