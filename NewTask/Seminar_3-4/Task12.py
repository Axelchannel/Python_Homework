#Для натурального N создать словарь индекс-значение, 
# состоящий из элементов последовательности
#3k + 1.

def Dictionary(n):
    return {i:3*i + 1 for i in range(1, n)}

print(Dictionary(5))
        