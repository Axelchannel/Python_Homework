#Проверить истинность утверждения ¬(X ⋁ Y) = ¬X ⋀ ¬Y

def Statement(x,y,z):
    return not(x or y or z) == (not x and not y and not z) 

def CheckTheStat():
    for x in range(0,2):
        for y in range(0,2):
            for z in range(0,2):

                print(Statement(x,y,z))


CheckTheStat()
