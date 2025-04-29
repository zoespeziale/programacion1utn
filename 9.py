# Ejercicio 9: Desarrollar las funciones en una biblioteca.

from listas_personas import edades, nombres, mails, country, telefonos

def mostrar_mayorBrasil():
    edadmayor = 0
    for i in range(len(country)):
        if country[i] == "Brazil":
                if edades[i] > edadmayor:
                    edadmayor = edades[i]
    for j in range(len(edades)):
        if edades[j] == edadmayor:
            print(nombres[j], telefonos[j], mails[j])
    return ("Se han mostrado todos los usuarios correspondientes")

print(mostrar_mayorBrasil())