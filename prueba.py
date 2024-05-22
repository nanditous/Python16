from random import choice
import os

# Variables globales
palabras = ['panadero', 'dinosaurio', 'helipuerto', 'tiburon']
letras_correctas = []
letras_incorrectas = []
intentos = 6
aciertos = 0
juego_terminado = False


# Función para limpiar la pantalla
def limpiar_pantalla():
    # Para Windows
    if os.name == 'nt':
        os.system('cls')
    # Para Unix (Linux, macOS)
    else:
        os.system('clear')


def elegir_palabra(lista_palabras):
    palabra_elegida = choice(lista_palabras)
    letras_unicas = len(set(palabra_elegida))
    return palabra_elegida, letras_unicas


def pedir_letra():
    letra_elegida = ""
    es_valida = False
    abecedario = "abcdefghijklmnopqrstuvwxyz"

    while not es_valida:
        letra_elegida = input("Elegir una letra: ").lower()
        if letra_elegida in abecedario and len(letra_elegida) == 1:
            if letra_elegida not in letras_correctas and letra_elegida not in letras_incorrectas:
                es_valida = True
            else:
                print("Ya has elegido esa letra, prueba con otra.")
        else:
            print("No has elegido una letra válida")
    return letra_elegida  # Mover return fuera del while


def mostrar_nuevo_tablero(palabra_elegida):
    lista_oculta = []
    for l in palabra_elegida:
        if l in letras_correctas:
            lista_oculta.append(l)
        else:
            lista_oculta.append("-")
    print(" ".join(lista_oculta))


def chequear_letra(letra_elegida, palabra_elegida, vidas, coincidencias, letras_unicas):
    fin = False
    if letra_elegida in palabra_elegida:
        letras_correctas.append(letra_elegida)
        coincidencias += palabra_elegida.count(letra_elegida)
    else:
        letras_incorrectas.append(letra_elegida)
        vidas -= 1

    if vidas == 0:
        fin = perder(palabra_elegida)
    elif coincidencias == letras_unicas:
        fin = ganar(palabra_elegida)

    return vidas, fin, coincidencias


def perder(palabra):
    print("Te has quedado sin vidas!")
    print(f"La palabra oculta era: {palabra}")
    return True


def ganar(palabra_descubierta):
    mostrar_nuevo_tablero(palabra_descubierta)
    print("¡Felicitaciones, has encontrado la palabra!")
    return True


palabra, letras_unicas = elegir_palabra(palabras)

while not juego_terminado:
    limpiar_pantalla()  # Llamar a la función para limpiar pantalla
    print("\n" + "*" * 20 + "\n")
    print("Letras incorrectas: " + "-".join(letras_incorrectas))
    print(f"Vidas: {intentos}")
    print("\n" + "*" * 20 + "\n")
    mostrar_nuevo_tablero(palabra)
    letra = pedir_letra()
    intentos, juego_terminado, aciertos = chequear_letra(letra, palabra, intentos, aciertos, letras_unicas)
