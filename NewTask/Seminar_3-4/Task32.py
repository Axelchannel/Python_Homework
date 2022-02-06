#Дана последовательность чисел. Получить список неповторяющихся 
# элементов исходной последовательности
#Пример: [1, 2, 3, 5, 1, 5, 3, 10] => [1, 2, 3, 5, 10]

from random import randint

def Create_List():
    return [randint(1,22) for i in range(5)]

def New_List(list):
    return [i for i in set(list)]



list = Create_List()
print(list)


print(New_List(list))