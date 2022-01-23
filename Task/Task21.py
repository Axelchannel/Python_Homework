#Программа проверяет пятизначное число на палиндромом.

def CheckThePolindrom(n):
    if n // 10000 == n % 10 and n // 1000 % 10 == n // 10 % 10:
        return True
    else:
        return False

print(CheckThePolindrom(32123))

