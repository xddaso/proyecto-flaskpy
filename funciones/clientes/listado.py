from .. import conexionDB as db

def listadoClientes():
    try:
        db.conecta()
        clientes=list()
        mycursor=db.mydb.cursor()
        mycursor.execute("SELECT * FROM client")
        myresult=mycursor.fetchall()
        for c in myresult:
            cli={"id":c[0], "nombre":c[1], "apellido1":c[2], "apellido2":c[3], "teléfono":c[4]}
            clientes.append(cli)
        mycursor.close()
        db.desconectar()
        return clientes
    except Exception as error:
        print("Hubo un problema al intentar mostrar los datos")
        print(error)