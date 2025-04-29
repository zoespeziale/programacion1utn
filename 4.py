# Ejercicio 4: Desarrollar una función que reciba por parámetro, una lista de números 
# y un número especificado. La misma debe buscar el número especificado en la lista 
# y retornar “True” si existe.

numeros = [20, 4, 33, 22, 7, 25]

def encontrar_numero(numero:int, numeros:list):
    for i in range(len(numeros)):
        if numeros[i] == numero:
            print("El número ingresado pertenece a la lista")
            return True
    else:
        print("El número ingresado no pertenece a la lista")
        return False


numero = int(input("Indique un número para verificar si se encuentra en la lista: "))
print(encontrar_numero(numero, numeros))