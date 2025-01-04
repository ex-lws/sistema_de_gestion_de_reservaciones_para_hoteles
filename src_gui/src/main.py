# Modulos agregados para ser ejecutados desde una sola clase para ahorrar codigo

from menu import mostrarOpciones
from menu import opcionUsuario
from modulo_1_listar_habitaciones import mostrarHabitaciones
from modulo_2_disponibilidad_habitaciones import menu_disponibilidad
from modulo_3_proceso_reservacion import mostrar_instrucciones_reservacion
from modulo_3_proceso_reservacion import recoger_datos
from modulo_3_proceso_reservacion import insertar_datos
from modulo_3_proceso_reservacion import actualizar_estado_habitacion
from modulo_4_mostrar_reportes import mostrar_reportes_reservacion


def main():

    #Funciones importadas
    while True:
        mostrarOpciones()
        opcion_usuario = opcionUsuario()

        #Operaciones

        if opcion_usuario == 0:
            print ("--Su objetivo es realizar las reservaciones que el húesped solicita.--")

        elif opcion_usuario == 1:
            print("--Mostrando habitaciones.--")
            mostrarHabitaciones()

        elif opcion_usuario == 2:
            print("--Entrando al menu de consulta de disponibilidad de las habitaciones.--")
            menu_disponibilidad()

        elif opcion_usuario == 3:
            print("--Iniciando reporte de reserveación.--")
            mostrar_instrucciones_reservacion()
            datos_reservacion = recoger_datos()
            print(datos_reservacion)
            insertar_datos(datos_reservacion['cliente'], datos_reservacion['habitacion'], datos_reservacion['reservacion'], datos_reservacion['pago'])
            numero_habitacion = datos_reservacion['habitacion']['numero_habitacion']
            actualizar_estado_habitacion(numero_habitacion)
        elif opcion_usuario == 4:
            print("--Mostrando los reportes de reservación.--")
            mostrar_reportes_reservacion()
        
        elif opcion_usuario == 5:
            print("--Mostrando estadísticas operacionales.--")    
        
        elif opcion_usuario == 6:
            print("--Saliendo del sistema...--")
            break

main()