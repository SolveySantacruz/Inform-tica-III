"""
El modulo binario contiene las siguientes funciones:
            convertirADecimal     => recibe string (cadena_binario), retorna string (cadena_decimal)
            convertirAOctal       => recibe string (cadena_binario), retorna string (cadena_octal)
            convertirAHexadecimal => recibe string (cadena_binario), retorna string (cadena_hexadecimal)
"""
def convertirADecimal(cadena_binario):
    cadena_decimal=str(int(cadena_binario,2))
    return cadena_decimal

def convertirAOctal(cadena_binario):
    cadena_octal=str(oct(int(cadena_binario,2)))
    return cadena_octal

def convertirAHexadecimal(cadena_binario):
    cadena_hexadecimal=str(hex(int(cadena_binario,2)))
    return cadena_hexadecimal