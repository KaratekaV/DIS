from time import time

import numpy as np
import matplotlib.pyplot as plt
import random

def obtenerTiempoEjecucion(tiempo_inicial,tam,string):
    tiempo_final = time()
    tiempo_ejecucion = tiempo_final - tiempo_inicial
    print("La lista de tamaño: ", tam)
    print("Usando el algoritmo: ", string)
    return tiempo_ejecucion

def quicksort(lista,izq,der):
    i=izq
    j=der
    x=lista[int(round((izq + der)/2))]
 
    while( i <= j ):
        while lista[i]<x and j<=der:
            i=i+1
        while x<lista[j] and j>izq:
            j=j-1
        if i<=j:
            aux = lista[i]; lista[i] = lista[j]; lista[j] = aux;
            i=i+1;  j=j-1;
 
    if izq < j:
        quicksort( lista, izq, j );
    if i < der:
        quicksort( lista, i, der );
        

def ordenamientoBurbuja(lista,tam):
    for i in range(1,tam):
        for j in range(0,tam-i):
            if(lista[j] > lista[j+1]):
                k = lista[j+1]
                lista[j+1] = lista[j]
                lista[j] = k;
    
    
def imprimeLista(lista,tam):
    for i in range(0,tam):
        print (lista[i])
 
def creaLista(cn):
    lista=[]
    print("Creando la lista de números enteros")
    print()
    
    for i in range(0,cn):
        lista.append(int(random.randrange(cn)))
    return lista

def creaListaPruebas():
    lista=[]

    lista.append(500)
    lista.append(1000)
    lista.append(2000)
    lista.append(5000)
    lista.append(10000)
    lista.append(20000)
    lista.append(30000)
    lista.append(40000)
    lista.append(50000)
    return lista

P=creaListaPruebas()
tBurbuja=[]
tQuicksort=[]

for i in range(0,len(P)):

    L=creaLista(P[i])
    L2=L.copy()

    tiempo_inicial = time()
    quicksort(L2,0,len(L2)-1)
    tiempo_ejecucion=obtenerTiempoEjecucion(tiempo_inicial,len(L2),"Quicksort")
    tQuicksort.append(tiempo_ejecucion)
    print("Ha tardado en ordenarla: ", tiempo_ejecucion, " segundos")
    
    print("La primera lista ha sido ordenada correctamente")
    print()
    
    tiempo_inicial = time()
    ordenamientoBurbuja(L,len(L))
    tiempo_ejecucion=obtenerTiempoEjecucion(tiempo_inicial,len(L),"Burbuja")
    tBurbuja.append(tiempo_ejecucion)
    print("Ha tardado en ordenarla: ", tiempo_ejecucion, " segundos")
    
    print("La segunda lista ha sido ordenada correctamente")
    #imprimeLista(L2,len(L2))
    print("----------------")

print("Plotting times...")
print("Burbuja:")
imprimeLista(tBurbuja, len(tBurbuja))

print("---------------")
print("Quicksort:")
imprimeLista(tQuicksort, len(tQuicksort))

fig = plt.figure()
fig.subplots_adjust(bottom=0.2)

ax1 = fig.add_subplot(211)
line1 = ax1.plot(tBurbuja, 'bo-', label='Burbuja')
line2 = ax1.plot(tQuicksort, 'go-', label='Quicksort')

lines = line1+line2
labels = [l.get_label() for l in lines]

ax1.legend(lines,labels, loc=(0,-0.5), ncol=2)
ax1.set_xlabel('Algoritmos')

lbl = [item.get_text() for item in ax1.get_xticklabels()]
lbl[1] = '500'
lbl[2] = '1000'
lbl[3] = '2000'
lbl[4] = '5000'
lbl[5] = '10000'
lbl[6] = '20000'
lbl[7] = '30000'
lbl[8] = '40000'
lbl[9] = '50000'

ax1.set_xticklabels(lbl)

plt.show()
