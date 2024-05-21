def suma_absolutos(*args):
    suma = 0
    for n in args:
        suma += abs(n)
    return suma


resultado = suma_absolutos(1, 2, 3, -4, -5, -40)
print(resultado)