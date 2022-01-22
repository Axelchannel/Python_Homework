def FindMaxFromThree(x,y,z):
    max = x
    if max<y:
        max=y
    if max<z:
        max = z
    return max

print(FindMaxFromThree(3,5,7))

