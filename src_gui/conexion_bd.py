import psycopg2

def conectar_bd():
    try:
        conexion = psycopg2.connect(
            host="localhost",
            database="bd",
            user="postgres",
            password="admin",
            port = "5432" 
        )
        return conexion
    except Exception as e:
        print("Error al conectar a la base de datos:", e)
        return None
