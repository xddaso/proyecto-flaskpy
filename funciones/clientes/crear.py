from .. import conexionDB as db

def crearCliente(nombre, apellido1, apellido2, telefono):
    try:
        db.conecta()
        mycursor=db.mydb.cursor()
        sql = """INSERT INTO client (nom, cognom1, cognom2, telefon)
                    VALUES (%s, %s, %s, %s);"""
        mycursor.execute(sql, (nombre, apellido1, apellido2, telefono))
        db.mydb.commit()
        saved_id=mycursor.lastrowid
        mycursor.close()
        db.desconectar()
        return (saved_id)
    except Exception as error:
        print("Hubo un problema con la inserción de datos")
        print(error)