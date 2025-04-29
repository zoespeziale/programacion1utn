# Ejercicio 7:
# Una startup desea analizar las estadísticas de los usuarios de su sitio de 
# compras on-line recientemente lanzado al mercado. Para ello necesita un programa 
# que le permita acceder a los datos relevados.
# Realizar una función con el siguiente Menú de Opciones:
# 1-Importar listas
# 2-Listar los datos de los usuarios de México
# 3-Listar los nombres, mails y teléfonos de los usuarios de Brasil
# 4-Listar los datos del/los usuario/s más joven/es
# 5-Obtener un promedio de edad de los usuarios
# 6-De los usuarios de Brasil, listar los datos del usuario de mayor edad
# 7-Listar los datos de los usuarios de México y Brasil cuyo código postal 
# sea mayor a 8000
# 8-Listar nombre, mail y teléfono de los usuarios italianos mayores a 40 
# años.

def mostrar_menu():
    funcion = int(input("Indique el númeron de la función que desea realizar: 1. Importar listas 2. Listar los datos de los usuarios de México 3. Listar los nombre, mail y teléfono de los usuarios de Brasil 4.Listar los datos del/los usuario/s más joven/es 5. Obtener un promedio de edad de los usuarios 6. De los usuarios de Brasil, listar los datos del usuario de mayor edad 7. Listar los datos de los usuarios de México y Brasil cuyo código postal sea mayor a 8000 8. Listar nombre, mail y teléfono de los usuarios italianos mayores a 40 años: "))
    while funcion < 1 or funcion > 8:
        funcion = int(input("Opción incorrecta. Indique el númeron de la función que desea realizar: 1. Importar listas 2. Listar los datos de los usuarios de México 3. Listar los nombre, mail y teléfono de los usuarios de Brasil 4.Listar los datos del/los usuario/s más joven/es 5. Obtener un promedio de edad de los usuarios 6. De los usuarios de Brasil, listar los datos del usuario de mayor edad 7. Listar los datos de los usuarios de México y Brasil cuyo código postal sea mayor a 8000 8. Listar nombre, mail y teléfono de los usuarios italianos mayores a 40 años: "))
    return funcion

print(mostrar_menu())


# Ejercicio 8: 
# Crear una función para cada opción de menú. Nota: No se podrá acceder a ninguna opción de menú si no se realizó la importación 
# de las listas.

from listas_personas import nombres, telefonos, mails, address, postalZip, region, country, edades

def importar_listas():
    from listas_personas import nombres, telefonos, mails, address, postalZip, region, country, edades
    return nombres, telefonos, mails, address, postalZip, region, country, edades

def mostrar_usuariosMexico():
    for i in range(len(country)):
        if country[i] == "Mexico":
            print(nombres[i], telefonos[i], mails[i], address[i], postalZip[i], edades[i])

def mostrar_datosBrasil():
    for i in range(len(country)):
        if country[i] == "Brasil":
            print(nombres[i], mails[i], telefonos[i])

def mostrar_usuariosJovenes():
    kjdf

def mostrar_promedioEdad():
    promedio = (edades + edades) / len(edades) 
    return promedio


def mostrar_mayorBrasil():
    edadmayor = 0
    for i in range(len(country)):
        if country[i] == "Brasil":
            for j in range(len(edades)):
                if edades[j] > edadmayor:
                    edadmayor = edades[j]
    return edadmayor

def mostrar_cpmayor():
    for i in range(len(country)):
        if country[i] == "Mexico" or country[i] == "Brasil":
            if postalZip[i] > 8000:
                print(nombres[i], mails[i], edades[i])
    return ("se han mostrado todos los usuarios correspondientes")
            


print(mostrar_usuariosMexico())
