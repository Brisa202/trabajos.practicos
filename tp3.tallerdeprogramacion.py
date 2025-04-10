#EJERCICIO 1 Crear un programa que determine el valor máximo entre tres números.
#¿Cuántas funciones y/o procedimientos son necesarios? ¿Cuántos parámetros?
def maximo_de_tres(a, b, c):
    if a >= b and a >= c:
        return a
    else:
        if b >= a and b >= c:
            return b
        else:
            return c

# Probamos la función
n1 = int(input("Ingrese el primer número: "))
n2 = int(input("Ingrese el segundo número: "))
n3 = int(input("Ingrese el tercer número: "))

mayor = maximo_de_tres(n1, n2, n3)
print("El número mayor es:", mayor)

#EJERCICIO 2 Crear un programa que determine el valor máximo entre 10 números utilizando las funciones del ejercicio anterior.

# Función para comparar tres números (sin elif)
def maximo_de_tres(a, b, c):
    if a >= b and a >= c:
        return a
    else:
        if b >= a and b >= c:
            return b
        else:
            return c

# Función para encontrar el mayor de una lista de 10 números
def maximo_de_diez(lista):
    mayor = lista[0]  # Empezamos suponiendo que el primero es el mayor

    for numero in lista[1:]:  # Recorremos del segundo al último
        # Comparamos de a 2 usando maximo_de_tres, usando el número actual y el "mayor"
        mayor = maximo_de_tres(mayor, numero, numero)  # el tercer parámetro se repite para que funcione la función
    return mayor

# Cargar los 10 números desde teclado
numeros = []
for i in range(10):
    num = int(input(f"Ingrese el número {i+1}: "))
    numeros.append(num)

# Buscar el máximo
resultado = maximo_de_diez(numeros)

# Mostrar resultado
print("El número mayor entre los 10 es:", resultado)

#EJERCICIO 3 Crear un programa que:
#a) Cargue dos vectores A y B, con N y M números enteros respectivamente
#b) Calcule la suma de los números cargados en cada vector
#c) Si N y M son iguales, realice la suma de los vectores (elemento a elemento) y muestre el vector resultante
#¿Cuántas funciones y/o procedimientos son necesarios?

# Función para cargar un vector con N números
def cargar_vector(cantidad):
    vector = []
    for i in range(cantidad):
        num = int(input(f"Ingrese el número {i+1}: "))
        vector.append(num)
    return vector

# Función para sumar todos los elementos de un vector
def sumar_vector(vector):
    suma = 0
    for num in vector:
        suma += num
    return suma

# Función para sumar los elementos entre dos vectores (posición por posición)
def sumar_vectores_elemento_a_elemento(v1, v2):
    resultado = []
    for i in range(len(v1)):
        suma = v1[i] + v2[i]
        resultado.append(suma)
    return resultado

# --------- PROGRAMA PRINCIPAL ---------

# Cargar cantidad de elementos de cada vector
n = int(input("¿Cuántos números tendrá el vector A? "))
m = int(input("¿Cuántos números tendrá el vector B? "))

# Cargar los vectores
print("\n--- Cargando vector A ---")
vectorA = cargar_vector(n)

print("\n--- Cargando vector B ---")
vectorB = cargar_vector(m)

# Calcular la suma de cada vector
sumaA = sumar_vector(vectorA)
sumaB = sumar_vector(vectorB)

# Mostrar resultados
print("\nSuma de los elementos del vector A:", sumaA)
print("Suma de los elementos del vector B:", sumaB)

# Si N y M son iguales, sumar los vectores elemento a elemento
if n == m:
    vector_resultante = sumar_vectores_elemento_a_elemento(vectorA, vectorB)
    print("\nSuma de los vectores A + B (elemento a elemento):", vector_resultante)
else:
    print("\nLos vectores tienen distinta cantidad de elementos, no se pueden sumar elemento a elemento.")

#EJERCICIO 4 Crear un programa que cargue una o más oraciones y luego indique la suma total de vocales y consonantes:
#Crear dos funciones, una para contar las vocales y otra para contar las consonantes que tiene cada palabra.
#Cada función tomará como parámetro una palabra.
#En el programa principal mostrar la cantidad total de vocales y la cantidad total de consonantes en el texto de
#entrada.


# Función que cuenta las vocales en una palabra
def contar_vocales(palabra):
    vocales = "aeiouAEIOU"
    cantidad = 0
    for letra in palabra:
        if letra in vocales:
            cantidad += 1
    return cantidad

# Función que cuenta las consonantes en una palabra
def contar_consonantes(palabra):
    vocales = "aeiouAEIOU"
    cantidad = 0
    for letra in palabra:
        # Verificamos que sea una letra y que no sea vocal
        if letra.isalpha() and letra not in vocales:
            cantidad += 1
    return cantidad

# ---------------------- PROGRAMA PRINCIPAL ----------------------

# Pedimos al usuario que ingrese una o más oraciones
oracion = input("Ingrese una o más oraciones: ")

