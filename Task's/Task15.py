# Дано число. Проверить, кратоно ли оно 7 и 23

def Multiplicity(number):
    return a % 7 == 0  and a % 23 == 0

print("Введите число")
a = int(input())

print(Multiplicity(a))
      