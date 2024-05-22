"""mi_archivo = open('prueba.txt')

todas = mi_archivo.readlines()
todas = todas[1]
print(todas)"""

archivo = open("prueba.txt","w")
archivo.writelines(['Soy el nuevo texto\n', 'hola mundo aqui estoy\n', 'Que se yo\n'])
archivo.close()

