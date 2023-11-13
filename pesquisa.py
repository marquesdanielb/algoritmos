def pesquisa_binaria(lista, item):
    baixo = 0 #1 
    alto = len(lista) - 1 #1

    while baixo <= alto: #2
        meio = int((baixo + alto) / 2) #3
        chute = lista[meio]
        if chute == item: #4
            return meio
        if chute > item: #5
            alto = meio - 1
        else: #6
            baixo = meio + 1
    return None #7

minha_lista = [1, 3, 5, 7, 9] #8

print(pesquisa_binaria(minha_lista, 9)) #9
print(pesquisa_binaria(minha_lista, -1)) #10
