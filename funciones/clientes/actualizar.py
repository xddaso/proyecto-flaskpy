from .. import conexionDB as db

def actualizarCliente(id,nombre,apellido1,apellido2,telefono):
    try:
        db.conecta()
        mycursor=db.mydb.cursor()
        sql = """UPDATE client
                SET nom=%s, cognom1=%s, cognom2=%s, telefon=%s
                WHERE id=%s;
                """
        mycursor.execute(sql, (nombre, apellido1, apellido2, telefono, id))
        db.mydb.commit()
        mycursor.close()
        db.desconectar()
    except Exception as error:
        print("Hubo un problema con la actualización de los datos")
        print(error)

