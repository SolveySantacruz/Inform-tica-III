# 14 de septiembre

### Iterables y sus métodos

cadena1='Anita lava la tina '
print(cadena1.upper()) #Retorna una nueva cadena en mayúsculas

print(cadena1.lower())
print(cadena1.capitalize())
print(cadena1.count('a')) #Retorna un entero

print(cadena1.isalnum()) # Para hacer preguntas. Retorna booleanos
print(cadena1.isalpha())# Para hacer preguntas
print(cadena1.replace('Anita','Cristian'))
print(cadena1.center(50))# Retorna una nueva cadena centrada 50 espacios

### Métodos de indexación y slicing 

cadena2= 'Mensaje para informatica 3'

str1='HOLAMUNDO'
print(str1[4])
print(str1[2:7:1]) #Funciona igual que los rangos

# Indexación

print(cadena2[0]) # primer elemento de la cadena
print(cadena2[1]) #Segundo elemento de la cadena
print(cadena2[-7:-2:1])

print(cadena2[-1]) #último elemento de la cadena
print(cadena2[-2]) #penúltimo elemento de la cadena

# Slicing

# Extraer toda la cadena al revéz.

print(cadena2[-1:-(len(cadena2)-1):-1])
print(cadena2[-1::-1])
print(cadena2[::-1])

# Extraer cada tercer elemento empezando en el segundo índice

print(cadena2[1:(len(cadena2)-1):3])

# Extraer los dos elementos en la mitad de la cadena
print(cadena2[(len(cadena2)//2):((len(cadena2)//2)+1):1])


