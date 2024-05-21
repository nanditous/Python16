def suma_cuadrados(*args):
    suma = 0
    for n in args:
        suma += n**2
    return suma


resultado = suma_cuadrados(1, 2, 3, 4)
print(resultado)
