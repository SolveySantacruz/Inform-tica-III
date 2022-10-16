# 05 - 10 - 2022

#---------------------EJERCICIOS DICCIONARIOS ---------------------

#Los diccionarios son una estructura de datos que contienen
#un par clave-valor. Permite acceder a la información de una manera
# mas personalizada y eficiente

diccionarioEstudiantes = {
    "Cristian Pachon": 2.0,
    "Maria Bermudez" : 3.0,
    "Camilo Ibarra" : 4.0,
    "Fernanda Gutierrez": 5.0
}

diccionarioPaises = {
    "Colombia": ["Cali", "Manizales", "Cartagena"],
    "Argentina": ["Buenos Aires", "La plata", "Cordoba"],
    "Brasil": ["Sao Paulo", "Brasilia", "Minas Gerais"]
}

diccionarioNumeros = {
    1: "uno",
    2: "dos",
    3: "tres",
    4: "cuatro",
    5: "cinco"
}

# ¿Cómo extraer un valos dada una clave
# """Extraer del diccionario estudiantes el valor de la clave Camilo Ibarra"""
valor = diccionarioEstudiantes["Camilo Ibarra"]
print(valor)

# """Imprimir todos los valores de diccionarioEstudiantes"""
for clave in ["Cristian Pachon","Maria Bermudez","Camilo Ibarra","Fernanda Gutierrez"]:
    print(diccionarioEstudiantes[clave])

# ¿Cómo eliminar un par clave-valor?
# """Eliminar los elementos cuya clave empiece por la letra C en diccionarioEstudiantes"""

for clave in ["Cristian Pachon","Maria Bermudez","Camilo Ibarra","Fernanda Gutierrez"]:
    if clave[0] == "C":
        diccionarioEstudiantes.pop(clave)
print(diccionarioEstudiantes)

# ¿Cómo agregar un par clave-valor?
# """Agregar los siguientes estudiantes en el diccionarioEstudiantes
# - Juan Loaiza (3.2)
# - Sofia Ospina (5.0)
# - Miguel Pineda (3.1)

diccionarioEstudiantes["Juan Loaiza"] = 3.2
diccionarioEstudiantes["Sofia Ospina"] = 5.0
diccionarioEstudiantes["Miguel Pineda"] = 3.1
print(diccionarioEstudiantes)

# ¿Cómo cambiar un valor?
#"""Cambiar la calificacion de diccionarioEstudiantes así:
#    -Mujeres: 5.0
#    -Hombres: 0.0


for clave in diccionarioEstudiantes:
    if clave.split()[0][-1] == "a":
        diccionarioEstudiantes[clave] = 5.0
    else:
        diccionarioEstudiantes[clave] = 0.0
print(diccionarioEstudiantes)

# ¿cómo extraer todas las claves de un diccionario?

claves = diccionarioEstudiantes.keys()
print(claves)

# ¿ Cómo extraer todos los valores de un diccionario

valores = diccionarioEstudiantes.values()
print(valores)

# ¿ Como extraer los pares clave-valor?
parejas = diccionarioEstudiantes.items()
print(parejas)
