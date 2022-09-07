
### Condicional if

# Determinar si un número es mayor a 18, utilizando el condicional if.

numero= 20

if numero>18:
    print('Número es mayor que 18')

# Determinar si un número es mayor o menor a 18, utilizando el 
# condicional if y else.

numero=12

if numero>18:
    print('Número es mayor que 18')
else:
    print('Número es igual o menor que 18')

# Pedir a un usuario que ingrese tres números, luego retornar el número
# mayor y el menor. 

num1=float(input('Ingrese número= '))
num2=float(input('Ingrese número= '))
num3=float(input('Ingrese número= '))
mayor=0
menor=0


if (num1>=num2) and (num1>=num3):
    mayor=num1
elif (num2>=num1) and (num2>=num3):
    mayor=num2
elif (num3>=num1 and num3>=num2):
    mayor=num3
print("El número mayor es {}".format(mayor))

