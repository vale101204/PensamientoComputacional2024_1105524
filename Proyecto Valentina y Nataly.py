import os


contRuta1 = 0
contRuta2 = 0
contRuta3 = 0
contRuta4 = 0
contRuta5 = 0
precio_total = 0.0

def solicitar_informacion():
    print("-------BIENVENIDO A LA COMPRA DE BOLETO---------")
    print("Rutas existentes:")
    print("Estacion Javier - Codigo: 51")
    print("Estacion Trebol - Codigo: 61")
    print("Estacion Don Bosco - Codigo: 71")
    print("Estacion Plaza municipal - Codigo: 82")
    codigo_abordo = int(input("Por favor, ingrese el codigo de la estacion que abordara: "))
    if(codigo_abordo == 51 or codigo_abordo == 61 or codigo_abordo == 71 or codigo_abordo == 82):
        print("El codigo ingresado es valido")
    else:
        print("El codigo ingresado no es valido")
        return
    codigo_destino = int(input("Por favor, ingrese el codigo de la estacion de destino: "))
    if(codigo_destino == 51 or codigo_destino == 61 or codigo_destino == 71 or codigo_destino == 82):
        print("El codigo ingresado es valido")
    else:
        print("El codigo ingresado no es valido")
        return
    if(codigo_abordo == 51):
        if(codigo_destino == 61):
            print("La ruta si existe")
        elif(codigo_destino == 71):
            print("La ruta si existe")
        else:
            print("Error. Esta ruta no existe")
            return
    elif(codigo_abordo == 71):
        if(codigo_destino == 82):
            print("La ruta si existe")
        else:
            print("Error. La ruta no existe")
            return
    elif(codigo_abordo == 61):
        if(codigo_destino == 51):
            print("La ruta si existe")
        else:
            print("Error. La ruta no existe")
            return
    elif(codigo_abordo == 82):
        if(codigo_destino == 51):
            print("La ruta si existe")
        else:
            print("Error. La ruta no existe")
            return
    
    nombre = input("Ingrese su nombre: ")
    edad = int(input("Ingrese su edad: "))
    embarazo = input("Indique si se encuentra embarazada, Si o No: ")
    calculos(codigo_abordo, codigo_destino, edad, embarazo)

def calculos(codigo_abordo, codigo_destino, edad, embarazo):
    global contRuta1, contRuta2, contRuta3, contRuta4, contRuta5, precio_total

    ruta = ""
    distancia = 0
    precio = 0.00
    tiempo_estimado = 0

    if codigo_abordo == 51:
        if codigo_destino == 61:
            ruta = "Usted debe abordar en la estacion Javier y desabordar en la estacion Trebol"
            distancia = 39
            contRuta1 += 1
        elif codigo_destino == 71:
            ruta = "Usted debe abordar en la estacion Javier y desabordar en la estacion Don Bosco"
            distancia = 18
            contRuta2 += 1
        
    elif codigo_abordo == 61:
        if codigo_destino == 51:
            ruta = "Usted debe abordar en la estacion Trebol y desabordar en la estacion Javier"
            distancia = 8
            contRuta4 += 1
        
    elif codigo_abordo == 71:
        if codigo_destino == 82:
            ruta = "Usted debe abordar en la estacion Don Bosco y desabordar en la estacion Plaza Municipal"
            distancia = 23
            contRuta3 += 1
        
    elif codigo_abordo == 82:
        if codigo_destino == 51:
            ruta = "Usted debe abordar en la estacion Plaza Municipal y desabordar en la estacion Javier"
            distancia = 42
            contRuta5 += 1
        

    if distancia >= 8:
        distancia_restante = distancia - 8
        precio = 1.50 + (distancia_restante * 0.25)

    if embarazo.lower() == "si":
        precio = 0
    elif 15 <= edad <= 25:
        descuento = precio * 0.25
        precio -= descuento

    tiempo_estimado = distancia / 20
    tiempo_total = tiempo_estimado
    precio_total += precio
    print("Ruta: ", ruta)
    print("Se tardara un aproximado de: ", tiempo_estimado, " horas")
    print("El precio de boleto sera de: ", precio)
    print("")



def verEstaciones():
    print("Estaciones existentes:")
    print("estacion Javier - Codigo: 51")
    print("estacion Trebol - Codigo: 61")
    print("estacion Don Bosco - Codigo: 71")
    print("estacion Plaza municipal - Codigo: 82")
    print("-------------------------------------")
    print("Rutas existentes:")
    print("Ruta 1. De la estacion 51 a la estacion 61 con distancia de 39 kilometros")
    print("Ruta 2. De la estacion 51 a la estacion 71 con distancia de 18 kilometros")
    print("Ruta 3. De la estacion 71 a la estacion 82 con distancia de 23 kilometros")
    print("Ruta 4. De la estacion 61 a la estacion 51 con distancia de 8 kilometros")
    print("Ruta 5. De la estacion 82 a la estacion 51 con distancia de 42 kilometros")
    print("--------------------------------------------------------------------------")
    

def verReportes():
    global contRuta1, contRuta2, contRuta3, contRuta4, contRuta5, precio_total

    print("Cantidad de boletos vendidos para la ruta 1: " + str(contRuta1))
    print("Cantidad de boletos vendidos para la ruta 2: " + str(contRuta2))
    print("Cantidad de boletos vendidos para la ruta 3: " + str(contRuta3))
    print("Cantidad de boletos vendidos para la ruta 4: " + str(contRuta4))
    print("Cantidad de boletos vendidos para la ruta 5: " + str(contRuta5))

    totalBoletos = contRuta1 + contRuta2 + contRuta3 + contRuta4 + contRuta5
    print("Total de boletos vendidos: " + str(totalBoletos))
    print("Cantidad de dinero percibido por la venta de boletos: " + str(precio_total))

def ejecutarOpcion(opcion):
    if opcion == 1:
        verEstaciones()
    elif opcion == 2:
        solicitar_informacion()
    elif opcion == 3:
        verReportes()
        
    

def main():
    continuar = True
    while(continuar):
        opcionCorrecta = False
        while(not opcionCorrecta):
            print("--- BIENVENIDO AL MENU PRINCIPAL ---")
            print("1. Ver estaciones existentes")
            print("2. Comprar boleto")
            print("3. Reportes")
            print("4. Salir del programa")
            print("------------------------------------")
            opcion = int(input("Seleccione una opcion: "))

            if opcion < 1 or opcion > 4:
                print("Opcion incorrecta, ingrese nuevamente...")
            elif opcion == 4:
                continuar = False
                break
            else:
                opcionCorrecta = True
                ejecutarOpcion(opcion)

main()