print("¡Hola mundo!")
nombre = input("¿Cómo te llamas? ")
edad = int(input("Edad: "))
print (nombre)
print (edad)
#print(f"Hola {nombre}, tienes {edad} años")

#Si edad <0 >101:
if edad >= 65 and edad<=100:  
    print ("adulto mayor")
elif edad >=18 and edad <=64:
    print ("Mayor de edad")
elif edad <=17 and edad >=1:
    print("Menor de edad")
elif edad <0 or edad >=101: 
    print ("Esa edad no es posible")
else:
    print ("numero negativo")
    