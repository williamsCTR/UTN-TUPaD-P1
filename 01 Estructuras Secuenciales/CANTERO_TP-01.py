# 1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”. 

#print("Hola Mundo")

#########################################################################################################################
#########################################################################################################################

#2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando  el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir 
#por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para  realizar la impresión por pantalla.

#nombre = input("Ingrese nombre: ")
#print (f"Hola, ",nombre,"!!!")

#########################################################################################################################
#########################################################################################################################

#3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e  imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa 
#“Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30  años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar 
#la impresión por pantalla.

#nombre = input("Por favor ingresar nombre: ")
#apellido = input("Por favor ingresas apellido: ")
#edad = int( input("Por favor ingresas edad: "))
#residencia = input("Por favor ingresas lugar de residencia: ")
#print(f"Soy ",nombre,",tengo ",edad," años y vivo en ", residencia)

#########################################################################################################################
#########################################################################################################################

#4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y  su perímetro.

#radio = int(input("Por favor ingresar el radio del círculo: "))
#area = 3.14 * (radio ** 2)
#perimetro = (2 * 3.14) * radio
#print(f"El area es ",area, " y el perimetro es ",perimetro )

#########################################################################################################################
#########################################################################################################################

#5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a cuántas horas equivale.

#segundos =(int(input("Ingresas cantidad de segundos: ")))/3600
#print ("Los segundos ingresados equivalen a: ", segundos, "horas")

#########################################################################################################################
#########################################################################################################################

#6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de multiplicar de dicho número.

#numero = int(input("Ingresar un numero: "))
#print(f" 0  x ",numero," = ", (numero * 0))
#print(f" 1  x ",numero," = ", (numero * 1))
#print(f" 0  x ",numero," = ", (numero * 2))
#print(f" 1  x ",numero," = ", (numero * 3))
#print(f" 0  x ",numero," = ", (numero * 4))
#print(f" 1  x ",numero," = ", (numero * 5))
#print(f" 1  x ",numero," = ", (numero * 6))
#print(f" 0  x ",numero," = ", (numero * 7))
#print(f" 1  x ",numero," = ", (numero * 8))
#print(f" 0  x ",numero," = ", (numero * 9))
#print(f" 1  x ",numero," = ", (numero * 10))

#########################################################################################################################
#########################################################################################################################

#7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por  pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.

#num1 = int (input("Ingresar numero distinto de 0 "))
#num2 = int (input("Ingrese el segundo numero distinto de 0 "))
#if num1 and num2 != 0:print(f"La suma de los numero es ", (num1 + num2))

#########################################################################################################################
#########################################################################################################################

#8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice  de masa corporal.

#altura = int(input("Ingresar altura"))
#peso = int (input("Ingresar peso en KG"))
#masaCorporal = peso / (altura**2)
#print(f"Tu masa corporal es", masaCorporal)

#########################################################################################################################
#########################################################################################################################

# 9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por pantalla su equivalente en grados Fahrenheit.
# T𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐹𝑎ℎ𝑟𝑒𝑛ℎ𝑒𝑖𝑡 = 9/5                   𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐶𝑒𝑙𝑠𝑖𝑢𝑠   + 32

#tempCelsius = int (input("Ingresar temperatura en Celsius :"))
#tempFah = (tempCelsius * 9/5 ) + 32
#print(f"La temperatura en Fahrenheit es: " , tempFah)


#########################################################################################################################
#########################################################################################################################

#10) Crear un programa que pida al usuario  3 números e imprima por pantalla el promedio de dichos números.
#num1 = int (input("Ingresar numero: "))
#num2 = int (input("Ingrese el segundo numero: "))
#num3 = int (input("Ingrese el tercer numero: "))
#promedio = (num1 + num2 + num3) / 3
#print(f"El promedio de los numeros ingresado es ", promedio)