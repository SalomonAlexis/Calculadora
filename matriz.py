import random

class Matriz:
    # Constructor/inicializador
    def __init__(self, row: int, column: int) -> None:
        self._matriz = [[0] * column for _ in range(row)]


    # Setters, getters y deleters
    @property
    def matriz(self) -> list[list[int | float | complex]]:
        return self._matriz
    

    @matriz.setter
    def matriz(self, una_lista: list[list[int | float | complex]]) -> None:  # La matriz propiamente dicha se guarda como una lista de listas -> un vector de vectores.
        self._matriz = una_lista


    '''
    def agregar_vector(self, vector_string: str) -> None:
        pass
    '''

    @staticmethod
    def string_a_vector(vector_string: str) -> list[int | float | complex]:
        vector = vector_string.split(" ")
        n = len(vector)

        for i in range(n):
            vector[i] = int(vector[i]) if Matriz.es_entero(vector[i]) else float(vector[i])

        return vector
    

    @staticmethod
    def es_entero(valor: int | float) -> bool:
        '''
        Retorna Verdadero si el número es un entero.
        Se usa para mostrar la matriz un poco mas prolija.
        '''
        return (abs(round(valor, 4))) - abs(int(round(valor, 4))) == 0


    # Métodos mágicos
    def __str__(self) -> str:
        n = self.filas()
        m = self.columnas()

        n_digitos_redondeo = 3
        h_mayor = self.max_digit(n_digitos_redondeo)
        mensaje = ''

        for i in range(n):
            for j in range(m):
                mensaje += " "

                h = len(str(round(self.matriz[i][j], n_digitos_redondeo)))  # Determina el número de dígitos del elemento ij de la matriz.
                for k in range(h_mayor-h):
                    mensaje += " "

                mensaje += str(round(self.matriz[i][j], n_digitos_redondeo))
                mensaje += " "
            mensaje += "\n"

        return mensaje


    def __add__(self, otra_matriz: 'Matriz') -> 'Matriz':
        if self.suma_es_conformable_con(otra_matriz):
            suma = Matriz(self.filas(), self.columnas())

            for i in range(self.filas()):
                for j in range(self.columnas()):
                    suma.matriz[i][j] = self.matriz[i][j] + otra_matriz.matriz[i][j]
        else:
            suma = None

        return suma
    

    def __sub__(self, otra_matriz: 'Matriz') -> 'Matriz':
        if self.suma_es_conformable_con(otra_matriz):
            suma = Matriz(self.filas(), self.columnas())

            for i in range(self.filas()):
                for j in range(self.columnas()):
                    suma.matriz[i][j] = self.matriz[i][j] - otra_matriz.matriz[i][j]
        else:
            suma = None

        return suma
    
    
    def __mul__(self, otra_matriz: 'Matriz') -> 'Matriz':
        resultado = None

        if type(otra_matriz) == type(int()) or type(otra_matriz) == type(float()):
            resultado = Matriz(self.filas(), self.columnas())
            k = otra_matriz
            resultado = self.producto_escalar(k)

        elif type(otra_matriz) == type(Matriz(1,1)):
            if self.producto_es_conformable_con(otra_matriz):
                resultado = self.producto_matricial(otra_matriz)

        return resultado
    

    def __rmul__(self, otra_matriz: 'Matriz') -> 'Matriz':
        resultado = None

        if type(otra_matriz) == type(int()) or type(otra_matriz) == type(float()):
            resultado = Matriz(self.filas(), self.columnas())
            k = otra_matriz
            resultado = self.producto_escalar(k)

        return resultado
    

    def __pow__(self, exponente: int) -> 'Matriz':
        resultado = None

        if self.es_cuadrada():
            resultado = self.copiar()

            for i in range(1, exponente):
                resultado *= self

        return resultado


    def __eq__(self, otra_matriz: 'Matriz') -> bool:
        flag = True

        if self.tiene_igual_tamaño_que(otra_matriz):
            n = self.filas()
            m = self.columnas()
            
            for i in range(n):
                for j in range(m):
                    if self.matriz[i][j] != otra_matriz.matriz[i][j]:
                        flag = False
                        break 
        else:
            flag = False

        return flag


    # Métodos regulares booleanos
    def tiene_igual_tamaño_que(self, otra_matriz: 'Matriz') -> bool:
        return self.filas() == otra_matriz.filas() and self.columnas() == otra_matriz.columnas()


    def es_cuadrada(self) -> bool:
        return self.filas() == self.columnas()
    

    def producto_es_conformable_con(self, otra_matriz: 'Matriz') -> bool:
        return self.columnas() == otra_matriz.filas()
    

    def suma_es_conformable_con(self, otra_matriz: 'Matriz') -> bool:
        return self.filas() == otra_matriz.filas() and self.columnas() == otra_matriz.columnas()
    

    def es_ortogonal(self) -> bool:
        matriz_inversa = self.inversa()
        matriz_transpuesta = self.transpuesta()

        return matriz_inversa == matriz_transpuesta


    # Métodos regulares
    def filas(self) -> int:
        return len(self.matriz)
    

    def columnas(self) -> int:
        return len(self.matriz[0])


    def submatriz(self, i_pivot: int, j_pivot: int) -> 'Matriz':
        '''
        Devuelve una matriz de orden n-1 a partir de otra de orden n...
        '''

        n = self.filas()
        m = self.columnas()

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
        '''
        Incompleto
        '''

        rango = None

        if self.es_cuadrada() and self.determinante != 0:
            rango = self.filas()
    
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

                    # Verifica si el elemento seleccionado es cero para evitar realizar llamadas sucesivas...
                    if self.matriz[0][j] != 0:
                        valor_determinante += self.matriz[0][j] * (-1)**(1 + (j+1)) * submatriz.determinante()
                    else:
                        valor_determinante += 0

        return valor_determinante


    def producto_escalar(self, k: int) -> 'Matriz':
        resultado = Matriz(self.filas(), self.columnas())

        for i in range(self.filas()):
                for j in range(self.columnas()):
                    resultado.matriz[i][j] = self.matriz[i][j] * k

        return resultado
    

    def producto_matricial(self, otra_matriz: 'Matriz') -> 'Matriz':
        resultado = None

        if self.producto_es_conformable_con(otra_matriz):
            resultado = Matriz(self.filas(), otra_matriz.columnas())

            for i in range(resultado.filas()):
                for j in range(resultado.columnas()):
                    for k in range(otra_matriz.filas()):
                        resultado.matriz[i][j] += self.matriz[i][k] * otra_matriz.matriz[k][j]

        return resultado
    

    def transpuesta(self) -> 'Matriz':
        resultado = Matriz(self.filas(), self.columnas())

        for i in range(self.filas()):
            for j in range(self.columnas()):
                resultado.matriz[i][j] = self.matriz[j][i]

        return resultado
    

    def transponer(self) -> None:
        transpuesta = self.transpuesta()
        self.matriz = transpuesta.matriz


    def copiar(self) -> 'Matriz':
        '''
        Devuelve una copia de la matriz.
        '''
        n = self.filas()
        m = self.columnas()

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
            n = self.filas()
            m = self.filas()

            matriz_inicial = self.copiar()
            matriz_inversa = Matriz.identidad(n)

            # Recorro la matriz por columnas. Ignoro los elementos de la diagonal principal.
            # Aplico misma operación a ambas matrices.
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


    def escalonada(self) -> 'Matriz':
        matriz_escalonada = None
        
        if self.es_cuadrada():
            n = self.filas()
            m = self.filas()

            matriz_escalonada = self.copiar()

            # Recorro la matriz por columnas. Ignoro los elementos de la diagonal principal.
            for j in range(n):
                for i in range(m):
                    if i > j:
                        if matriz_escalonada.matriz[j][j] != 0:
                            k = (-1) * matriz_escalonada.matriz[i][j] / matriz_escalonada.matriz[j][j]
                            matriz_escalonada.sumar_multiplo_a_fila(i, j, k)

            '''
            # Opero sobre los elementos de la diagonal principal que faltaron.
            # Los demás elementos se ignoran ya que valen 0.
            for i in range(n):
                k = 1 / matriz_inicial.matriz[i][i]
                matriz_inicial.multiplicar_fila(k, i)
            '''
            
        return matriz_escalonada
    

    def escalonar(self) -> None:
        escalonada = self.escalonada()
        self.matriz = escalonada.matriz


    @classmethod
    def nula(cls, n: int, m: int) -> 'Matriz':
        matriz_nula = cls(n, m)
        '''
        for i in range(n):
            for j in range(m):
                matriz_nula.matriz[i][j] = 0
        '''
        return matriz_nula


    @classmethod
    def identidad(cls, n: int) -> 'Matriz':
        matriz_identidad = cls(n, n)

        for i in range(n):
            matriz_identidad.matriz[i][i] = 1

        return matriz_identidad


    @classmethod
    def random(cls, n: int, m: int) -> 'Matriz':
        matriz_random = cls(n, m)

        for i in range(n):
            for j in range(m):
                matriz_random.matriz[i][j] = random.randint(0, 9)

        return matriz_random
    

    def ingresar_matriz(self) -> None:
        n = self.filas()
        m = self.columnas()

        for i in range(n):
            for j in range(m):
                valor = float(input(f'Ingrese el elemento {i+1}{j+1}: '))
                self.matriz[i][j] = valor
    

    def max_digit(self, n_digitos_redondeo: int=3) -> int:
        '''
        Devuelve el número de dígitos del elemento de la matriz que tenga más dígitos.
        '''
        self.emprolijar()

        n = len(self.matriz)  # Número de filas
        m = len(self.matriz[0]) # Número de columnas

        mayor = None

        for i in range(n):
            for j in range(m):
                if mayor is None or len(str(round(self.matriz[i][j], n_digitos_redondeo))) > mayor:
                    mayor = len(str(round(self.matriz[i][j], n_digitos_redondeo)))

        return mayor
    

    def emprolijar(self) -> None:
        n = self.filas()
        m = self.columnas()
        
        for i in range(n):
            for j in range(m):
                if self.es_entero(self.matriz[i][j]):
                    self.matriz[i][j] = int(round(self.matriz[i][j], 0))
