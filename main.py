'''
Calculadora para operar matrices

Autor: Alexis Salomón
'''
from matriz import Matriz

def main():
    pass


def test():
    matriz = Matriz(3, 3)
    matriz.matriz = [[2, -4, 5], [3, -1, 2], [4, 1, 6]]
    print(matriz)

    matriz.invertir()
    print(matriz)



if __name__ == '__main__':
    test()
    