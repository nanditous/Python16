lista_numeros = [1, 2, 15, 7, 2]


def reducir_lista(lista):
    # elimino duplicados y ordeno
    lista_sin_duplicados = list(set(lista))
    lista_sin_duplicados.sort()
    # elimino el más alto
    lista_sin_duplicados.pop()
    return lista_sin_duplicados


def promedio(lista):
    if len(lista) == 0:
        return 0
    else:
        return sum(lista) / len(lista)


lista_reducida = reducir_lista(lista_numeros)
resultado = promedio(lista_reducida)
print(resultado)
