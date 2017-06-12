from time import time

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
    lista.append(10)
    lista.append(50)
    lista.append(100)
    lista.append(200)
    lista.append(500)
    lista.append(1000)
    lista.append(2000)
    lista.append(5000)
    #lista.append(10000)
    #lista.append(20000)
    #lista.append(50000)
    return lista

P=creaListaPruebas()

for i in range(0,len(P)):

    L=creaLista(P[i])
    L2=L.copy()

    print("Ordenando la lista de números enteros por método de la burbuja")
    
    tiempo_inicial = time()
    ordenamientoBurbuja(L,len(L))
    tiempo_ejecucion=obtenerTiempoEjecucion(tiempo_inicial,len(L),"Burbuja")
    print("Ha tardado en ordenarla: ", tiempo_ejecucion, " segundos")
    
    print("La primera lista ha sido ordenada correctamente")
    print()
    print("Ordenando la lista de números enteros por quicksort")
    
    tiempo_inicial = time()
    quicksort(L2,0,len(L2)-1)
    tiempo_ejecucion=obtenerTiempoEjecucion(tiempo_inicial,len(L2),"Quicksort")
    print("Ha tardado en ordenarla: ", tiempo_ejecucion, " segundos")
    
    print("La segunda lista ha sido ordenada correctamente")
    #imprimeLista(L2,len(L2))
    print("----------------")
