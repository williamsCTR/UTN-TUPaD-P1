## 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
## (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

#for i in range (101):
#    print(i)

#########################################################################################################################
#########################################################################################################################

##2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de dígitos que contiene.

#num = input("Ingrese un numero entero: ")
#cantidadDig = len(num)
#print(f"La Cantidad de digito del numero: ", num, "es: ", cantidadDig)

#########################################################################################################################
#########################################################################################################################

#3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores dados por el usuario, excluyendo esos dos valores.

#num1 = int(input("Ingrese el primer numero: "))
#num2 = int(input("Ingrese el segundo numero: "))
#suma = 0

#for numero in range (num1,num2+1):
#    suma += numero

#print(suma)

#########################################################################################################################
#########################################################################################################################

#4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
#secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0.

#numero = int(input("Por favor ingrese un numero entero para sumar (ingresar 0 para terminar la suma) "))
#suma = 0
#while numero !=0:
#    suma += numero
#    numero = int(input("Por favor ingrese un numero entero para sumar (ingresar 0 para terminar la suma) "))

#print(f"La suma de todos los numero es: ", suma)

#########################################################################################################################
#########################################################################################################################

#5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
#programa debe mostrar cuántos intentos fueron necesarios para acertar el número

#import random
#numRandom = random.randint(0,9)
#num = int(input("Ingresar un numero entre 0 y 9"))
#contador = 0

#while num != numRandom:
#    num = int(input("Ingrese otro numero entre o y 9"))
#    contador+=1

#print("Felicidades adivinates el numeor random y te tomo: ", contador,"intentos")

#########################################################################################################################
#########################################################################################################################

#6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos entre 0 y 100, en orden decreciente.

#for e in range(0,101,2):
#    print(e)

#########################################################################################################################
#########################################################################################################################

#7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un número entero positivo indicado por el usuario.

#num = int(input("Ingresar un numero entero: "))
#suma = 0

#for e in range(0,num+1):
#    suma += e

#print(suma)

#########################################################################################################################
#########################################################################################################################

#8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
#programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
#negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
#menor, pero debe estar preparado para procesar 100 números con un solo cambio).

#numerosPares = 0
#numerosImpares = 0
#numerosNegativos = 0
#numerosPositivos = 0

#for e in range(10):
#    numero = int (input("Ingresar un numero entero"))
#    if numero >= 0:
#        numerosPositivos+=1
#    else:
#        numerosNegativos +=1
#    
#    if numero % 2 == 0:
#        numerosPares +=1
#    else:
#        numerosImpares +=1
#print("Se ingreso: ", e + 1, "de numero y la cantidad de pares son: ", numerosPares," la cantidad de impares son: ", numerosImpares, " la cantidad de positivos son: ", numerosPositivos, " y la cantidad de negativos son: ", numerosNegativos)

#########################################################################################################################
#########################################################################################################################

#9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
#media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
#poder procesar 100 números cambiando solo un valor).

#suma = 0
#for e in range(10):
#    numero = int (input("Ingresar un numero entero"))
#    suma += numero
#print("La media es: ", (suma/(e+1)))

#########################################################################################################################
#########################################################################################################################

#10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
#usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

numero = input("Ingrese un numero: ")
numeroInvertido = numero[::-1]
print("El numero ingresado es: ",numero," al invertirlo queda como: ", numeroInvertido)
