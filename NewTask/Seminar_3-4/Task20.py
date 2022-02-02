#Определить, присутствует ли в заданном списке строк, 
# некоторое число

def FindNumber(number,list):
    count = 0
    for i in list:
        if str(number) or int(number)== list[count]:
            return True
        else: count += 1 
    return False 

list = ['a', 'b', 'c', 3]
number = 3

print(FindNumber(number,list))