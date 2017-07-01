from Nodo_Arbol_Espejo import Nodo
from graphviz import Digraph

archivo=open("ArbolUsuariosConListas.txt","w")
archivo.write("digraph grafica{\n" + "rankdir=TB;\n" + "node [shape = record, style=filled, fillcolor=seashell2];\n" ) 
g = Digraph('g', filename='ArbolUsuarios', node_attr={'shape': 'record', 'style':'filled', 'fillcolor': 'seashell2','height': '.1'})

class arbolBinario:
	def __init__(self):
		self.raiz=None
		self.contador=0
		self.contadorraiz=0


	def agregar(self,elemento):
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
			if self.contadorraiz==0:
				if elemento.usuario <= padre.usuario:
					padre.izq=elemento
					print padre.usuario+'->'+elemento.usuario
					g.edge(padre.usuario, elemento.usuario)
					#archivo.write(padre.usuario+'->'+elemento.usuario+'\n')
					self.ExisteUsuario(elemento,padre.usuario)
					self.setcontadorraiz(1)
					#self.g.edge(padre.usuario, elemento.usuario)
					#self.Listaa.ExisteUsuario(padre.usuario)

				else:
					padre.der=elemento
					print padre.usuario+'->'+elemento.usuario
					g.edge(padre.usuario, elemento.usuario)
					#archivo.write(padre.usuario+'->'+elemento.usuario+'\n')
					self.ExisteUsuario(elemento,padre.usuario)
					self.setcontadorraiz(1)
			else:
				if elemento.usuario <= padre.usuario:
					padre.izq=elemento
					print padre.usuario+'->'+elemento.usuario
					g.edge(padre.usuario, elemento.usuario)
					#archivo.write(padre.usuario+'->'+elemento.usuario+'\n')
					self.ExisteUsuario(elemento,elemento.usuario)
					#self.g.edge(padre.usuario, elemento.usuario)
					#self.Listaa.ExisteUsuario(padre.usuario)

				else:
					padre.der=elemento
					print padre.usuario+'->'+elemento.usuario
					g.edge(padre.usuario, elemento.usuario)
					#archivo.write(padre.usuario+'->'+elemento.usuario+'\n')
					self.ExisteUsuario(elemento,elemento.usuario)
			#if elemento.usuario <= padre.usuario:
			#	padre.izq=elemento
			#	print padre.usuario+'->'+elemento.usuario
			#	g.edge(padre.usuario, elemento.usuario)
			#else:
			#	padre.der=elemento
			#	print padre.usuario+'->'+elemento.usuario
			#	g.edge(padre.usuario, elemento.usuario)

	def setcontadorraiz(self,valor):
		self.contadorraiz=valor

	def graficarUsuariosConListas(self):
		archivo.write("\n"+"}")
		archivo.close()	

	def Recorrido_EnOrden(self,node):
		# izquierda -> raiz -> derecha
		if node!=None:
			self.Recorrido_EnOrden(node.izq)
			print str(node.usuario)
			self.Recorrido_EnOrden(node.der)

	def getRaiz(self):
		return self.raiz

	def graficarUsuarios(self):
		g.view()
		return "TRUE"

	def ExisteUsuario(self,elemento,UsuarioBase):
		aux=elemento.ListaDoble.primero
		#self.UsuarioBase=UsuarioBase
		while  aux:
			#print "Usuario Base: "+aux.UsuarioBase+" Usuario Comparacion: "+UsuarioBase
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
				if aux==None:
					print "Termino el recorrido de la lista de la lista"
		self.contador=0	
