from random import choice


def lanzar_moeda():
    moneda = ["Cara", "Cruz"]
    lanza = choice(moneda)
    return lanza


def probar_suerte(a,b):
    if a == "Cara":
        print("La lista se autodestruirá")
        return []
    elif a == "Cruz":
        print("La lista fué salvada")
        return b


lista_numeros = [1, 2, 3, 4, 5, 6]
tirar = lanzar_moeda()
probar = probar_suerte(tirar, lista_numeros)
print(probar)
