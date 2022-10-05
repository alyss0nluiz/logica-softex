import random

def insertion_sort(array):
    for mov in range(1, len(array)):
        vetor = array[mov]
        j = mov - 1

        while (j >= 0) and (vetor < array[j]):
            array[j + 1] = array[j]
            j = (j -1)
            array[j + 1] = vetor

lista = []
for i in range(0, 30):
    lista.append(random.randint(1, 1000))
    if lista[i] %2 == 1:
        lista[i] = lista[i]
    else:
        lista[i] = lista[i] + 1

print("\nLista a ser ordenada:\n",lista)
insertion_sort(lista)
print('\nVetor em ordem crescente:\n',lista)