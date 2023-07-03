import random

class Matriz:
    # Constructor
    def __init__(self, row: int, column: int) -> None:
        self._row = row
        self._column = column
        self._matriz = [[0] * column for _ in range(row)]

    # Setters, getters y deleters
    @property
    def row(self) -> int:
        return self._row
    

    @row.setter
    def row(self, numero_filas: int) -> None:
        self._row = numero_filas


    @property
    def column(self) -> int:
        return self._column
    

    @column.setter
    def column(self, numero_columnas: int) -> None:
        self._column = numero_columnas


    @property
    def matriz(self) -> list[list[int]]:
        return self._matriz
    

    @matriz.setter
    def matriz(self, una_lista: list[list[int]]):  # La matriz propiamente dicha se guarda como una lista de listas -> un vector de vectores.
        self._matriz = una_lista


    # Métodos mágicos
    def __str__(self) -> str:
        n = len(self.matriz)
        m = len(self.matriz[0])
        h_mayor = self.max_digit()

        mensaje = ''

        for i in range(n):
            for j in range(m):
                mensaje += " "

                h = len(str(round(self.matriz[i][j], 2)))  # Determina el número de dígitos del elemento ij de la matriz.
                for k in range(h_mayor-h):
                    mensaje += " "

                mensaje += str(round(self.matriz[i][j], 2))
                mensaje += " "
            mensaje += "\n"

        return mensaje


    def __add__(self, matriz: 'Matriz') -> 'Matriz':
        if self.row == matriz.row and self.column == matriz.column:
            suma = Matriz(self.row, self.column)

            for i in range(self.row):
                for j in range(self.column):
                    suma.matriz[i][j] = self.matriz[i][j] + matriz.matriz[i][j]
        else:
            suma = None

        return suma
    

    def __sub__(self, otra_matriz: 'Matriz') -> 'Matriz':
        if self.suma_es_conformable_con(otra_matriz):
            suma = Matriz(self.row, self.column)

            for i in range(self.row):
                for j in range(self.column):
                    suma.matriz[i][j] = self.matriz[i][j] - otra_matriz.matriz[i][j]
        else:
            suma = None

        return suma
    
    
    def __mul__(self, otra_matriz: 'Matriz') -> 'Matriz':
        resultado = None

        if type(otra_matriz) == type(int()) or type(otra_matriz) == type(float()):
            resultado = Matriz(self.row, self.column)
            k = otra_matriz
            resultado = self.producto_escalar(k)

        elif type(otra_matriz) == type(Matriz(1,1)):
            if self.producto_es_conformable_con(otra_matriz):
                resultado = self.producto_matricial(otra_matriz)

        return resultado
    

    def __rmul__(self, otra_matriz: 'Matriz') -> 'Matriz':
        resultado = None

        if type(otra_matriz) == type(int()) or type(otra_matriz) == type(float()):
            resultado = Matriz(self.row, self.column)
            k = otra_matriz
            resultado = self.producto_escalar(k)

        return resultado


    def __eq__(self, otra_matriz: 'Matriz') -> bool:
        flag = True

        if self.tiene_igual_tamaño_que(otra_matriz):
            n = self.row
            m = self.column
            
            for i in range(n):
                for j in range(m):
                    if self.matriz[i][j] != otra_matriz.matriz[i][j]:
                        flag = False
                        break 
        else:
            flag = False

        return flag


    # Métodos regulares
    def tiene_igual_tamaño_que(self, otra_matriz: 'Matriz') -> bool:
        return self.row == otra_matriz.row and self.column == otra_matriz.column


    def es_cuadrada(self) -> bool:
        return self.row == self.column
    

    def producto_es_conformable_con(self, otra_matriz: 'Matriz') -> bool:
        return self.column == otra_matriz.row
    

    def suma_es_conformable_con(self, otra_matriz: 'Matriz') -> bool:
        return self.row == otra_matriz.row and self.column == otra_matriz.column
    

    def es_ortogonal(self) -> bool:
        matriz_inversa = self.inversa()
        matriz_transpuesta = self.transpuesta()

        return matriz_inversa == matriz_transpuesta


    def submatriz(self, i_pivot: int, j_pivot: int) -> 'Matriz':
        '''
        Devuelve una matriz de orden n-1 a partir de otra de orden n...
        '''

        n = self.row
        m = self.column

        submatriz = Matriz(n-1, m-1)
        r = 0
        c = 0

        for i in range(n):
            if i != i_pivot:
                for j in range(m):
                    if j != j_pivot:
                        submatriz.matriz[r][c] = self.matriz[i][j]
                        c = c + 1

                c = 0
                r = r + 1

        return submatriz


    def rango(self) -> int:
        rango = None
        if self.es_cuadrada():
            rango = self.row

        return rango


    def determinante(self) -> int:
        valor_determinante = 0
        rango = self.rango()

        if self.es_cuadrada():
            if self.rango() == 2:  # Caso base: Det(M(2))
                valor_determinante = self.matriz[0][0] * self.matriz[1][1] - self.matriz[0][1] * self.matriz[1][0]
            else:  # Caso recursivo: Det(M(n)) = C(1j) * Det(M(n-1))
                for j in range(rango):
                    submatriz = self.submatriz(0, j)
                    valor_determinante += self.matriz[0][j] * (-1)**(1 + (j+1)) * submatriz.determinante()

        return valor_determinante


    def producto_escalar(self, k: int) -> 'Matriz':
        resultado = Matriz(self.row, self.column)

        for i in range(self.row):
                for j in range(self.column):
                    resultado.matriz[i][j] = self.matriz[i][j] * k

        return resultado
    

    def producto_matricial(self, otra_matriz: 'Matriz') -> 'Matriz':
        resultado = None

        if self.producto_es_conformable_con(otra_matriz):
            resultado = Matriz(self.row, otra_matriz.column)

            for i in range(resultado.row):
                for j in range(resultado.column):
                    for k in range(otra_matriz.row):
                        resultado.matriz[i][j] += self.matriz[i][k] * otra_matriz.matriz[k][j]

        return resultado
    

    def transpuesta(self) -> 'Matriz':
        resultado = Matriz(self.row, self.column)

        for i in range(self.row):
            for j in range(self.column):
                resultado.matriz[i][j] = self.matriz[j][i]

        return resultado
    

    def transponer(self) -> None:
        transpuesta = self.transpuesta()
        self.matriz = transpuesta.matriz


    def copiar(self) -> 'Matriz':
        '''
        Devuelve una copia de la matriz.
        '''
        n = self.row
        m = self.column

        copia = Matriz(n, m)

        for i in range(n):
            for j in range(m):
                copia.matriz[i][j] = self.matriz[i][j]

        return copia
    

    def intercambiar_filas(self, i: int, j: int) -> None:
        self.matriz[i], self.matriz[j] = self.matriz[j], self.matriz[i]


    def multiplicar_fila(self, escalar: float, fila: int) -> None:
        if escalar != 0:
            n = len(self.matriz[fila])

            for j in range(n):
                self.matriz[fila][j] *= escalar


    def sumar_multiplo_a_fila(self, fila_destino: int, fila_origen: int, escalar: float) -> None:
        if escalar != 0:
            n = len(self.matriz[0])

            for j in range(n):
                self.matriz[fila_destino][j] += self.matriz[fila_origen][j] * escalar


    def inversa(self) -> 'Matriz':
        '''
        Devuelve la inversa de la matriz, aplicando operaciones elementales sucesivas.
        '''
        matriz_inversa = None

        if self.es_cuadrada() and self.determinante() != 0:
            n = self.row
            m = self.row

            matriz_inicial = self.copiar()
            matriz_inversa = Matriz.identidad(n)

            # Recorro la matriz por columnas. Ignoro los elementos de la diagonal principal.
            for j in range(n):
                for i in range(m):
                    if i != j:
                        k = (-1) * matriz_inicial.matriz[i][j] / matriz_inicial.matriz[j][j]
                        matriz_inicial.sumar_multiplo_a_fila(i, j, k)
                        matriz_inversa.sumar_multiplo_a_fila(i, j, k)

            # Opero sobre los elementos de la diagonal principal que faltaron.
            # Los demás elementos se ignoran ya que valen 0.
            for i in range(n):
                k = 1 / matriz_inicial.matriz[i][i]
                matriz_inicial.multiplicar_fila(k, i)
                matriz_inversa.multiplicar_fila(k, i)

        return matriz_inversa


    def invertir(self) -> None:
        '''
        Invierte la propia matriz.
        '''
        inversa = self.inversa()
        self.matriz = inversa.matriz


    @classmethod
    def nula(cls, n: int, m: int) -> 'Matriz':
        matriz_nula = cls(n, m)

        for i in range(n):
            for j in range(m):
                matriz_nula.matriz[i][j] = 0

        return matriz_nula


    @classmethod
    def identidad(cls, n: int) -> 'Matriz':
        matriz_identidad = cls(n, n)

        for i in range(n):
            for j in range(n):
                if i == j:
                    matriz_identidad.matriz[i][j] = 1
                else:
                    matriz_identidad.matriz[i][j] = 0

        return matriz_identidad


    @classmethod
    def random(cls, n: int, m: int) -> 'Matriz':
        matriz_random = cls(n, m)

        for i in range(n):
            for j in range(m):
                matriz_random.matriz[i][j] = random.randint(0, 9)

        return matriz_random
    

    def ingresar_matriz(self) -> None:
        n = self.row
        m = self.column

        for i in range(n):
            for j in range(m):
                valor = float(input(f'Ingrese el elemento {i+1}{j+1}: '))
                self.matriz[i][j] = valor
    

    def max_digit(self) -> int:
        '''
        Devuelve el número de dígitos del elemento de la matriz que tenga más dígitos.
        '''

        n = len(self.matriz)  # Número de filas
        m = len(self.matriz[0]) # Número de columnas

        mayor = None

        for i in range(n):
            for j in range(m):
                if mayor is None or len(str(round(self.matriz[i][j], 2))) > mayor:
                    mayor = len(str(round(self.matriz[i][j], 2)))

        return mayor
