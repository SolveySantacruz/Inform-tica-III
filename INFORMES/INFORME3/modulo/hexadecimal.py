"""
El modulo Hexadecimal debe tener las siguientes funciones:
            convertirABinario => recibe string (cadena_hexadecimal), retorna string (cadena_binario)
            convertirADecimal => recibe string (cadena_hexadecimal), retorna string (cadena_decimal)
            convertirAOctal   => recibe string (cadena_hexadecimal), retorna string (cadena_Octal)
"""

def convertirABinario(cadena_hexadecimal):
    cadena_binario=str(bin(int(cadena_hexadecimal,16)))
    return cadena_binario

def convertirADecimal(cadena_hexadecimal):
    cadena_decimal=str(int(cadena_hexadecimal,16))
    return cadena_decimal

def convertirAOctal(cadena_hexadecimal):
    cadena_octal=str(oct(int(cadena_hexadecimal,16)))
    return cadena_octal