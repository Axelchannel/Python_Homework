#Задать номер четверти, показать диапазоны для возможных координат

def Quarter():
    print("Введите номер четверти")
    a = int(input())
    if a == 1: print("Первая четверть: x>0,y>0")
    if a == 2: print("Вторая четверть: x<0,y>0")
    if a == 3: print("Третья четверть: x<0,y<0")
    if a == 4: print("Чётвертая четверть: x>0,y<0")


Quarter()