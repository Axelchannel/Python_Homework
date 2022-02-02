#Задать список из n чисел последовательности 
#(1+1/n)*n и вывести на экран их сумму

def list(n):
    list =[]
    for i in range(1,n+1):
        list.append((1+1/i)**i)
    return list

def sumList(list):
    sum=0
    for i in list:
        sum+=i
    return sum

list = list(2)
print(list)

print(sumList(list))
