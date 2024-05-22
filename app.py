##!/usr/bin/env python3

import logging
from flask import Flask, request, redirect, abort, render_template, url_for, flash
import funciones.clientes.listado as cli
import funciones.clientes.lectura as cliL
import funciones.clientes.actualizar as cliA
import funciones.clientes.borrar as cliB
import funciones.clientes.crear as cliC
app = Flask(__name__)

# Defineix el nivell per defecte de log
app.logger.setLevel(logging.INFO)

#SECRET_KEY: clau d'encriptació de la cookie
app.config.update(
    SECRET_KEY='secret_xxx'
)
@app.route("/")
def home():
    return render_template('index.html')

@app.route('/hello')
@app.route('/hello/<name>')
def hello(name=None):
    # Get value from URL
    return render_template('hello.html', name=name)

@app.route('/hello2')
def hello2():
    # Get value from URL query param
    # /hello2?alias=xxx
    param = request.args.get('alias')
    return render_template('hello.html', alias=param)

@app.route('/resource/create', methods=["GET", "POST"])
def resource_create():
    if request.method == 'GET':
        # Show form
        return render_template('resource/create.html')
    elif request.method == 'POST':
        # Get POST data
        nombre = request.form['nombre']
        apellido1 = request.form['apellido1']
        apellido2 = request.form['apellido2']
        telefono = request.form['telefono']
        saved_id=cliC.crearCliente(nombre, apellido1, apellido2, telefono)
        # Redirect to show page
        return redirect(url_for('resource_read', id=saved_id))
    else:
        # Not found response
        abort(404)

@app.route('/resource/read/<int:id>')
def resource_read(id):
    # TODO Get data (database select)
    data=cliL.lecturaCliente(id)
    # data = {
    #     'id': 1234,
    #     'field1': 'Value1',
    #     'field2': 'Value2',
    #     'field3': 'Value3'
    # }
    # Show data
    return render_template('resource/read.html',resource=data)

@app.route('/resource/update/<int:id>', methods=["GET", "POST"])
def resource_update(id):
    if request.method == 'GET':
        data=cliL.lecturaCliente(id)
        return render_template('resource/update.html',resources=data)
    elif request.method == 'POST':
        nombre = request.form['nombre']
        apellido1 = request.form['apellido1']
        apellido2 = request.form['apellido2']
        telefono = request.form['telefono']
        cliA.actualizarCliente(id,nombre,apellido1,apellido2,telefono)
        return render_template('resource/redirect.html')

@app.route('/resource/delete/<int:id>', methods=["GET", "POST"])
def resource_delete(id):
    if request.method == 'GET':
        return render_template('resource/delete.html',id=id)
    elif request.method == 'POST':
        confirmar=request.form.getlist('confirmar') # Obtener si el usuario marca o no el checkbox
        if confirmar:
            cliB.borrarCliente(id)
            return render_template('resource/redirect.html')
        else:
            return render_template('resource/cancelar.html')

@app.route('/resource/list')
def resource_list():
    # TODO Get data (database select)
    data=cli.listadoClientes()
    # data = [{
    #     'id': 1234,
    #     'field1': 'Value A1',
    #     'field2': 'Value A2',
    #     'field3': 'Value A3'
    # }, {
    #     'id': 5678,
    #     'field1': 'Value B1',
    #     'field2': 'Value B2',
    #     'field3': 'Value B3'
    # }]
    # Show data
    return render_template('resource/list.html',results=data)

@app.route("/contacte", methods = ["GET", "POST"])
def contacte():
    if request.method == 'GET':
        # Show form
        return render_template('contacte.html')
    elif request.method == 'POST':
        # Get POST data
        data = request.form
        email = data.get("email-contacte") 

        app.logger.info(f"Comentaris de {email}")
        # TODO: Add more logs 

        # Flash message to inform the user
        flash(f"En breu rebreu resposta a {email}")
        return redirect(url_for('thanks'))

@app.route("/thanks-for-your-comments") # default is GET
def thanks():
    return render_template('contacte-thanks.html')

# Run this application in debug mode ap port 5001
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=True)