import mysql.connector

def conecta():
    try:
        print("Abriendo la conexion a la BD...")
        global mydb
        mydb = mysql.connector.connect(
            host="shared.daw.cat",
            user="1aa01",
            password="1ASIXdaw*01",
            port="3306",
            database="1aa01_gestor_negocis"
            # host="localhost",
            # user="fran",
            # password="fran",
            # port="3306",
            # database="1aa01_gestor_negocis"
        )
    except Exception as error:
        print("Hubo un problema con la conexión a la base de datos")
        print(error)

def desconectar():
    try:
        print("Cerrando la conexión a la BD...")
        mydb.close()
    except Exception as error:
        print("Hubo un problema al intentar cerrar la conexión a la base de datos")
        print(error)