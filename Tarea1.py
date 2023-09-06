from random import randint
from time import time as seg

n = 3100*10
lista = []

while len(lista)<n:
    ale = randint(1,n)
    if not(ale in lista):
        lista.append(ale)

inicio = seg()
lista1 = []
lista2 = []

for valor in lista:
    if valor<(n//2):
        lista1.append(valor)
    else:
        lista2.append(valor)
        

for i in range(len(lista1)):
    for x in range(len(lista1)-1):
        if lista1[x] > lista1[x+1]:
            lista1[x], lista1[x+1] = lista1[x+1], lista1[x]


for i in range(len(lista2)):
    for x in range(len(lista2)-1):
        if lista2[x] > lista2[x+1]:
            lista2[x], lista2[x+1] = lista2[x+1], lista2[x]


fin = seg()

print(fin - inicio)


