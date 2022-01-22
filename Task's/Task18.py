
def Tr(x,y,z):
    return not(x or y or z) == (not x and not y and not z)

def Change(x,y,z):
    r=range(0,2)
    for x in r:
        for y in r:
            for z in r:
                Tr(x,y,z)


