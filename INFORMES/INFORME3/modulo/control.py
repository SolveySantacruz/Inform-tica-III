"""
Aquí se controla las conversiones
"""
def explicarConversor():
    explicacion=""" 
    --------------------------------------------------------------------
    Bienvenido a conversiones.

    Realiza las conversiones que necesites en los sistemas:
    - Decimal
    - Binario
    - Octal
    - Hexadecimal

    Elige la conversión que deseas realizar:

    1. Decimal a Binario          |   7. Octal a Decimal
    2. Decimal a Octal            |   8. Octal a Binario
    3. Decimal a Hexadecimal      |   9. Octal a Hexadecimal
    4. Binario a Decimal          |  10. Hexadecimal a Decimal
    5. Binario a Octal            |  11. Hexadecimal a Binario
    6. Binario a Hexadecimal      |  12. Hexadecimal a Octal
    ---------------------------------------------------------------------
    """
    print(explicacion) 

print(explicarConversor())
tipoConversion=int(input('Elige la conversión que deseas realizar: '))

while True:
    if tipoConversion>=1 and tipoConversion<=12:
        cadena=(input('Ingrese un número válido a convertir: '))
        break

    else:
        print('Número Inválido')
        tipoConversion=int(input('Elige la conversión que deseas realizar: '))
        cadena=(input('Ingrese un número válido a convertir: '))
        break
    

if tipoConversion==1:
    from decimal import convertirABinario
    conversion= convertirABinario(cadena)
    print('El número {} en sistema binario es '.format(cadena),conversion)
elif tipoConversion==2:
    from decimal import convertirAOctal
    conversion= convertirAOctal(cadena)
    print('El número {} en sistema octal es '.format(cadena),conversion)
elif tipoConversion==3:
    from decimal import convertirAHexadecimal 
    conversion= convertirAHexadecimal(cadena)
    print('El número {} en sistema hexadecimal es '.format(cadena),conversion)
elif tipoConversion==4:
    from binario import convertirADecimal
    conversion= convertirADecimal(cadena)
    print('El número {} en sistema decimal es '.format(cadena),conversion)
elif tipoConversion==5:
    from binario import convertirAOctal
    conversion= convertirAOctal(cadena)
    print('El número {} en sistema octal es '.format(cadena),conversion)
elif tipoConversion==6:
    from binario import convertirAHexadecimal
    conversion= convertirAHexadecimal(cadena)
    print('El número {} en sistema hexadecimal es '.format(cadena),conversion)
elif tipoConversion==7:
    from octal import convertirADecimal
    conversion= convertirADecimal(cadena)
    print('El número {} en sistema decimal es '.format(cadena),conversion)
elif tipoConversion==8:
    from octal import convertirABinario
    conversion= convertirABinario(cadena)
    print('El número {} en sistema binario es '.format(cadena),conversion)
elif tipoConversion==9:
    from octal import convertirAHexadecimal
    conversion= convertirAHexadecimal(cadena)
    print('El número {} en sistema hexadecimal es '.format(cadena),conversion)
elif tipoConversion==10:
    from hexadecimal import convertirADecimal
    conversion= convertirADecimal(cadena)
    print('El número {} en sistema decimal es '.format(cadena),conversion)
elif tipoConversion==11:
    from hexadecimal import convertirABinario
    conversion= convertirABinario(cadena)
    print('El número {} en sistema binario es '.format(cadena),conversion)
elif tipoConversion==12:
    from hexadecimal import convertirAOctal
    conversion= convertirAOctal(cadena)
    print('El número {} en sistema octal es '.format(cadena),conversion)