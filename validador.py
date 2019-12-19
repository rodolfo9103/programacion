import re

print ("! Bienvenido al validador de nombres!")
nombre = re.compile (r '^ [A-Za-zäÄëËïÏöÖüÜáéíóúáéíóúÁÉÍÓÚÂÊÎÔÛâêîôûàèìòùÀÈÌÒÙ] {3,20} $')

nombreYa apellido = ("Ingrese su nombre:", "Ingrese su Apellido:")
respuestas = []

para yo en nombreYa apellido:
    rsp = input (i)
    si nombre.search (rsp):
        respuestas.append (rsp)
    más:
        
        respuestas.append ("Ha ingresado un nombre y apellido incorrecto")

imprimir (respuestas)