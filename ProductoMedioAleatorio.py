class GeneradorAleatorioProductoMedio:
    def __init__(self, semilla1, semilla2):
        self.semilla1 = semilla1
        self.semilla2 = semilla2

    def generar(self, num_numeros):
        numeros_aleatorios = []
        for _ in range(num_numeros):
            producto = self.semilla1 * self.semilla2
            str_producto = str(producto)
            
            while len(str_producto) < 2 * len(str(self.semilla1)):
                str_producto = '0' + str_producto

            indice_medio = len(str_producto) // 4
            digitos_medio = str_producto[indice_medio:indice_medio + len(str(self.semilla1))]
            
            nueva_semilla = int(digitos_medio)
            numeros_aleatorios.append(nueva_semilla / (10 ** len(str(self.semilla1))))
            
            self.semilla1 = self.semilla2
            self.semilla2 = nueva_semilla
        
        return numeros_aleatorios

# Asignamos el valor de las semillas
semilla1 = 12
semilla2 = 14

generador_aleatorio = GeneradorAleatorioProductoMedio(semilla1, semilla2)

# Generacion de números pseudoaleatorios
num_numeros = 10 # En este caso seleccionamos que sean 10 numeros los que se generen
numeros_aleatorios = generador_aleatorio.generar(num_numeros)

# Imprime los numeros por consola
for i, num in enumerate(numeros_aleatorios, start=1):
    print(f"Numero {i}: {num}")
