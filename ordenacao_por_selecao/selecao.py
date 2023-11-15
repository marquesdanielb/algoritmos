def buscaMenor(arr):
    menor = arr[0] #1.1 Armazena o menor valor.
    menor_indice = 0 #1.2 Armazena o índice do menor valor.
    for i in range(1, len(arr)):
        if arr[i] < menor:
            menor = arr[i]
            menor_indice = i
    return menor_indice

def ordenacaoporSelecao(arr): #2.1 Oredenações em um array
    novoArr = []
    for i in range(len(arr)):
        menor = buscaMenor(arr) #2.2 Encontra o menor elemento do array e adiciona ao novo array
        novoArr.append(arr.pop(menor))
    return novoArr

print(ordenacaoporSelecao([5, 3, 6, 13, 10]))