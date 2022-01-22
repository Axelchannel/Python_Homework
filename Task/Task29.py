#Написать программу вычисления произведения чисел от 1 до N

def ProductOfNumber(n):
    s=1
    for i in range(1,n+1):
        s=s*i
    return s 

print(ProductOfNumber(3))