# Ejercicio 6: Analizar los datos del archivo listas_personas.py. Utilizando el archivo 
# listas_personas.py. Importar los nombres a una lista. Realizar una función que 
# muestre los mismos.

from listas_personas import nombres

nombres_personas = [nombres]

def mostrar_nombres(lista:list):
    return lista

print(mostrar_nombres(nombres_personas))