'''
Calculadora para operar matrices

Autor: Alexis Salomón
'''
from matriz import Matriz

def main():
    pass


def test():
    matriz = Matriz(15,15)
    matriz_b = Matriz.nula(16, 9)

    print(matriz)
    print(matriz_b)


if __name__ == '__main__':
    test()
    