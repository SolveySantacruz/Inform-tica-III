"""
El modulo Octal contiene las siguientes funciones:
            convertirABinario     => recibe string (cadena_octal), retorna string (cadena_binario)
            convertirADecimal     => recibe string (cadena_octal), retorna string (cadena_decimal)
            convertirAHexadecimal => recibe string (cadena_octal), retorna string (cadena_hexadecimal)
"""

def convertirABinario(cadena_octal):
    cadena_binario=str(bin(int(cadena_octal,8)))
    return cadena_binario

def convertirADecimal(cadena_octal):
    cadena_decimal=str(int(cadena_octal,8))
    return cadena_decimal

def convertirAHexadecimal(cadena_octal):
    cadena_hexadecimal=str(hex(int(cadena_octal,8)))
    return cadena_hexadecimal