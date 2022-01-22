#Возведите число А в натуральную степень B используя цикл

def Extent():
    print("Введите число")
    a = float(input())
    print("Введите натуральную степень")
    b=int(input())
    result=a
    for i in range(1,b):
        result = result * a
    return result

print(Extent())
