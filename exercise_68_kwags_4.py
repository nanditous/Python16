def es_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True


def contar_primo(numero):
    primos = []
    for i in range(2, numero + 1):
        if es_primo(i):
            primos.append(i)
    print(f"Números primos en el rango de 0 a {numero}: {primos}")
    return len(primos)


cantidad_de_primos = contar_primo(30)
print(f"Cantidad de números primeros encontrados {cantidad_de_primos}")
