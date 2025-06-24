#1) Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa función para calcular y mostrar en pantalla
#   el factorial de todos los números enteros entre 1 y el número que indique el usuario

# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     return n * factorial(n - 1)
# num = int(input("Ingrese un número entero mayor o igual a 1: "))
# for i in range(1, num + 1):
#     print(f"Factorial de {i} es {factorial(i)}")

#########################################################################################################################
#########################################################################################################################

#2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición
#   indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario especifique.

# def fibonacci(n):
#     if n == 0:
#        return 0
#     elif n == 1:
#         return 1
#     return fibonacci(n - 1) + fibonacci(n - 2)

# pos = int(input("Ingrese una posición (entero mayor o igual a 0): "))

# print(f"Serie de Fibonacci hasta la posición {pos}:")
# for i in range(pos + 1):
#     print(fibonacci(i), end=" ")

#########################################################################################################################
#########################################################################################################################

#3) Crea una función recursiva que calcule la potencia de un número base elevado a un exponente, utilizando la fórmula 𝑛
#   𝑚 = 𝑛 ∗ 𝑛 (𝑚−1). Prueba esta función en un algoritmo general.

#def potencia(base, exponente):
#    if exponente == 0:
#        return 1
#    return base * potencia(base, exponente - 1)

#base = int(input("Ingrese la base: "))
#exponente = int(input("Ingrese el exponente (entero no negativo): "))

#resultado = potencia(base, exponente)
#print(f"{base} elevado a la {exponente} es: {resultado}")

#########################################################################################################################
#########################################################################################################################

#4) Crear una función recursiva en Python que reciba un número entero positivo en base decimal y devuelva su representación en binario como una cadena de texto.

#def decimal_a_binario(n):
#    if n == 0:
#        return ""
#    else:
#        return decimal_a_binario(n // 2) + str(n % 2)
    
#num = int(input("Ingrese un número entero positivo: "))

#if num == 0:
#    print("El binario de 0 es: 0")
#elif num > 0:
#    binario = decimal_a_binario(num)
#    print(f"El número {num} en binario es: {binario}")
#else:
#    print("Por favor, ingrese un número entero positivo.")

#########################################################################################################################
#########################################################################################################################
#5) Implementá una función recursiva llamada es_palindromo(palabra) que reciba una cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no lo es.

#def es_palindromo(palabra):
#    if len(palabra) <= 1:
#        return True
#    if palabra[0] != palabra[-1]:
#        return False
#    return es_palindromo(palabra[1:-1])

#texto = input("Ingrese una palabra (sin espacios ni tildes): ").lower()

#if es_palindromo(texto):
#    print(f"'{texto}' es un palíndromo.")
#else:
#    print(f"'{texto}' no es un palíndromo.")

#########################################################################################################################
#########################################################################################################################

#6) Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un número entero positivo y devuelva la suma de todos sus dígitos.

#def suma_digitos(n):
#    if n < 10:
#        return n
#    else:
#        return n % 10 + suma_digitos(n // 10)
#numero = int(input("Ingrese un número entero positivo: "))

#if numero >= 0:
#    resultado = suma_digitos(numero)
#    print(f"La suma de los dígitos de {numero} es: {resultado}")
#else:
#    print("Error: debe ingresar un número entero positivo.")

#########################################################################################################################
#########################################################################################################################

#7) Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n bloques, en el siguiente nivel uno
# menos (n - 1), y así sucesivamente hasta llegar al último nivel con un solo bloque.

#def contar_bloques(n):
#    if n == 1:
#        return 1
#    else:
#        return n + contar_bloques(n - 1)
#nivel = int(input("Ingrese el número de bloques en el nivel más bajo: "))

#if nivel >= 1:
#    total = contar_bloques(nivel)
#    print(f"Total de bloques necesarios: {total}")
#else:
#    print("Debe ingresar un número entero positivo mayor o igual a 1.")

#########################################################################################################################
#########################################################################################################################

#8) Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un número entero positivo (numero) y un
# dígito (entre 0 y 9), y devuelva cuántas veces aparece ese dígito dentro del número.

def contar_digito(numero, digito):
    if numero == 0:
        return 0
    ultimo = numero % 10
    if ultimo == digito:
        return 1 + contar_digito(numero // 10, digito)
    else:
        return contar_digito(numero // 10, digito)

num = int(input("Ingrese un número entero positivo: "))
d = int(input("Ingrese un dígito (0-9): "))

if num >= 0 and 0 <= d <= 9:
    cantidad = contar_digito(num, d)
    print(f"El dígito {d} aparece {cantidad} veces en {num}.")
else:
    print("Entrada inválida.")