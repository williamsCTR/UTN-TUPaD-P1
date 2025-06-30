# 1) Dado el diccionario precios_frutas precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
#   Añadir las siguientes frutas con sus respectivos precios:
#   ● Naranja = 1200
#   ● Manzana = 1500
#   ● Pera = 2300

#precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

#precios_frutas['Naranja'] = 1200
#precios_frutas['Manzana'] = 1500
#precios_frutas['Pera'] = 2300

#print(precios_frutas)



#########################################################################################################################
#########################################################################################################################

# 2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:
#   ● Banana = 1330
#   ● Manzana = 1700
#   ● Melón = 2800

#precios_frutas['Banana'] = 1330
#precios_frutas['Manzana'] = 1700
#precios_frutas['Melón'] = 2800

#print(precios_frutas)



#########################################################################################################################
#########################################################################################################################

# 3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
#desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los precios.

#frutas = list(precios_frutas.keys())
#print(frutas)



#########################################################################################################################
#########################################################################################################################

# 4) Escribí un programa que permita almacenar y consultar números telefónicos.
#• Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
#• Luego, pedí un nombre y mostrale el número asociado, si existe.

#contactos = {}
#for i in range(1,6):
#    nombre = input(f"Ingresa el nombre del contacto {i}: ")
#    numero = int(input(f"Ingresa el numero de {nombre}: "))
#    contactos[nombre] = numero

#persona = input("De quien queres saber el numero?: ")

#if persona in contactos:
#    print(f"El número de {persona} es {contactos[persona]}.")
#else:
#    print(f"{persona} no está en la agenda.")




#########################################################################################################################
#########################################################################################################################

# 5)  Solicita al usuario una frase e imprime:
#   • Las palabras únicas (usando un set).
#   • Un diccionario con la cantidad de veces que aparece cada palabra.

#frase = input("Ingresa una frase: ")
#palabras = frase.split()
#palabras_unicas = set(palabras)

#recuento = {}
#for palabra in palabras:
#    if palabra in recuento:
#        recuento[palabra] += 1
#    else:
#        recuento[palabra] = 1

#print(f"Palabras unicas: {palabras_unicas}")
#print(f"Recuento: {recuento}")        



#########################################################################################################################
#########################################################################################################################
# 6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas. Luego, mostrá el promedio de cada alumno.

#notas_alumnos = {}
#for i in range(3):
#    nombre = input(f"Ingrese el nombre del alumno {i+1}: ")
#    nota1 = float(input(f"Ingresa la primera nota de {nombre}: "))
#    nota2 = float(input(f"Ingresa la segunda nota de {nombre}: "))
#    nota3 = float(input(f"Ingresa la tercera nota de {nombre}: "))
#    notas_alumnos[nombre] = (nota1, nota2, nota3)

#for nombre, notas in notas_alumnos.items():
#    total = 0
#    for nota in notas:
#        total += nota
#    promedio = total / 3
#    print(f"El promedio de {nombre} es de {promedio}")



#########################################################################################################################
#########################################################################################################################

#7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1 y Parcial 2:
#   • Mostrá los que aprobaron ambos parciales.
#   • Mostrá los que aprobaron solo uno de los dos.
#   • Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).

#parcial1 = {"Juan", "Pedro", "Maria", "Carla", "Martin"}
#parcial2 = {"Juan", "Mariana", "Sebastian", "Carla"}
#ambos = parcial1.intersection(parcial2)
#solo_parcial1 = parcial1.difference(parcial2)
#solo_parcial2 = parcial2.difference(parcial1)
#solo_uno = solo_parcial1.union(solo_parcial2)
#almenos_uno = parcial1.union(parcial2)

#print(f"Aprobaron ambos parciales: {ambos}")
#print(f"Aprobaron solo un parcial: {solo_uno}")
#print(f"Aprobaron al menos uno: {almenos_uno}")

#########################################################################################################################
#########################################################################################################################

#8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock. Permití al usuario:
#   • Consultar el stock de un producto ingresado.
#   • Agregar unidades al stock si el producto ya existe.
#   • Agregar un nuevo producto si no existe.

#productos = {"jabon": 3, "shampoo": 5, "algodon": 7, "perfume": 4}
#opcion= 0

#while opcion != 4:
#    print("Que desea realizar? ")
#    print("1. Consultar stock")
#    print("2. Agregar unidades a un producto existente")
#    print("3. Agregar un nuevo producto")
#    print("4. Salir")
#    opcion = int(input("Ingrese el numero de opcion: "))

#    if opcion == 1:
#        nombre = input("De que producto queres consultar stock? ")
#        if nombre in productos:
#            print(f"Stock de {nombre}: {productos[nombre]} unidades")
#        else:
#            print("El producto no existe en el inventario.")
#    elif opcion == 2:
#        nombre = input("A que producto queres agregar unidades? ")
#        if nombre in productos:
#            sumar = int(input("Cuantas unidades queres agregar? "))
#            productos[nombre] += sumar
#        else:
#            print("El producto no existe en el inventario.")
#    elif opcion == 3:
#        nombre = input("Que producto queres agregar? ")
#        cantidad = int(input("Cuantas unidades del nuevo producto? "))
#        productos[nombre] = cantidad
#    elif opcion == 4: 
#        print(f"Stock final: {productos}")
#        print("PROGRAMA FINALIZADO. GRACIAS")
#    else: 
#        print("Ingrese una opcion valida")
        
#########################################################################################################################
#########################################################################################################################

#9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.

#agenda = {("martes", "14:00"): "Consulta progamacion", ("jueves", "16:00"): "consulta matematica"}
    
#dia = input("Ingrese el día: ")
#hora = input("Ingrese la hora: ")
#clave = (dia, hora)

#if clave in agenda:
#    print("Actividad: ", agenda[clave])
#else:
#    print("No hay actividades en ese dia y horario.")



#########################################################################################################################
#########################################################################################################################

#10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo diccionario donde:
#   • Las capitales sean las claves.
#   • Los países sean los valores.

original = {"Argentina": "Buenos Aires", "Chile": "Santiago"}
invertido = {}
for pais, capital in original.items():
    invertido[capital]= pais 

print(original)
print(invertido)