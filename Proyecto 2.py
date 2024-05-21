from datetime import datetime, time

class Zona:
    def __init__(self, nombre, temperatura_deseada=22):
        self.nombre = nombre
        self.temperatura_deseada = temperatura_deseada
        self.temperatura_actual = 22
        self.horarios = {}

    def ajustar_temperatura(self, nueva_temperatura):
        self.temperatura_deseada = nueva_temperatura
        print(f"Temperatura ajustada a {nueva_temperatura}°C en la zona {self.nombre}")

    def programar_horario(self, hora, temperatura):
        self.horarios[hora] = temperatura
        print(f"Horario programado: {hora.strftime('%H:%M')} - {temperatura}°C en la zona {self.nombre}")

class Sensor:
    def __init__(self, zona):
        self.zona = zona

    def leer_temperatura(self):
        # Aquí podríamos simular una lectura de sensor real.
        return self.zona.temperatura_actual

class SistemaDeControl:
    def __init__(self):
        self.zonas = []

    def agregar_zona(self, zona):
        self.zonas.append(zona)
        print(f"Zona {zona.nombre} agregada con temperatura deseada {zona.temperatura_deseada}°C")

    def ajustar_temperatura_zona(self, nombre_zona, nueva_temperatura):
        for zona in self.zonas:
            if zona.nombre == nombre_zona:
                zona.ajustar_temperatura(nueva_temperatura)
                break

    def programar_horario_zona(self, nombre_zona, hora, temperatura):
        for zona in self.zonas:
            if zona.nombre == nombre_zona:
                zona.programar_horario(hora, temperatura)
                break

    def monitorear_y_ajustar_temperatura(self):
        for zona in self.zonas:
            sensor = Sensor(zona)
            temperatura_actual = sensor.leer_temperatura()
            ahora = datetime.now().time()
            if ahora in zona.horarios:
                zona.temperatura_deseada = zona.horarios[ahora]
            if temperatura_actual < 22 or temperatura_actual > 22:
                zona.temperatura_actual = 22
                print(f"Temperatura en {zona.nombre} ajustada a 22°C debido a la temperatura ambiente")

class InterfazUsuario:
    def __init__(self, sistema_control):
        self.sistema_control = sistema_control

    def mostrar_menu(self):
        while True:
            print("\nMenú Principal")
            print("1. Configurar zonas de temperatura")
            print("2. Ajustar temperatura por zonas")
            print("3. Programar horarios")
            print("4. Monitorear sensores y ajustar temperatura")
            print("5. Salir")
            opcion = input("Seleccione una opción: ")
            if opcion == '1':
                self.configurar_zonas()
            elif opcion == '2':
                self.ajustar_temperatura()
            elif opcion == '3':
                self.programar_horarios()
            elif opcion == '4':
                self.monitorear_sensores()
            elif opcion == '5':
                print("Saliendo del sistema...")
                break
            else:
                print("Opción no válida, por favor intente de nuevo.")

    def configurar_zonas(self):
        nombre_zona = input("Ingrese el nombre de la zona: ")
        temperatura_deseada = int(input("Ingrese la temperatura deseada para la zona: "))
        zona = Zona(nombre_zona, temperatura_deseada)
        self.sistema_control.agregar_zona(zona)

    def ajustar_temperatura(self):
        nombre_zona = input("Ingrese el nombre de la zona: ")
        nueva_temperatura = int(input("Ingrese la nueva temperatura deseada para la zona: "))
        self.sistema_control.ajustar_temperatura_zona(nombre_zona, nueva_temperatura)

    def programar_horarios(self):
        nombre_zona = input("Ingrese el nombre de la zona: ")
        hora_str = input("Ingrese la hora (HH:MM): ")
        temperatura = int(input("Ingrese la temperatura para el horario programado: "))
        hora = datetime.strptime(hora_str, '%H:%M').time()
        self.sistema_control.programar_horario_zona(nombre_zona, hora, temperatura)

    def monitorear_sensores(self):
        self.sistema_control.monitorear_y_ajustar_temperatura()

if __name__ == "__main__":
    sistema_control = SistemaDeControl()
    interfaz_usuario = InterfazUsuario(sistema_control)
    interfaz_usuario.mostrar_menu()