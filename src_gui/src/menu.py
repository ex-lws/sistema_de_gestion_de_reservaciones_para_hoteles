def mostrarOpciones():

    print("============================================")
    print("Bienvenido al sistema de gestión de hoteles.")
    print("============================================")
    print("Opcion 0.- Mostrar ayuda")
    print("Opcion 1.- Mostrar todas las habitaciones")
    print("Opcion 2.- Mostrar estado de disponibilidad de las habitaciones")
    print("Opcion 3.- Inicar proceso de reservación")
    print("Opcion 4.- Consultar reportes de reservación")
    print("Opcion 5.- Estadísticas operacionales")
    print("Opcion 6.- Salir")

def opcionUsuario():
    while True:
        try:
            #Guardar la selección del usuario
            opcion_usuario = int(input("Seleccione una opción del 0 - 6: "))
            print("Usted seleccionó: " + str(opcion_usuario))
            return opcion_usuario
            #En caso de que no seleccioné algún valor númerico
        except ValueError:
            print("Por favor, introduzca un número válido entre 0 y 6.")

