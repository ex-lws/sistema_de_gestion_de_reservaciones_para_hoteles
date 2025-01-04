def mostrarHabitaciones():

    lista_habitaciones = {

        'Habitacion 101' : {
            'Tipo' : 'Sencilla', 
            'Características' : ['TV', 'Baño', 'Cama king'], 
            'Precio' : 450},

        'Habitacion 102' : {
            'Tipo' : 'Sencilla', 
            'Características' : ['TV', 'Baño', 'Cama queen'], 
            'Precio' : 400},

        'Habitacion 103' : {
            'Tipo' : 'Sencilla', 
            'Características' : ['TV', 'Baño', 'Cama individual'], 
            'Precio' : 350},

        'Habitacion 104' : {
            'Tipo' : 'Sencilla', 
            'Características' : ['TV', 'Baño', 'Cama individual'], 
            'Precio' : 350},

        'Habitacion 105' : {
            'Tipo' : 'Doble', 
            'Características' : ['TV', 'Baño amplio', 'Comedor', 'Dos camas king', 'Wi-Fi'], 
            'Precio' : 850},

        'Habitacion 106' : {
            'Tipo' : 'Doble', 
            'Características' : ['TV', 'Baño amplio', 'Comedor', 'Dos camas individuales', 'Wi-Fi'], 
            'Precio' : 830},

        'Habitacion 201' : {
            'Tipo' : 'Suite', 
            'Características' : ['TV grande', 'Jacuzzi', 'Comedor','Cama king y sofá cama', 'Wi-Fi', 'Sistema de sonido'], 
            'Precio' : 1600},

        'Habitacion 202' : {
            'Tipo' : 'Suite', 
            'Características' : ['TV grande', 'Jacuzzi', 'Comedor','Cama queen y sofá cama', 'Wi-Fi', 'Sistema de sonido'], 
            'Precio' : 1500},

        'Habitacion 203' : {
            'Tipo' : 'Suite', 
            'Características' : ['TV grande', 'Jacuzzi', 'Comedor','Cama individual y sofá cama', 'Wi-Fi', 'Sistema de sonido'], 
            'Precio' : 1400},

        'Habitacion 204' : {
            'Tipo' : 'Familiar', 
            'Características' : ['TV grande', 'Baño amplio', 'Comedor','Dos camas individuales' , 'Wi-Fi', 'Sistema de sonido', 'Juegos de actividades para niños'],
            'Precio' : 1700},

        'Habitacion 205' : {
            'Tipo' : 'Familiar', 
            'Características' :  ['TV grande', 'Jacuzzi', 'Comedor','Dos camas individuales' , 'Wi-Fi', 'Sistema de sonido', 'Juegos de actividades para niños'],
            'Precio' : 1800},

        'Habitacion 206' : {
            'Tipo' : 'Familiar', 
            'Características' : ['TV grande', 'Jacuzzi y baño', 'Comedor','Dos camas individuales' , 'Wi-Fi', 'Sistema de sonido', 'Juegos de actividades para niños'], 
            'Precio' : 1900},

        'Habitacion 301' : {
            'Tipo' : 'Deluxe', 
            'Características' : ['TV grande', 'Jacuzzi y baño', 'Comedor','Cama king' , 'Wi-Fi', 'Sistema de sonido', 'Mini bar', 'Calefacción'], 
            'Precio' : 2600},

        'Habitacion 302' : {
            'Tipo' : 'Deluxe', 
            'Características' : ['TV grande', 'Jacuzzi y baño', 'Comedor','Cama queen' , 'Wi-Fi', 'Sistema de sonido', 'Mini bar', 'Calefacción'], 
            'Precio' : 2500},

        'Habitacion 303' : {
            'Tipo' : 'Deluxe', 
            'Características' : ['TV grande', 'Jacuzzi y baño', 'Comedor','Cama queen' , 'Wi-Fi', 'Sistema de sonido', 'Mini bar', 'Calefacción'],
            'Precio' : 2500},

        'Habitacion 304' : {
            'Tipo' : 'Suite precidencial', 
            'Características' : ['TV grande', 'Jacuzzi y baño', 'Comedor','Cama king' , 'Wi-Fi de alta velocidad', 'Sistema de sonido premium', 'Mini bar', 'Calefacción', 'Balcón'],
            'Precio' : 3400},

        'Habitacion 305' : {
            'Tipo' : 'Suite precidencial', 
            'Características' : ['TV grande', 'Jacuzzi y baño', 'Comedor','Cama king' , 'Wi-Fi de alta velocidad', 'Sistema de sonido premium', 'Mini bar', 'Calefacción', 'Balcón'], 
            'Precio' : 3400},

        'Habitacion 306' : {
            'Tipo' : 'Suite precidencial', 
            'Características' : ['TV grande', 'Jacuzzi y baño', 'Comedor','Cama king' , 'Wi-Fi de alta velocidad', 'Sistema de sonido premium', 'Mini bar', 'Calefacción', 'Balcón'], 
            'Precio' : 3400},

        }

     # Mostrar todas las habitaciones disponibles en el hotel
    print("Mostrando todas las habitaciones disponibles:")
    print('\n')

    for numero, detalles in lista_habitaciones.items():
        print(f'Número: {numero}')
        print(f"Tipo: {detalles['Tipo']}")
        print(f'Características: {", ".join(detalles["Características"])}')
        print(f'Precio: ${detalles["Precio"]}')
        print('\n')
