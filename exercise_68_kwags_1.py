def devolver_distintos(num1, num2, num3):
    suma = num1 + num2 + num3

    numeros = [num1,num2, num3]
    mayor = max(numeros)
    menor = min(numeros)

    for numero in numeros:
        if numero !=mayor and numero !=menor:
            intermedio = numero
            break

    if suma > 15:
        return mayor
    elif suma < 10:
        return menor
    else:
        return intermedio


print(devolver_distintos(5,5,6))
print(devolver_distintos(1,2,3))
print(devolver_distintos(6,5,1))