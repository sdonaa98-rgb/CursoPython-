print("¡Hola mundo!")
nombre = input("¿Cómo te llamas? ")
edad = int(input("Edad: "))
print (nombre)
print (edad)
#print(f"Hola {nombre}, tienes {edad} años")
if edad >= 65:  
    print ("adulto mayor")
elif edad >=18 and edad <=64:
    print ("Mayor de edad")
elif edad <=17 and edad >=1:
    print("Menor de edad")
else:
    print ("numero negativo")
    