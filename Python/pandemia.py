N, M = map(int,input("").split())
I, R = map(int,input("").split())

reunioes = []

for i in range(M):
    lista = map(int,input("").split())
    reunioes.append(lista)

for i in range(R,len(reunioes)):
    infecatos = [I]
    if I in reunioes[i]:
        for i in reunioes[i]:
            if i not in infecatos: 
                infecatos.append(i)

print(len(infecatos) + 1)
                
                 
