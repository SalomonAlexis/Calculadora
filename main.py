'''
Calculadora para operar matrices

Autor: Alexis Salomón
'''
from matriz import Matriz

def main():
    pass


def test():
    matriz = Matriz(3, 3)
    matriz.matriz = [[-2, -3, -2], [1, 3, -2], [-1, -6, 4]]
    print(matriz)

    matriz.invertir()
    print(matriz)



if __name__ == '__main__':
    test()
    