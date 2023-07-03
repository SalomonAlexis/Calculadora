'''
Calculadora para operar matrices

Autor: Alexis Salomón
'''
from matriz import Matriz

def main():
    pass


def test():
    matriz_a = Matriz(3, 3)
    matriz_b = Matriz(3, 3)
    matriz_c = Matriz.identidad(3)
    matriz_d = Matriz.identidad(4)

    print(matriz_a != matriz_b)
    print(matriz_a != matriz_c)
    print(matriz_a != matriz_d)


if __name__ == '__main__':
    test()
    