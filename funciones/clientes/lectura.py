from .. import conexionDB as db

def lecturaCliente(id):
    try:
        db.conecta()
        mycursor=db.mydb.cursor()
        mycursor.execute(f"SELECT * FROM client WHERE id={id}")
        myresult=mycursor.fetchall()
        for c in myresult:
            cliente={"id":c[0], "nombre":c[1], "apellido1":c[2], "apellido2":c[3], "teléfono":c[4]}
        mycursor.close()
        db.desconectar()
        return cliente
    except Exception as error:
        print("Hubo un problema al intentar seleccionar el cliente")
        print(error)
