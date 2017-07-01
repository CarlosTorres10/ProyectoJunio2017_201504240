from NodoArbolPrueba import Nodo
from ListaDoblePrueba import ListaDoblePruebas
from graphviz import Digraph
archivo=open("UsuariosConListas.txt","w")
archivo.write("digraph grafica{\n" + "rankdir=TB;\n" + "node [shape = record, style=filled, fillcolor=seashell2];\n" ) 

#g = Digraph('g', filename='ArbolUsuarios', node_attr={'shape': 'record', 'style':'filled', 'fillcolor': 'seashell2','height': '.1'})

class arbolBinario:
	def __init__(self):
		self.raiz=None
		self.contador=0
		self.contadorraiz=0
		self.g=Digraph('g', filename='ArbolUsuarios55', node_attr={'shape': 'record', 'style':'filled', 'fillcolor': 'seashell2','height': '.1'})



	def agregar(self,elemento):
		#print elemento.ListaDoble.primero.UsuarioBase
		#print elemento.ListaDoble.ulitmo
		#aux=elemento.ListaDoble.primero 
		#while aux!=None
		if self.raiz==None:
			self.raiz=elemento
		else:
			aux=self.raiz
			padre=None
			while aux!=None:
				padre=aux
				if elemento.usuario>= aux.usuario:
					aux=aux.der	
				else:
					aux=aux.izq
			#print self.contadorraiz
			if self.contadorraiz==0:
				if elemento.usuario <= padre.usuario:
					padre.izq=elemento
					print padre.usuario+'->'+elemento.usuario
					archivo.write(padre.usuario+'->'+elemento.usuario+'\n')
					self.ExisteUsuario(elemento,padre.usuario)
					self.setcontadorraiz(1)
					#self.g.edge(padre.usuario, elemento.usuario)
					#self.Listaa.ExisteUsuario(padre.usuario)

				else:
					padre.der=elemento
					print padre.usuario+'->'+elemento.usuario
					archivo.write(padre.usuario+'->'+elemento.usuario+'\n')
					self.ExisteUsuario(elemento,padre.usuario)
					self.setcontadorraiz(1)
			else:
				if elemento.usuario <= padre.usuario:
					padre.izq=elemento
					print padre.usuario+'->'+elemento.usuario
					archivo.write(padre.usuario+'->'+elemento.usuario+'\n')
					self.ExisteUsuario(elemento,elemento.usuario)
					#self.g.edge(padre.usuario, elemento.usuario)
					#self.Listaa.ExisteUsuario(padre.usuario)

				else:
					padre.der=elemento
					print padre.usuario+'->'+elemento.usuario
					archivo.write(padre.usuario+'->'+elemento.usuario+'\n')
					self.ExisteUsuario(elemento,elemento.usuario)
		
				#self.g.edge(padre.usuario, elemento.usuario)
			#self.ExisteUsuario(elemento,padre.usuario)
		#archivo.close()
	def setcontadorraiz(self,valor):
		self.contadorraiz=valor

	def ExisteUsuario(self,elemento,UsuarioBase):
		aux=elemento.ListaDoble.primero
		#self.UsuarioBase=UsuarioBase
		while  aux:
			print "Usuario Base: "+aux.UsuarioBase+" Usuario Comparacion: "+UsuarioBase
			if UsuarioBase==aux.UsuarioBase:
				
				if (self.contador==0):
					#print aux.UsuarioBase + " -> " + '"Oponente--'+aux.Oponente +'"'+ "+" +'"\\nTirosRealizados--'+ aux.TirosRealizados +'"'+"+" +'"\\nTirosAcertados--'+ aux.TirosAcertados +'"'+"+" + '"\\nTirosFallados--'+aux.TirosFallados +'"'+"+" + '"\\nVictoria--'+aux.Victoria +'"'+"+" +'"\\nTirosRecibidos--'+ aux.TirosRecibidos+'"',
					archivo.write(aux.UsuarioBase + " -> " + '"Oponente--'+aux.Oponente +'"'+ "+" +'"\\nTirosRealizados--'+ aux.TirosRealizados +'"'+"+" +'"\\nTirosAcertados--'+ aux.TirosAcertados +'"'+"+" + '"\\nTirosFallados--'+aux.TirosFallados +'"'+"+" + '"\\nVictoria--'+aux.Victoria +'"'+"+" +'"\\nTirosRecibidos--'+ aux.TirosRecibidos+'"\n')
					aux=aux.siguiente
					self.contador +=1
				else:
					#print " -> " + '"Oponente--'+aux.Oponente +'"'+ "+" +'"\nTirosRealizados--'+ aux.TirosRealizados +'"'+"+" +'"\nTirosAcertados--'+ aux.TirosAcertados +'"'+"+" + '"\nTirosFallados--'+aux.TirosFallados +'"'+"+" + '"\nVictoria--'+aux.Victoria +'"'+"+" +'"\nTirosRecibidos--'+ aux.TirosRecibidos+'"',
					archivo.write(" -> " + '"Oponente--'+aux.Oponente +'"'+ "+" +'"\\nTirosRealizados--'+ aux.TirosRealizados +'"'+"+" +'"\\nTirosAcertados--'+ aux.TirosAcertados +'"'+"+" + '"\\nTirosFallados--'+aux.TirosFallados +'"'+"+" + '"\\nVictoria--'+aux.Victoria +'"'+"+" +'"\\nTirosRecibidos--'+ aux.TirosRecibidos+'"\n')
					aux=aux.siguiente
					self.contador +=1
				#g.edge(aux.UsuarioBase,"Oponente--"+aux.Oponente+"\n"+"Tiros Realizados--"+aux.TirosRealizados+"\n"+"Tiros Acertados--"+aux.TirosAcertados+"\n"+"Tiros Fallados--"+aux.TirosFallados+"\n"+"Victoria--"+aux.Victoria+"\n"+"Tiros Recibidos--"+aux.TirosRecibidos,aux.Oponente)
				#arbol.g.edge(aux.UsuarioBase,"Oponente--"+aux.Oponente+"\n"+"Tiros Realizados--"+aux.TirosRealizados+"\n"+"Tiros Acertados--"+aux.TirosAcertados+"\n"+"Tiros Fallados--"+aux.TirosFallados+"\n"+"Victoria--"+aux.Victoria+"\n"+"Tiros Recibidos--"+aux.TirosRecibidos,aux.Oponente)
			else:
				aux=aux.siguiente
				#if aux==None:
				#	print "Termino el recorrido de la lista de la lista"
		self.contador=0	
	
	def buscar(self,usuario):
		Lista.ExisteUsuario(usuario)
		#self.Listaa.ExisteUsuario(padre.usuario)

	def Recorrido_EnOrden(self,node):
		# izquierda -> raiz -> derecha
		if node!=None:
			self.Recorrido_EnOrden(node.izq)
			print str(node.usuario)
			Lista.ExisteUsuario(node.usuario)
			self.Recorrido_EnOrden(node.der)

	def getRaiz(self):
		return self.raiz

	def graficarUsuarios(self):
		archivo.write("\n"+"}")
		archivo.close()
		#self.g.view()
		#return "TRUE"

	def cerrarArchivo(self):
		archivo.write("\n"+"}")
		archivo.close()

	def agregar2(self,elemento):
		#print elemento.ListaDoble.primero.UsuarioBase
		#print elemento.ListaDoble.ulitmo
		#aux=elemento.ListaDoble.primero 
		#while aux!=None
		if self.raiz==None:
			self.raiz=elemento
		else:
			aux=self.raiz
			padre=None
			while aux!=None:
				padre=aux
				if elemento.usuario>= aux.usuario:
					aux=aux.der	
				else:
					aux=aux.izq
			if elemento.usuario <= padre.usuario:
				padre.izq=elemento
				print padre.usuario+'->'+elemento.usuario
				
				self.ExisteUsuario(elemento,elemento.usuario)
				archivo.write(padre.usuario+'->'+elemento.usuario+'\n')
				
				#self.g.edge(padre.usuario, elemento.usuario)
				#self.Listaa.ExisteUsuario(padre.usuario)

			else:
				padre.der=elemento
				print padre.usuario+'->'+elemento.usuario
				self.ExisteUsuario(elemento,elemento.usuario)
				archivo.write(padre.usuario+'->'+elemento.usuario+'\n')
				