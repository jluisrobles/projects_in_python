mi_texto = "Los dias de la semana"
resultado = mi_texto[0]
print (resultado)

mi_texto1 = "Los dias de la semana"
resultado1 = mi_texto1.index("e")
print (resultado1)

#Desde dónde buscará en este caso desde la posicion 5
mi_texto2 = "Los dias de la semana"
resultado2 = mi_texto2.index("s",5)
print (resultado2)

#Desde dónde buscará en este caso desde la posicion 5 hasta 10
mi_texto3 = "Los dias de la semana"
resultado3 = mi_texto3.index("d",5,10)
print (resultado3)

#Busca de IZQUIERDA a DERECHA
mi_textoS= "Los dias de la semana"
resultadoS = mi_textoS.rindex("e")
print (resultadoS)