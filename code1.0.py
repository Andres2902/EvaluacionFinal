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
