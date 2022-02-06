#В заданном списке вещественных чисел найдите разницу между 
#максимальным и минимальным значением дробной части элементов. 
#Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19


def Find_Max(list):
    max = 0.01
    for i in list:
        if round(i % 1,2)>max: max = round(i % 1,2)
    return max


def Find_Min(list):
    min  = 0.99
    for i in list:
        if round(i % 1,2)<min: min = round ( i % 1, 2)
    return min 



list = [1.2,1.04,10.05]


print(Find_Max(list))

print(Find_Min(list))

print("Разница:")
print(Find_Max(list)-Find_Min(list))
        



