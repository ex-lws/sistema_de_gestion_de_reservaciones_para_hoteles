# Conexión a la base de datos
# Versión 1.0
# Fecha: 18/10/2024
# Autor: Reyes Cruz Luis Alberto

# Esta clase tiene como finalidad modular la conexión de la base de datos.

import psycopg2
from psycopg2 import OperationalError

def check_connection():
    # Parámetros de conexión
    host = "localhost"
    dbname = "bd_reservaciones" 
    user = "postgres"  
    password = "admin"
    port = "5432"  

    try:
        # Intenta realizar la conexión
        connection = psycopg2.connect(
            host=host,
            dbname=dbname,
            user=user,
            password=password,
            port=port
        )

        # Si la conexión es exitosa
        print("Conexión exitosa a la base de datos PostgreSQL")
        
        # Cierra la conexión
        connection.close()

    except OperationalError as e:
        # Si hay un error, lo captura
        print(f"Error al conectar a la base de datos: {e}")

check_connection()
