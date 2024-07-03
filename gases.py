import os, time , msvcrt
from funciones import *

os.system("cls")
print ("Bienvenido a GasXplosive")
time.sleep(1)

while True:
    
    os.system("cls")
    print("""
          __________________________
               MENÚ DE OPCIONES 
          __________________________
          1)Registrar  pedido
          2)Listar todos los pedidos
          3)Buscar pedido por RUT
          4)Imprimir hoja de ruta
          5)Salir del programa
          ___________________________""")
    
    
    
    try:
        opc = int(input("Ingrese la opción deseada : "))
        if opc == 1:
            opc_1()
        elif opc ==2:
            opc_2()
        elif opc == 3:
            opc_3()
        elif opc ==4:
            opc_4()
        elif opc == 5:
            os.system("cls")
            print("Gracias por la preferencia a GASXPLOSIVE")

            time.sleep(5)
            print("gracias a dios🙏")
            break
        else:
            print("La opción tiene que ser entre 1 y 5")
            time.sleep(3)
    
    except:
        print("La opción  ingresada no es valida!!")
    