'''
Calculadora para operar matrices

Autor: Alexis Salomón
'''
from matriz import Matriz

def main():
    pass


def test():
    matriz_a = Matriz(3, 3)
    matriz_a.matriz = [[1, 1, 1, 1], [2, 5, -1, 2], [3, 1, 1, 3], [4, 4, 4, 4]]
    print(matriz_a)

    matriz_a.escalonar()
    print(matriz_a)



if __name__ == '__main__':
    test()
    