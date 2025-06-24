#1. Crear una función llamada imprimir_hola_mundo que imprima por pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el programa principal.

#def imprimir_hola_mundo():
#    print ("hola mundo")

#imprimir_hola_mundo()


#########################################################################################################################
#########################################################################################################################

#2. Crear una función llamada saludar_usuario(nombre) que reciba como parámetro un nombre y devuelva un saludo personalizado.
#   Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver: “Hola Marcos!”. Llamar a esta función desde el programa
#   principal solicitando el nombre al usuario.

#def saludar_usuario(nombre):
#    return print(f"Hola  {nombre} !!!!")

#nombre_usuario = input("Ingresar nombre: ")
#print (saludar_usuario(nombre_usuario))




#########################################################################################################################
#########################################################################################################################

#3. Crear una función llamada informacion_personal(nombre, apellido, edad, residencia) que reciba cuatro parámetros e imprima: “Soy
#[nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pedir los datos al usuario y llamar a esta función con los valores ingresados.


#def informacion_personal(nombre, apellido, edad, residencia):
#    return print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

#Nombre_usu=input("Ingresar nombre: ")
#Apellido_usu=input("Ingresar Apellido: ")
#Edad_usu=input("Ingresas edad: ")
#residencia_usu=input("Ingresar residencia: ")

#informacion_personal(Nombre_usu,Apellido_usu,Edad_usu,residencia_usu)

#########################################################################################################################
#########################################################################################################################

#4. Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del círculo. calcular_perimetro_circulo(radio) que
#   reciba el radio como parámetro y devuelva el perímetro del círculo. Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados.

#import math

#def calcular_area_circulo(radio):
#    return math.pi * radio ** 2

#def calcular_perimetro_circulo(radio):
#    return 2 * math.pi * radio

#radio = float(input("Ingresá el radio del círculo: "))


#area = calcular_area_circulo(radio)
#perimetro = calcular_perimetro_circulo(radio)

#print(f"El área del círculo es:  {area} El perímetro del círculo es: {perimetro}")

#########################################################################################################################
#########################################################################################################################

#5.Crear una función llamada segundos_a_horas(segundos) que reciba una cantidad de segundos como parámetro y devuelva la cantidad
#de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función.

#def segundos_a_horas(segundos):
#    return segundos / 3600

#horas = segundos_a_horas(int(input("Ingresá la cantidad de segundos: ")))
#print (f"Los segundos ingresados equivalen a: {horas:.0f} hora")

#########################################################################################################################
#########################################################################################################################

#6. Crear una función llamada tabla_multiplicar(numero) que reciba un número como parámetro y imprima la tabla de multiplicar de ese
#   número del 1 al 10. Pedir al usuario el número y llamar a la función.

# def tabla_multiplicar(numero):
#     print(f"Tabla de multiplicar del {numero}:")
#     for i in range(1, 11):
#        resultado = numero * i
#        print(f"{numero} x {i} = {resultado}")

# numero = int(input("Ingresá un número para ver su tabla de multiplicar: "))
# tabla_multiplicar(numero)
    
#########################################################################################################################
#########################################################################################################################

#7.Crear una función llamada operaciones_basicas(a, b) que reciba dos números como parámetros y devuelva una tupla con el resultado de sumarlos,
# restarlos, multiplicarlos y dividirlos. Mostrar los resultados de forma clara.

#def operaciones_basicas(a, b):
#    suma = a + b
#    resta = a - b
#    multiplicacion = a * b
#    division = a / b
#    return (suma, resta, multiplicacion, division)

#a = int(input("Ingresá el primer número: "))
#b = int(input("Ingresá el segundo número: "))

#resultados = operaciones_basicas(a, b)
#print(f"Resultado de las operaciones entre el numero {a} y el numero {b} son:")
#print(f"Suma: {resultados[0]}")
#print(f"Resta: {resultados[1]}")
#print(f"Multiplicación: {resultados[2]}")
#print(f"División: {resultados[3]:.0f}")

#########################################################################################################################
#########################################################################################################################

#8. Crear una función llamada calcular_imc(peso, altura) que reciba el peso en kilogramos y la altura en metros, y devuelva el índice de
# masa corporal (IMC). Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales.

#def calcular_imc(peso, altura):
#     return peso / (altura ** 2)

#peso = float(input("Ingresá tu peso en kilogramos: "))
#altura = float(input("Ingresá tu altura en metros: "))

#print(f"Tu índice de masa corporal (IMC) es: {calcular_imc(peso, altura):.2f}")

#########################################################################################################################
#########################################################################################################################

#9.Crear una función llamada celsius_a_fahrenheit(celsius) que reciba una temperatura en grados Celsius y devuelva su equivalente en
# Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el resultado usando la función.

#def celsius_a_fahrenheit(celsius):
#    return (celsius * 9/5) + 32

#celsius = float(input("Ingresá la temperatura en grados Celsius: "))
#fahrenheit = celsius_a_fahrenheit(celsius)
#print(f"{celsius}°C equivalen a {fahrenheit:.2f}°F")

#########################################################################################################################
#########################################################################################################################

#10. Crear una función llamada calcular_promedio(a, b, c) que reciba tres números como parámetros y devuelva el promedio de ellos.
# Solicitar los números al usuario y mostrar el resultado usando esta función.

def calcular_promedio(a, b, c):
    return (a + b + c) / 3

a = float(input("Ingresá el primer número: "))
b = float(input("Ingresá el segundo número: "))
c = float(input("Ingresá el tercer número: "))

print(f"El promedio de los tres números es: {calcular_promedio(a, b, c):.2f}")