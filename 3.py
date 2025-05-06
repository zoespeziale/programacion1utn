# Ejercicio 3: Dadas las siguientes listas:
# Estudiantes =
# ["Ana","Luis","Juan","Sol","Roberto","Sonia","María","Sofia","Maria","Pedro","Anto
# nio", "Eugenia", "Soledad", "Mario", "María"]
# Apellidos = 
# [“Sosa”,”Gutierrez”,”Alsina”,”Martinez”,”Sosa”,”Ramirez”,”Perez”,”Lopez”,”Arregui”
# ,”Mitre”,”Andrade”,”Loza”,”Antares”,”Roca”,”Perez”]
# Nota = [8 ana sosa,4 luis gutierrez,9 juan alsina,10 sol martinez,8 roberto sosa,6 sonia ramirez,4 maria perez,8 sofia lopez,7 maria arregui,5 pedro mitre,6 antonio andrade,7 eugenia loza,10 soledad antares,4 mario roca,8 maria perez]
# Desarrollar una función que realice el ordenamiento de las listas por apellido de 
# manera ascendente, si el apellido es el mismo, debe ordenar por nombre de manera 
# ascendente, si el nombre también es el mismo, debe ordenar por nota de manera 
# descendente.

Estudiantes =["Ana","Luis","Juan","Sol","Roberto","Sonia","María","Sofia","Maria","Pedro","Antonio", "Eugenia", "Soledad", "Mario", "María"]
Apellidos = ["Sosa","Gutierrez","Alsina","Martinez","Sosa","Ramirez","Perez","Lopez","Arregui","Mitre","Andrade","Loza","Antares","Roca","Perez"]
Nota = [8,4,9,10,8,6,4,8,7,5,6,7,10,4,8]

def ordenar_estudiantes(nombres:list, apellidos:list, notas:list):
    for i in range(len(apellidos)+1):
        for j in range(i+1, len(apellidos)):
            if apellidos[i] > apellidos[j]:
                aux = apellidos[i]
                apellidos[i] = apellidos[j]
                apellidos[j] = aux
                aux2 = nombres[i]
                nombres[i] = nombres[j]
                nombres[j] = aux2
                aux3 = notas[i]
                notas[i] = notas[j]
                notas[j] = aux3
            if apellidos[i] == apellidos[j]:
                if nombres[i] > nombres[j]:
                    aux4 = nombres[i]
                    nombres[i] = nombres[j]
                    nombres[j] = aux4
                    aux5 = notas[i]
                    notas[i] = notas[j]
                    notas[j] = aux5
                if nombres[i] == nombres[j]:
                    if notas[i] < notas[j]:
                        aux6 = notas[i]
                        notas[i] = notas[j]
                        notas[j] = aux6
    return nombres, apellidos, notas

print(ordenar_estudiantes(Estudiantes, Apellidos, Nota))