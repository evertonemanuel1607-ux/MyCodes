def buscarmenor(arr):
    menor_ind = 0
    menor = arr[menor_ind]
    for i in range(1,len(arr)):
        if arr[i] < menor:
            menor = arr[i]
            menor_ind = i
    return menor_ind

def ordenacao(arr):
    newarr = []
    for i in range(len(arr)):
        menor = buscarmenor(arr)
        newarr.append(arr.pop(menor))
    return newarr


print(ordenacao([70,40,2,50,42]))
