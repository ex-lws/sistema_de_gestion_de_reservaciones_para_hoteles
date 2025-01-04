from conexion_bd import conectar_bd

# Realizamos las estructuras de las consultas.

def obtener_habitaciones_disponibles():
    conexion = conectar_bd()
    if conexion:
        try:
            cursor = conexion.cursor()
            # Consulta para obtener habitaciones con estado 'Disponible' sin importar mayúsculas/minúsculas
            cursor.execute("SELECT numero_habitacion, tipo_habitacion, estado FROM habitacion WHERE LOWER(estado) = 'disponible';")
            habitaciones = cursor.fetchall()

            if habitaciones:
                print("--Habitaciones disponibles--:")
                for habitacion in habitaciones:
                    print(f"Número: {habitacion[0]}, Tipo: {habitacion[1]}")
            else:
                print("--No hay habitaciones disponibles--.")
            
            cursor.close()
        except Exception as e:
            print("--Error al realizar la consulta:--", e)
        finally:
            conexion.close()

def obtener_habitaciones_disponibles_por_tipo():

    conexion = conectar_bd()
    if conexion:
        
        try:
            cursor = conexion.cursor()
            opcion_usuario = input("Por favor escriba el tipo de habitación a consultar:")
            #Agregamos métodos para adecuar el input que va a la base de datos
            tipo_habitacion_consulta = opcion_usuario.strip().capitalize()
            print ("Consultó: ", tipo_habitacion_consulta)
            query = "SELECT numero_habitacion, precio_noche FROM habitacion WHERE estado = 'Disponible' and tipo_habitacion = %s;"
            cursor.execute(query, (tipo_habitacion_consulta,))
            habitaciones_disponibles_por_tipo = cursor.fetchall()

            if habitaciones_disponibles_por_tipo:
                print("--Habitaciones disponibles:--")
                for habitacion in habitaciones_disponibles_por_tipo:
                    numero, precio = habitacion
                    print(f"Número: {numero}, Precio por noche: ${precio}")
            else:
                print("--No se encontraron habitaciones disponibles de ese tipo.--")

        except Exception as e:
            print("--Error: la consulta no se pudo realizar.--")
    else:
        print ("--La conexión con la base de datos falló.--")

def consultar_habitaciones_por_precio():
    conexion = conectar_bd()
    if conexion:
        try:
            cursor = conexion.cursor()
            # Obtener el precio del usuario y convertirlo a float
            precio_habitacion_consulta = float(input("Escriba el precio de la habitación que desea consultar: "))

            # Usar un marcador de posición para evitar inyección SQL
            query = "SELECT numero_habitacion, tipo_habitacion, precio_noche FROM habitacion WHERE estado = 'Disponible' and precio_noche >= %s;"
            cursor.execute(query, (precio_habitacion_consulta,))

            # Obtener los resultados de la consulta
            habitaciones_disponibles = cursor.fetchall()

            # Verificar si hay resultados
            if habitaciones_disponibles:
                print("--Mostrando las habitaciones disponibles--")
                for habitacion in habitaciones_disponibles:
                    numero, tipo, precio = habitacion
                    print(f"Número: {numero}, Tipo: {tipo}, Precio por noche: ${precio}")
            else:
                print("--No se encontraron habitaciones con ese precio.--")

        except Exception as e:
            print("--Error: la consulta no se pudo realizar.")
            print(f"Detalles del error: {e}")

        finally:
            conexion.close()

    else:
        print("--La conexión a la base de datos falló.--")

def consultar_disponibilidad_por_numero_habitacion():
    conexion = conectar_bd()

    if conexion:

        try:
            cursor = conexion.cursor()
            # Convertimos a int el número de la habitación a buscar
            numero_habitacion_consulta = int(input ("Por favor escriba el número de habitación que desea consultar"))
            query = """
                SELECT tipo_habitacion, precio_noche 
                FROM habitacion 
                WHERE estado = %s AND numero_habitacion = %s;
            """
            cursor.execute(query, ('Disponible', numero_habitacion_consulta))
            habitaciones_disponibles_por_numero = cursor.fetchone()
            if habitaciones_disponibles_por_numero:
                tipo_habitacion, precio_noche = habitaciones_disponibles_por_numero
                print(f"Tipo de habitación: {tipo_habitacion}, Precio por noche: ${precio_noche}")
            else:
                print("--No se encontró una habitación disponible con ese número.--")

        except Exception as e:
            print ("--No se pudo realizar la consulta.--")
        
        finally:
            conexion.close()

    else: 
        print ("--La conexión con la base de datos falló.--")

def menu_disponibilidad():
    while True:
        print ('=======================================================================')
        print ('Bienvenido al menu para consultar la disponibilidad de las habitaciones.')
        print ('=======================================================================')
        print ('Seleccione:')
        print ('')
        print ('Opcion 0.- Mostrar ayuda.')
        print ('Opcion 1.- Consultar todas las habitaciones que estén disponibles.')
        print ('Opcion 2.- Consultar disponibilidad por medio del tipo de habitacion.')
        print ('Opcion 3.- Consultar disponibilidad por medio del precio.')
        print ('Opcion 4.- Consultar disponibilidad por medio del numero de la habitacion.')
        print ('Opcion 5.- Salir al menu principal.')
        
        opcion = input("Seleccione una opción (0-4): ")

        if opcion == '0':
            # Función de ayuda
            print("--Esta es la sección para consultar la disponibilidad de habitaciones.--")
        elif opcion == '1':
            # Función para consultar todas las habitaciones disponibles.
            print("--Consultando todas las habitaciones disponibles.--")
            obtener_habitaciones_disponibles()
        elif opcion == '2':
            # Función para consultar por tipo de habitación
            print("--Consultando disponibilidad por tipo de habitación.--")
            obtener_habitaciones_disponibles_por_tipo()
        elif opcion == '3':
            # Función para consultar la disponibilidad por medio del precio
            print("--Consultando disponibilidad por medio del precio de la habitación.--")
            consultar_habitaciones_por_precio()
        elif opcion == '4':
            # Función para consultar disponibilidad por medio del número
            print("--Consultando disponibilidad por número de habitación.--")
            consultar_disponibilidad_por_numero_habitacion()
        elif opcion == '5':
            # Función para volver al menú principal
            print ("--Regresando al menú principal.--")
            break
        else:
            print("--Opción no válida, por favor seleccione una opción entre 0 y 4.--")



