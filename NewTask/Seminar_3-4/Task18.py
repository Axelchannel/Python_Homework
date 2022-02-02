#Реализовать алгоритм перемешивания списка
import random
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
def mix (arr):
    for i in arr:
        random_index = random.randint(i, len(arr) - 1)
        temporary = arr[i]
        arr[i] = arr[random_index]
        arr[random_index] = temporary
    return arr
print (mix(list))