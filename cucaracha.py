class Cucaracha:

     def __init__(self,cantidad):
        self.cantidad = cantidad

     def reproducir(self):
        return"holaaa"
     def aplastar(self):
        return "que hay"
     def rociar(self):
        return "siempre en linea"
     def salir(self):
        return exit    



     def menu():
         opcion = 0
    

         while opcion != 4:
             print ("1- reproducir")
             print ("2- aplastar")  
             print ("3- rociar")
             print ("4- salir")
             opcion = input("seleccione una opcion:")

         if opcion == 1:
            reproducir()
         elif opcion == 2:
            aplastar()
         elif opcion == 3:
            rociar()
         elif opcion == 4:
            salir()           