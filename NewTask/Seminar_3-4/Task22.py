#Найти сумму чисел списка стоящих на нечетной позиции

def L(list):
    sum = 0
    for i in list:
        if i % 2 !=0 :
            sum = sum + i
    return sum 


list = [1,2,3,4,5]
print(L(list))