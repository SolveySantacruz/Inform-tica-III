"""
 El modulo decimal contiene las siguientes funciones:
            convertirABinario     => recibe string (cadena_decimal), retorna string (cadena_binario)
            convertirAOctal       => recibe string (cadena_decimal), retorna string (cadena_octal)
            convertirAHexadecimal => recibe string (cadena_decimal), retorna string (cadena_hexadecimal)
"""

def convertirABinario(cadena_decimal):
    cadena_binario=str(bin(int(cadena_decimal)))
    return cadena_binario
    
def convertirAOctal(cadena_decimal):
    cadena_octal=str(oct(int(cadena_decimal)))
    return cadena_octal

def convertirAHexadecimal(cadena_decimal):
    cadena_hexadecimal=str(hex(int(cadena_decimal)))
    return cadena_hexadecimal