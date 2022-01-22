#Выяснить, кратно ли число заданному, если нет, вывести остаток

def CheckNumber(a):
    if a % 125 == 0:
        return "Кратно"
    else:
        return  a % 125
   
print(CheckNumber(200))
