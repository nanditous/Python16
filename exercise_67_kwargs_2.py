def lista_atributos(**kwargs):
    lista = list(kwargs.values())
    return lista

resultado = lista_atributos(a=1,b=2,c=3,d=4)
print(resultado)
