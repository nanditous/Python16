def letras_unicas_ordenadas(palabra):
    letras_unicas = set(palabra)
    print(letras_unicas)
    lista_letras = list(letras_unicas)
    print(lista_letras)
    lista_letras.sort()
    return lista_letras

resultado = letras_unicas_ordenadas("entretenido")
print(resultado)

