#Imprimir como tipo lista
compras = ["pan", "leche", "huevos"]
print (compras)
# Imprimir iterando los elementos de la lista. (con FOR)
for producto in compras:
    print(producto)
#Appened - Agregar elemento al final de una lsita
compras.append("refresco")
print (compras)
#Pop - recupear ultimo elemento de la lista 
variableultimoelemento = compras.pop() 
print (variableultimoelemento)
print (compras)
#Parseo - conversión de datos 
variableTexto = float ("1.58")
variableNumero = 1.58
print (variableTexto)
print (variableNumero)
resultado= variableNumero+variableTexto
print (resultado)
#truncar / de flotante lo convertimos a entero para hacer una suma. 
variableTexto = float ("1.58") 
variableentera = int (variableTexto)
variableNumero = 1.58
resultado= variableNumero+variableentera
print (resultado)
#Redondeando 
variableround = round (variableTexto)
resultado= variableNumero+variableround
print (resultado)