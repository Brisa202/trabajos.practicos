# Ejercicio 1: Contar la cantidad de dígitos de un número entero
# Dado un número entero positivo, contar cuántos dígitos tiene.

def contar_digitos_entero(n):
    contador = 0
    while n > 0:
        n = n // 10  # Elimina el último dígito
        contador += 1
    return contador

# Prueba del ejercicio 1
numero = int(input("Ingresa un número entero positivo: "))
print("Cantidad de dígitos:", contar_digitos_entero(numero))

# Ejercicio 2: Contar los dígitos en la parte entera y decimal de un número
# Dado un número decimal, contar cuántos dígitos tiene en la parte entera y en la parte decimal.

def contar_digitos_decimal(n):
    parte_entera = int(n)  # Extrae la parte entera
    parte_decimal = n - parte_entera  # Extrae la parte decimal
    
    # Contar los dígitos de la parte entera
    digitos_entera = 0
    if parte_entera == 0:
        digitos_entera = 1
    else:
        while parte_entera > 0:
            parte_entera = parte_entera // 10
            digitos_entera += 1

    # Contar los dígitos de la parte decimal
    digitos_decimal = 0
    while parte_decimal > 0:
        parte_decimal *= 10
        digito = int(parte_decimal)
        parte_decimal -= digito
        digitos_decimal += 1

    return digitos_entera, digitos_decimal

# Prueba del ejercicio 2
numero_decimal = float(input("Ingresa un número decimal: "))
parte_entera, parte_decimal = contar_digitos_decimal(numero_decimal)
print("Dígitos en parte entera:", parte_entera, "Dígitos en parte decimal:", parte_decimal)

# Ejercicio 3: Determinar los números compuestos en una lista
# Dada una lista de números, devolver los que sean compuestos.
# Un número compuesto tiene más de dos divisores.

def es_compuesto(n):
    if n < 2:
        return False  # Los números menores que 2 no son compuestos
    divisores = 0
    i = 1
    while i <= n:
        if n % i == 0:
            divisores += 1
        i += 1
    return divisores > 2  # Si tiene más de 2 divisores, es compuesto

def numeros_compuestos(lista):
    resultado = []
    i = 0
    while i < len(lista):
        if es_compuesto(lista[i]):
            resultado.append(lista[i])
        i += 1
    return resultado

# Prueba del ejercicio 3
lista_numeros = [4, 7, 9, 10, 13, 15, 17, 20]
print("Números compuestos:", numeros_compuestos(lista_numeros))

#Ejercicio 4:Dado un vector con N dígitos, invertir sus elementos considerando lo siguiente:
#Usando un vector auxiliar

def invertir_con_auxiliar(lista):
    aux = []  # Lista auxiliar vacía
    for i in range(len(lista) - 1, -1, -1):  # Recorremos la lista de atrás hacia adelante
        aux.append(lista[i])  # Agregamos los elementos a la nueva lista
    return aux

# Ejemplo de uso
numeros = [1, 2, 3, 4, 5]
invertidos = invertir_con_auxiliar(numeros)
print(invertidos)  # Salida: [5, 4, 3, 2, 1]

#Sin usar una lista auxiliar
def invertir_sin_auxiliar(lista):
    n = len(lista)
    for i in range(n // 2):  # Recorremos solo la mitad de la lista
        lista[i], lista[n - 1 - i] = lista[n - 1 - i], lista[i]  # Intercambiamos los elementos
    return lista

# Ejemplo de uso
numeros = [1, 2, 3, 4, 5]
invertidos = invertir_sin_auxiliar(numeros)
print(invertidos)  # Salida: [5, 4, 3, 2, 1]

#Ejericio 5:Dada una lista A de N números reales, crear y mostrar una lista B con aquellos elementos de A que en su parte entera tenga:
#Exactamente dos dígitos pares.
#Al menos dos dígitos impares.
# Función para contar la cantidad de dígitos pares e impares en la parte entera de un número
def contar_pares_impares(numero):
    pares = 0  # Contador de dígitos pares
    impares = 0  # Contador de dígitos impares
    numero = abs(int(numero))  # Tomamos solo la parte entera y positiva del número

    # Mientras el número tenga dígitos
    while numero > 0:
        digito = numero % 10  # Obtenemos el último dígito
        if digito % 2 == 0:  # Si el dígito es par
            pares += 1
        else:  # Si el dígito es impar
            impares += 1
        numero //= 10  # Eliminamos el último dígito dividiendo entre 10

    return pares, impares  # Retornamos la cantidad de pares e impares

# Función para filtrar los números de la lista A y crear la lista B
def filtrar_lista(A):
    B = []  # Lista resultante

    for num in A:  # Recorremos cada número en la lista A
        pares, impares = contar_pares_impares(num)  # Contamos los dígitos pares e impares
        if pares == 2 or impares >= 2:  # Si cumple alguna de las condiciones
            B.append(num)  # Agregamos el número a la lista B

    return B  # Retornamos la lista filtrada

# Solicitar al usuario que ingrese la lista de números reales separados por espacios
A = list(map(float, input("Ingresa los números de la lista separados por espacios: ").split()))

# Aplicamos la función
B = filtrar_lista(A)

# Mostrar la lista resultante
print("Lista filtrada:", B)



#Ejercicio6:Dada una lista N de números enteros y un número entero K, insertar K a la derecha de cada múltiplo de K.
#Ejemplo: [5, 12, 35, 67, 8, 16, 1, 13] K=4 ➔ [5, 12, 4, 35, 67, 8, 4, 16, 4, 1, 13]

# Función para insertar K a la derecha de cada múltiplo de K
def insertar_despues_de_multiplos(N, K):
    resultado = []  # Lista para almacenar el resultado

    for num in N:  # Recorremos cada número en la lista N
        resultado.append(num)  # Agregamos el número original a la lista
        if num % K == 0:  # Si el número es múltiplo de K
            resultado.append(K)  # Insertamos K después del número

    return resultado  # Retornamos la lista modificada

# Entrada de la lista N desde el usuario
N = list(map(int, input("Ingresa los números de la lista separados por espacios: ").split()))

# Entrada del número K
K = int(input("Ingresa el número K: "))

# Aplicamos la función
N_modificada = insertar_despues_de_multiplos(N, K)

# Mostramos la lista resultante
print("Lista modificada:", N_modificada)
