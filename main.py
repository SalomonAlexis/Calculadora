'''
Calculadora para operar matrices

Autor: Alexis Salomón
'''
from matriz import Matriz

def main():
    pass


def test():
    matriz = Matriz.identidad(3)
    print(matriz)

    matriz.sumar_multiplo_a_fila(1, 0, 10)
    print(matriz)


test()
