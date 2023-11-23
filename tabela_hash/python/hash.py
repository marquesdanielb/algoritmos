caderno = dict()
caderno["maca"] = 0.67
caderno["leite"] = 1.49
caderno["abacate"] = 1.49
print(caderno)

lista_telefonica = {}
lista_telefonica["jenny"] = 98989999
lista_telefonica["emergencia"] = 192
print(lista_telefonica["jenny"])

votou = {}
votou["augusto"] = True
votou["virgulino"] = True

def verifica_eleitor(nome):
    if votou.get(nome):
        print("Já votou")
    else:
        votou[nome] = True
        print("Deixa votar")
        
print(verifica_eleitor("augusto"))
