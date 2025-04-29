# Ejercicio 1: Desarrollar una función que pida 10 nombres de manera secuencial, los 
# guarde en una lista y la retorne. El programa principal debe invocar a la función y
# mostrar por pantalla el retorno.

nombres = [0] * 10

def pedir_nombres():
    for i in range (10):
        nombres[i] = input("Indique su nombre y apellido: ")
    return nombres

print(pedir_nombres())