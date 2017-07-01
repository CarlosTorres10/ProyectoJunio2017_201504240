#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
from Arbol_ABB import ArbolABB
from Nodo_Arbol_Espejo import Nodo
from Arbol_Binario_Busqueda_Espejo import arbolBinario
from flask import Flask, request, Response
from ListaDoblePrueba import ListaDoblePruebas

app = Flask("EDD_ProyectoJunio2017")
Arbol=ArbolABB()
ArbolEspejo=arbolBinario()
ListaDoble=ListaDoblePruebas()

os.system('cls')
@app.route("/")
def hellof():
	return "WEB ACTIVO"

@app.route("/insertarEnABB", methods=['POST'])
def insertarABB():
	Arbol.Insertar(str(request.form['Usuario']),str(request.form['Password']),str(request.form['Conectado']))
	print (Arbol.Recorrido_EnOrden(Arbol.root))
	return "TRUE"

@app.route("/buscarEnABB", methods=['POST'])
def buscarABB():
	return Arbol.Buscar(Arbol.root,str(request.form['Usuario']))

@app.route("/validarLogin", methods=['POST'])
def validarLogin():
	return Arbol.ValidarLogin(Arbol.root,str(request.form['Usuario']),str(request.form['Password']))

@app.route("/graficarUsuarios", methods=['POST'])
def graficarUsuarios():
	return ArbolEspejo.graficarUsuarios()

@app.route("/LlenarListaDoble",methods=['POST'])
def LlenarListaDoble():
	ListaDoble.agregar_final(str(request.form['UsuarioBase']),str(request.form['Oponente']),str(request.form['TirosRealizados']),str(request.form['TirosAcertados']),str(request.form['TirosFallados']),str(request.form['Victoria']),str(request.form['TirosRecibidos']))
	#ListaDoble.recorrer_inicio_fin()
	return "Lista Llenadad con exito!!!"

@app.route("/graficarUsuariosConListas", methods=['POST'])
def graficarUsuariosConListas():
	ArbolEspejo.graficarUsuariosConListas()
	return "TRUE"
	


if __name__ == "__main__":
  app.run(debug=True)

#Arbol=ArbolABB()
#Arbol.Insertar("carlos",123,0)
#Arbol.Recorrido_EnOrden(Arbol.root)
#print(Arbol.Buscar(Arbol.root,144))