# Separamos las oraciones en palabras
palabras = oracion.split()

# Inicializamos los contadores de totales
total_vocales = 0
total_consonantes = 0

# Recorremos cada palabra para aplicar las funciones
for palabra in palabras:
    total_vocales += contar_vocales(palabra)
    total_consonantes += contar_consonantes(palabra)

# Mostramos los resultados finales
print("\nCantidad total de vocales:", total_vocales)
print("Cantidad total de consonantes:", total_consonantes)

#EJERCICIO 5 Crear un programa que contenga un menú con las siguientes opciones:
#Calcular la potencia K de un número X.
#Obtener la cantidad de dígitos de un número X.
#Determinar si un número es capicúa.
#Implementar funciones para cada opción del menú.
# Función para calcular la potencia

def calcular_potencia(base, exponente):
    return base ** exponente

# Función para contar los dígitos de un número
def contar_digitos(numero):
    return len(str(abs(numero)))  # abs() para manejar negativos

# Función para verificar si un número es capicúa
def es_capicua(numero):
    numero_str = str(abs(numero))
    return numero_str == numero_str[::-1]

# -------------------- PROGRAMA PRINCIPAL --------------------

# Mostramos el menú
print("=== MENÚ ===")
print("1. Calcular la potencia K de un número X")
print("2. Obtener la cantidad de dígitos de un número X")
print("3. Determinar si un número es capicúa")

# Pedimos la opción al usuario
opcion = input("Elija una opción (1, 2 o 3): ")

# Ejecutamos la opción correspondiente
if opcion == "1":
    x = int(input("Ingrese el número base X: "))
    k = int(input("Ingrese el exponente K: "))
    resultado = calcular_potencia(x, k)
    print("Resultado:", resultado)

if opcion == "2":
    x = int(input("Ingrese el número X: "))
    cantidad = contar_digitos(x)
    print("Cantidad de dígitos:", cantidad)

if opcion == "3":
    x = int(input("Ingrese el número X: "))
    if es_capicua(x):
        print("El número es capicúa")
    else:
        print("El número NO es capicúa")

#EJERCICIO 6 Escriba un programa que para dos matrices A y B de números enteros de dimensiones MxN, realice la suma o el
#producto de las matrices (a elección del usuario) y las cargue en otra matriz C.
#Utilizar funciones y/o procedimientos para:
#cargar las matrices
#realizar la suma
#realizar el producto
#mostrar en pantalla una matriz
#Invóquelas adecuadamente.

# Función para cargar una matriz con M filas y N columnas
def cargar_matriz(nombre):
    m = int(input(f"Ingrese la cantidad de filas para la matriz {nombre}: "))
    n = int(input(f"Ingrese la cantidad de columnas para la matriz {nombre}: "))
    matriz = []

    for i in range(m):
        fila = []
        print(f"Ingrese los elementos de la fila {i+1} de la matriz {nombre}:")
        for j in range(n):
            valor = int(input(f"Elemento [{i}][{j}]: "))
            fila.append(valor)
        matriz.append(fila)

    return matriz

# Función para sumar dos matrices
def sumar_matrices(matriz_a, matriz_b):
    m = len(matriz_a)
    n = len(matriz_a[0])
    matriz_resultado = []

    for i in range(m):
        fila = []
        for j in range(n):
            suma = matriz_a[i][j] + matriz_b[i][j]
            fila.append(suma)
        matriz_resultado.append(fila)

    return matriz_resultado

# Función para multiplicar dos matrices
def multiplicar_matrices(matriz_a, matriz_b):
    m = len(matriz_a)
    n = len(matriz_a[0])
    matriz_resultado = []

    for i in range(m):
        fila = []
        for j in range(n):
            producto = matriz_a[i][j] * matriz_b[i][j]
            fila.append(producto)
        matriz_resultado.append(fila)

    return matriz_resultado

# Función para mostrar una matriz
def mostrar_matriz(matriz):
    print("Matriz resultante:")
    for fila in matriz:
        print(fila)

# ----------------- PROGRAMA PRINCIPAL -----------------

# Cargar matrices A y B
matriz_a = cargar_matriz("A")
matriz_b = cargar_matriz("B")

# Verificamos si tienen las mismas dimensiones
if len(matriz_a) == len(matriz_b) and len(matriz_a[0]) == len(matriz_b[0]):
    print("\n¿Qué operación desea realizar?")
    print("1. Sumar matrices")
    print("2. Multiplicar matrices")
    opcion = input("Ingrese 1 o 2: ")

    if opcion == "1":
        matriz_c = sumar_matrices(matriz_a, matriz_b)
        mostrar_matriz(matriz_c)
    elif opcion == "2":
        matriz_c = multiplicar_matrices(matriz_a, matriz_b)
        mostrar_matriz(matriz_c)
    else:
        print("Opción inválida.")
else:
    print("Las matrices no tienen las mismas dimensiones. No se puede operar.")
