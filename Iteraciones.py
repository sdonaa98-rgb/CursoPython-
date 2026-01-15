#Ejercicio de ciclo FOR 
altura = 8
for i in range(1, altura +1):
    print("*" * i)

#Ejercicio de ciclo FOR Inverso 

for i in reversed(range(altura)):
    print("*" * i)

#Ejercicio de Ciclo While (sabe donde empieza, se cumple la condición)
contador = 0
while contador <=5:
    print(contador)
   # contador += 1
    contador = contador +1
#Ejercicio de while empezando de 5 a 0
contador = 5
while contador >=0:
    print(contador)
   # contador += 1
    contador = contador -1