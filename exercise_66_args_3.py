def numeros_persona(nombre, *numeros):
    suma_numeros = sum(numeros)
    mensaje = f"{nombre}, la suma de tus números es {suma_numeros}"
    return mensaje


resultado = numeros_persona("Fernando",1, 2, 3, 4, 5, 6, 7)
print(resultado)