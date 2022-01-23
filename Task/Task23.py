#Показать таблицу квадратов чисел от 1 до N

from re import S


def SquartTable():
    print("Введите N")
    N=int(input())
    print('')
    s=''
    for i in range(1,N+1):
        s=s+str(i**2)+"\n"
    return s

print(SquartTable())