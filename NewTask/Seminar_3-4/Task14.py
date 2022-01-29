#Подсчитать сумму цифр в вещественном числе

def Sum(a):
    sum = 0
    for i in str(a):
        if i !='.':
            sum=sum+int(i)
    return sum

a = float(input())
print(Sum(a))
