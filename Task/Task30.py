#Показать кубы чисел, заканчивающихся на четную цифру

def CubesOfNumbers():
    print("Введите число")
    a=int(input())
    if a%2 == 0:
       return a**3

print(CubesOfNumbers())