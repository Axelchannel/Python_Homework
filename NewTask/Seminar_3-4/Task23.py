#Найти произведение пар чисел в списке. 
#Парой считаем первый и последний элемент, 
#второй и предпоследний и т.д. 
#Пример: [2, 3, 4, 5, 6] => [12, 15, 16]; [2, 3, 5, 6] => [12, 15] 



from os import name


def FindMulti(n):
    list = []
    for i in range((len(n)+1)//2):
        list.append(n[i] * n[-i-1])
    return list  

list = [2,3,4,5,6]
print(FindMulti(list))  


        
