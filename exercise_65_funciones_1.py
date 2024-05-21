from random import randint

def lanzar_dados():
    dado_1 = randint(1,6)
    dado_2 = randint(1,6)
    return dado_1, dado_2

def evaluar_jugada(dado1,dado2):
    suma_dados = dado1 + dado2
    if suma_dados <= 6:
        return f"La sumna de tus dados es {suma_dados}. Lamentablemente"
    elif suma_dados >= 6 and suma_dados <10:
        return f"La suma de tus dados es {suma_dados}. Tienes buenas chances"
    elif suma_dados >= 10:
        return f"La suma de tus dados es {suma_dados}. Parece un jugada ganadora"

dado1,dado2 = lanzar_dados()

resultado = evaluar_jugada(dado1,dado2)

print(resultado)