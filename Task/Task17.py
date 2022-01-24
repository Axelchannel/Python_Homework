#По двум заданным числам проверять является ли одно квадратом другого

def CheckSqrt():
    print("Введите два числа")
    a=int(input())
    b=int(input())
    if b==a**2 or a == b**2: return True

print(CheckSqrt())

