'''
Calculadora para operar matrices

Autor: Alexis Salomón
'''
from matriz import Matriz

def main():
    pass


def test():
    matriz = Matriz(3, 3)
    matriz.matriz = [[3, 0, 1],
                     [0, 5, 0],
                     [-1, 1, -1]]
    
    print(matriz)
    matriz.invertir()
    matriz.invertir()

    print(matriz)


if __name__ == '__main__':
    test()
    