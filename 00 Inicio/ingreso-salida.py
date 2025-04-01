#INPUT, todo lo que ingresa con el INPUT SE LO TOMA COMO CADENA DE CARACTER
nombre = input("Ingresar nombre:")
numeroEntero = input("Ingresar edad: ")

#para que esto no suceda se tiene que convertir el dato en valor numero
numeroEntero = int(numeroEntero)

#PRINT
print("Mucho gusto, " + nombre +"!")
print("Tu edad es ", numeroEntero)

#FPRINT
print(f"Mucho gusto {nombre} tu edad es {numeroEntero}")