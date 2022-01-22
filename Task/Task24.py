#Найти кубы чисел от 1 до N

def FindCubes(N):
    r=range(1,N+1)
    s=''
    for i in r:
        s =s+ str(i**3) +'\n'
    return s 

print(FindCubes(5))