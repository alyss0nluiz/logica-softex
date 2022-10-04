import random
def bubbleSort(numeros):
    elementos = len(numeros)-1
    troca = 0
    sequencia = False
    while sequencia == False:
        for i in range(elementos):
            if (numeros[i] > numeros[i+1]):
                troca = numeros[i]
                numeros[i] = numeros[i+1]
                numeros[i+1] = troca
                print (numeros)
    return numeros
numeros = []
for i in range(0,10,1):
    numeros.append(random.randint(0,100))
print(numeros)
bubbleSort(numeros)