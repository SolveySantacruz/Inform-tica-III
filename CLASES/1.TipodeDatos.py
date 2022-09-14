# Declaramos las siguientes elementos y asignamos en variables de su elección: 

# Enteros: 10, -100, 500, 200 --> Luego restarlos de manera sucesiva

a=10
b=-100
c=500
d=200
resultado=a-b-c-d
print('Resultado1 =',resultado)

# Flotantes: 100.0, 305.2, 400.3 --> Dividir de manera sucesiva

A,B,C=100.0,305.2,400.3
resultado=A/B/C
print('Resultado2 =', resultado)

# Booleanos: True, False --> Primero sumar y luego restar

a= True
b= False
sumaboo= a+b
restaboo= a-b
print(sumaboo)
print(restaboo)

# Strings: 'Cristian','Juanita' --> sumar y restar
# '', "","""","''" --> ¿Qué sucede?

nombre1= 'cristian'
nombre2= 'Juanita'
cadena1=""
cadena2=''
cadena3=" "" " #Esto no se puede hacer
cadena4="''" 

Suma= nombre1+nombre2
# Resta= nombre1-nombre2   no se puede

print('nombre1 -->', nombre1)
print('nombre2 -->', nombre2)
print('Cadena1 -->', cadena1)
print('Cadena2 -->', cadena2)
print('Cadena4 -->', cadena4)
print('Suma-->',Suma)
#print('Resta -->',Resta) 


# Busque la manera de convertir (casteo)

Entero=10
Flotante=11.5
String= 'Manizales'
String2='123'
Boolenao= True

# Un entero a flotante

print('E a F --> ',Entero, float(Entero)) # Se pueden hacer operaciones en el print

# Un flotante a entero

print('F a E --> ',Flotante, int(Flotante)) # Se pueden hacer operaciones en el print 

# Un flotante y un entero a string

print('E a S --> ',Entero, str(Entero)) # Se pueden hacer operaciones en el print 
print('F a S --> ',Flotante, str(Flotante)) # Se pueden hacer operaciones en el print 

# Un string a un entero y a un flotante

print('S a E --> ',String2, int(String2)) # Se pueden hacer operaciones en el print 
print('S a F --> ',String2, float(String2)) # Se pueden hacer operaciones en el print 

# Un booleano a un entero y a un flotante

print(int(Boolenao==True))
print(float(Boolenao==True))

# Un entero y flotante a booleano

print(bool(Entero))
print(bool(Flotante))

