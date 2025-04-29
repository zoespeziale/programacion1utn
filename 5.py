# Ejercicio 5: Dadas las siguientes listas:
# Nombres=["Ana","Luis","Juan","Sol","Roberto","Sonia","Ulises","Sofia","Maria","Ped
# ro","Antonio", "Eugenia", "Soledad", "Mario", "Mariela"]
# edades = [23,45,34,23,46,23,45,67,37,68,25,55,45,27,43]
# Desarrollar una función que reciba por parámetro la lista de edades, busque a las 
# personas de menor edad (puede ser más de una) y las retorne. El programa 
# principal deberá mostrar nombre y edad de los menores.

nombres= ["Ana","Luis","Juan","Sol","Roberto","Sonia","Ulises","Sofia","Maria","Pedro","Antonio", "Eugenia", "Soledad", "Mario", "Mariela"]
edades = [23,45,34,23,46,23,45,67,37,68,25,55,45,27,43]

def encontrar_menores(lista:list):
    menores = 100
    for i in range(len(edades)):
        if edades[i] < menores:
            menores = edades[i]
    for j in range(len(edades)):
        if edades[j] == menores:
            print(nombres[j], edades[j])
    return("Se mostraron los usuario de menor edad")

print(encontrar_menores(edades))