from conexion_bd import conectar_bd
import matplotlib.pyplot as plt
from PyQt5 import uic

def mostrarAyuda():

    print ("Las estadísticas operacionales del hotel permiten obtener un panorama de su funcionamiento y rendimiento.")
    print ("La tasa de ocupación muestra la cantidad de reservaciones actualmente reservadas y las compara con los activos del hotel.")
    print ("La tasa sobre los tipos de habtiación más se reservan tiene como finalidad analizar qué habitaiones prefieren los huéspedes para sus estancias.")
    print ("La tasa sobre el promedio de estancia muestra el tiempo promedio que los huéspedes se alojan en el hotel.")
    print ("Las estadísticas operacionales se muestran una vez la base de datos del sistema Rommie esté correctamente aliementada.")
    print ("--Desarrollado por Next Gen Software.--")

def tasaOcupacion():
    conexion = conectar_bd()
    if conexion:
        print("Conexión exitosa a la base de datos.")
        cursor = conexion.cursor()
        print ("--Mostrando gráficas sobr la tasa de ocupación del hotel.--")

        # Consulta para obtener el número total de habitaciones y las habitaciones ocupadas
        cursor.execute("SELECT COUNT(*) FROM habitacion")
        total_habitaciones = cursor.fetchone()[0]
        
        # Contar habitaciones con estado distinto a 'Disponible' (ocupadas o reservadas)
        cursor.execute("SELECT COUNT(*) FROM habitacion WHERE estado != 'Disponible'")
        habitaciones_ocupadas = cursor.fetchone()[0]

        # Calcular tasa de ocupación
        tasa = (habitaciones_ocupadas / total_habitaciones) * 100
        print(f"Tasa de ocupación: {tasa:.2f}%")

        # Graficar
        categorias = ['Ocupadas', 'Disponibles']
        valores = [habitaciones_ocupadas, total_habitaciones - habitaciones_ocupadas]

        plt.bar(categorias, valores, color=['red', 'green'])
        plt.title("Tasa de Ocupación")
        plt.ylabel("Número de Habitaciones")
        plt.show()

def tasaHabitacionMasReservada():
    conexion = conectar_bd()
    if conexion: 
        cursor = conexion.cursor()
        print("--Mostrando gráfica sobre las habitaciones más reservadas.--")

        # Consulta para obtener las habitaciones más reservadas
        cursor.execute("SELECT tipo_habitacion, COUNT(*) AS habitaciones_ocupadas FROM habitacion WHERE estado != 'Disponible' GROUP BY tipo_habitacion ORDER BY habitaciones_ocupadas DESC")

        # Obtener todos los resultados de la consulta
        tipos_habitacion_reservadas = cursor.fetchall()

        # Separar los tipos de habitación y las cantidades de habitaciones ocupadas
        tipos = [fila[0] for fila in tipos_habitacion_reservadas]  # tipo_habitacion
        ocupadas = [fila[1] for fila in tipos_habitacion_reservadas]  # habitaciones_ocupadas

        # Mostrar la gráfica
        plt.bar(tipos, ocupadas, color='blue')
        plt.title("Tipos de Habitación Más Reservados")
        plt.xlabel("Tipo de Habitación")
        plt.ylabel("Número de Habitaciones Ocupadas")
        plt.xticks(rotation=45)  # Rotar las etiquetas del eje x si son largas
        plt.tight_layout()  # Ajustar el espaciado para que todo se vea bien
        plt.show()

def tasaPromedioEstancia():
    conexion = conectar_bd()
    if conexion: 
        cursor = conexion.cursor()
        print("--Mostrando gráfico sobre el tiempo promedio de estancia de los huéspedes.--")

        # Consulta para obtener el tiempo promedio de estancia
        cursor.execute("SELECT AVG(EXTRACT(DAY FROM (check_out - check_in))) AS promedio_estancia FROM reservacion")

        # Obtener el resultado de la consulta
        promedio_estancia = cursor.fetchone()[0]

        # Mostrar la gráfica
        # Dado que es un solo valor, usaremos una gráfica de barras de una sola barra
        plt.bar(['Promedio de Estancia'], [promedio_estancia], color='green')
        plt.title("Promedio de Estancia de los Huéspedes")
        plt.ylabel("Días de Estancia Promedio")
        plt.tight_layout()  # Ajustar el espaciado para que todo se vea bien
        plt.show()

# MENU DE SELECCION 

while True:

    print ("===============================================================================")
    print ("Bienvenido de nuevo, aquí podrás consultar estadísticas operacionales del hotel")
    print ("================================================================================")
    print (" ")
    print (" ")
    print ("Opción 0.- Mostrar ayuda")
    print ("Opción 1.- Mostrar gráfico sobre la tasa de ocupación del hotel.")
    print ("Opción 2.- Mostrar gráfico sobre los tipos de habitación más reservadas.")
    print ("Opción 3.- Mostrar gráfico sobre el promedio de estancia de los huéspedes.")
    print ("Opción 4.- Salir")

    seleccion_usuario = int (input ("Seleccione alguna opción entre 0 y 4:"))

    if seleccion_usuario == 0:
        print ("--Mostrando ayuda.--")
        mostrarAyuda()

    if seleccion_usuario == 1:
        tasaOcupacion()

    if seleccion_usuario == 2:
        tasaHabitacionMasReservada()

    if seleccion_usuario == 3:
        tasaPromedioEstancia()

    if seleccion_usuario == 4:
        print ("--Nos vemos pronto.--")
        break
