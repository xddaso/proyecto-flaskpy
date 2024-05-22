from .. import conexionDB as db

def borrarCliente(id):
    try:
        db.conecta()
        mycursor=db.mydb.cursor()
        sql = "DELETE FROM client WHERE id=%s"
        mycursor.execute(sql, (id,))
        db.mydb.commit()
        mycursor.close()
        db.desconectar()
    except Exception as error:
        print("Hubo un problema con el borrado de datos")
        print(error)