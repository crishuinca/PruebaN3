import os  , time , msvcrt

pedidos = []

def  opc_1():
    os.system("cls")
    print("REGISTRAR PEDIDO.")
    time.sleep(2)
    rut = int(input("Ingrese su RUT (sin guiones ni puntos) : "))
    nombre = input("Ingrese su nombre : ")
    direccion = input("Ingrese la dirección deseada : ")
    cilindro_5 = int(input("Ingrese cuantos cilindros de  5 kilos quiere :"))
    total_5 = cilindro_5*12500
    cilindro_15 = int(input("Ingrese cuantos cilindros de 15 kilos quiere :"))
    total_15 = cilindro_15*25500
    total = total_5+total_15
    pedido=[rut,nombre,direccion,cilindro_5,cilindro_15,total]
    pedidos.append(pedido)
def  opc_2():
    print(pedidos)
    msvcrt.getch()

def  opc_3():
    pass

def  opc_4():
    pass

