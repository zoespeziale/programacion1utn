# Ejercicio 3: Desarrollar una función que pida 10 números dentro de un rango 
# especificado, validar los números solicitados dentro de ese rango, guardar en una 
# lista y retornarla. El programa principal debe invocar a la función y mostrar por 
# pantalla el retorno.

numeros = [0] * 10

def cargar_numeros():
    for i in range(10):
        numero = int(input("Indique un número del 10 al 30: "))
        while numero < 10 and numero > 30:
            numero = int(input("El número ingresado es incorrecto. Indique un número del 10 al 20: "))
        numeros[i] = numero
    return (f"Los números ingresados son: {numeros}")

print(cargar_numeros())