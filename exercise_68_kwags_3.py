def verificar_ceros(*args):
    for i in range(len(args) - 1):
        if args[i] == 0 and args[i+1] == 0:
            return True
    return False


print(verificar_ceros(3, 3, 4, 3, 2, 3, 0, 9, 0))
print(verificar_ceros(3, 3, 4, 3, 2, 3, 0, 0, 9, 0))
