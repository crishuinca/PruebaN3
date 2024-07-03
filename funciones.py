import os  , time , msvcrt

pedidos = []

def  opc_1():
    os.system("cls")
    print("REGISTRAR PEDIDO.")
    time.sleep(2)
    
    while True:
        try:
            rut = int(input("Ingrese su RUT (sin guiones ni puntos) : "))
            if len(str(rut))>= 8 and len(str(rut))<=9:
                break
            else:
                print("RUT invalido, ingrese denuevo")
                time.sleep(2)
        except:
            print("RUT invalido, ingrese denuevo")
            time.sleep(2)

    while True:
        nombre = input("Ingrese su nombre : ")
        if len(nombre)>=3:
            break
        else:
            print("El nombre debe tener 3 caracteres como minimo!!")

    while True:
        direccion = input("Ingrese la dirección deseada : ")
        if len(direccion)>=2:
                break
        else:
                print("La dirrecion debe tener 2 caracteres como minimo!!")
    while True:
        comuna = input("Ingrese la comuna  : ")
        if len(direccion)>=3:
            break
        else:
            print("La comuna debe tener 3 caracteres como minimo!!")

    while True:
        try:
            cilindro_5 = int(input("Ingrese cuantos cilindros de  5 kilos quiere :"))
            if cilindro_5 >=1:
                total_5 = cilindro_5*12500
                break
            else:
                print("No puede agregar 0 cilindros  al pedido!!")
                time.sleep(2)
        except:
            print("Valor ingresado es invalido!!")
            time.sleep(2)
    
    while True:
        try:
            cilindro_15 = int(input("Ingrese cuantos cilindros de 15 kilos quiere :"))
            if cilindro_15 >=1:
                total_15 = cilindro_15*25500
                break
            else:
                print("No puede agregar 0 cilindros  al pedido!!")
                time.sleep(2)
        except:
            print("Valor ingresado es invalido!!")
            time.sleep(2)
    total = total_5+total_15
    pedido=[rut,nombre,direccion,cilindro_5,cilindro_15,total]
    pedidos.append(pedido)
    os.system ("cls")
    print("PEDIDO REALIZADO CON ÉXITO")
    time.sleep(2)
def  opc_2():
    if len(pedidos) == 0:
        print("No  existen pedidos, haga uno en la opcion numero 1:")
        time.sleep(3)
    else:
        os.system("cls")
        print("LISTAR PEDIDOS")
        
        time.sleep(1)
        os.system("cls")
        for x in (pedidos):
            print(f"RUT:{x[0]} \nNOMBRE:{x[1]} \nDIRRECCION:{x[2]} \nCILINDROS 5KG:{x[3]} \nCILINDROS 15KG:{x[4]} \nTOTAL:{x[5]}\n\n")
        print("<<PRESIONE UNA TECLA PARA CONTINUAR>>")
        msvcrt.getch()

def  opc_3():
    pass

def  opc_4():
    os.system("cls")
    print("IMPRIMIR HOJA DE RUTA")
    time.sleep(2)
    os.system("cls")

    nombre_archivo = input("Ingrese el nombre del archivo : ")
    import csv 
    with open(f"{nombre_archivo}"+".csv","w",newline="")as archivo:
        for x in (pedidos):
            archivo.write(f"\t\tPEDIDOS\nRUT:{x[0]} \nNOMBRE:{x[1]} \nDIRRECCION:{x[2]} \nCILINDROS 5KG:{x[3]} \nCILINDROS 15KG:{x[4]} \nTOTAL:{x[5]}\n\n")
        print("EL ARCHIVO FUE CREADO CON ÉXITO !")
        time.sleep(3)
        

