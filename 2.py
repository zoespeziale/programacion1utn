# Ejercicio 2: Desarrollar una función que inicialice una lista de 10 números en 0, pida 
# posición y número a guardar al usuario, lo guarde en una lista en la posición 
# solicitada aleatoriamente y la retorne. El programa principal debe invocar a la 
# función y mostrar por pantalla el retorno.

numeros = [0] * 10

def cargar_numeros():
    for i in range(10):
        posicion = int(input("Indique la posición en la que desea guardar el número: "))
        numeros[posicion] = int(input("Indique el número a guardar: "))
        print(f"Número guardado correctamente: {numeros[posicion]}")
    return (f"La lista de números ingresados es: {numeros}")

                
print(cargar_numeros())