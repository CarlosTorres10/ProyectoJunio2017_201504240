from Nodo_ABB import Node
from Nodo_Arbol_Espejo import Nodo
from Arbol_Binario_Busqueda_Espejo import arbolBinario
from ListaDoblePrueba import ListaDoblePruebas

import os

ListaDoblee=ListaDoblePruebas()
AB=arbolBinario()
archivo=open("ArbolABBC.txt","w")


class ArbolABB:
	def __init__(self):
		self.root=None
		self.contador=0
		self.contador2=0

	def vacio(self):
		if self.root==None:
			return True
		else:
			return False

	def Insertar(self,usuario,password,conectado):
		if self.vacio():
			self.root=Node(usuario=usuario, password=password, conectado=conectado, is_root=True)
			NodoArbol=Nodo(usuario,password,conectado)
			NodoArbol.setListaDoble(ListaDoblee)
			AB.agregar(NodoArbol)
		else:
			node=self.__get_place(usuario,password,conectado)
			if usuario<=node.usuario:
				node.left=Node(usuario=usuario, password=password, conectado=conectado, parent=node, is_left=True)
				NodoArbol=Nodo(usuario,password,conectado)
				NodoArbol.setListaDoble(ListaDoblee)
				AB.agregar(NodoArbol)
			else:
				node.right=Node(usuario=usuario, password=password, conectado=conectado, parent=node, is_right=True)
				NodoArbol=Nodo(usuario,password,conectado)
				NodoArbol.setListaDoble(ListaDoblee)
				AB.agregar(NodoArbol)

	def __get_place(self,usuario,password,conectado):
		aux=self.root
		while aux:
			temp=aux
			if usuario<=aux.usuario:
				aux=aux.left
			else:
				aux=aux.right
		return temp

	def Recorrido_EnOrden(self,node):
		# izquierda -> raiz -> derecha
		if node:
			self.Recorrido_EnOrden(node.left)
			print("Nombre de usuario: "+node.usuario," Password: "+node.password," Conexion Actual: "+node.conectado)
			self.Recorrido_EnOrden(node.right)

	def Recorrido_PreOrden(self,node):
		# raiz -> izquierda -> derecha
		if node:
			print(node.usuario)
			self.Recorrido_PreOrden(node.left)
			self.Recorrido_PreOrden(node.right)

	def Recorrido_PosOrden(self,node):
		# izquierda -> derecha -> raiz
		if node:
			self.Recorrido_PosOrden(node.left)
			self.Recorrido_PosOrden(node.right)
			print(node.usuario)

	def Buscar(self, node, usuario):	
		# Si el dato no existe.
		if node==None:
			return "FALSE"
		else:
			#Si el dato existe.
			if node.usuario==usuario:
				print "usuario existente,sesion iniciada"
				return "TRUE"
			#Recursividad con recorrido en izquierda
			elif usuario<=node.usuario:
				return self.Buscar(node.left,usuario)
			#Recursividad con recorrido en derecha
			else:
				return self.Buscar(node.right,usuario)

	def ValidarLogin(self, node, usuario, password):	
		# Si el dato no existe.
		if node==None:
			print "Datos incorrectos"
			return "FALSE"
		else:
			#Si el dato existe.
			if node.usuario==usuario and node.password==password:
				print "Sesion iniciada, usuario: "+ node.usuario + " Contrasena: "+ node.password
				return "TRUE"
			#Recursividad con recorrido en izquierda
			elif usuario<=node.usuario:
				return self.Buscar(node.left,usuario)
			#Recursividad con recorrido en derecha
			else:
				return self.Buscar(node.right,usuario)
