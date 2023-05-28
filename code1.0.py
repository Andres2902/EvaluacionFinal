import sys


def obtener_ascii(palabra):
    valores_ascii = []
    for caracter in palabra:
        valores_ascii.append(ord(caracter))
    return valores_ascii


def obtener_binario(palabra):
    valores_binarios = []
    for caracter in palabra:
        valores_binarios.append(bin(ord(caracter))[2:])
    return valores_binarios


def obtener_resultados(palabra):
    valores_ascii = obtener_ascii(palabra)
    valores_binarios = obtener_binario(palabra)
    return {'ascii': valores_ascii, 'binario': valores_binarios}


menu = int(input('Menú\n=====\n1. Carácter\n2. Palabra'))

if menu == 1:
    caracter = input('Ingresa un carácter: ')
    palabra = caracter
    tipo = "carácter"
elif menu == 2:
    palabra = input('Ingresa una palabra: ')
    tipo = "palabra"
    caracter = palabra  # Utilizar la palabra completa como el valor de caracter
else:
    sys.exit()

print('Resultados\n===========')

resultados = obtener_resultados(palabra)
print('El código ASCII de "{0}" {1} es: {2}'.format(
    caracter, tipo, resultados['ascii']))
print('En código binario de "{0}" es: {1}'.format(
    caracter, resultados['binario']))
