def regressiva(i):
    print(i)
    if i <= 1:
        return
    else:
        regressiva(i-1)
    
def fat(x):
    if x == 1:
        return
    else:
        return x * fat(x-1)

#Outros exemplos de recursão
def soma(lista):
    if lista == []:
        return 0
    else:
        return lista[0] + soma(lista[1:])
    
def conta(lista):
    if lista == []:
        return 0
    else:
        return 1 + conta(lista[1:])
    
def maximo(lista):
    if len(lista) == 2:    
        return lista[0] if lista[0] > lista[1] else lista[1]
    sub_max = maximo(lista[1:])
    return lista[0] if lista[0] > sub_max else sub_max

print(conta([8,2,4,5,6,12,66]))    
print(soma([1,67,2,6]))
print(maximo([8,2,4,5,6,12,66]))
print(fat(3))
print(regressiva(10))