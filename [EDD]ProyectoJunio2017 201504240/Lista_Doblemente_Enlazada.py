from Nodo_ListaDoble import NodoLista
from graphviz import Digraph
g = Digraph('g', filename='ArbolUsuariosConLista.pdf', node_attr={'shape': 'record', 'style':'filled', 'fillcolor': 'seashell2','height': '.1'})

class ListaDoble:
	def __init__(self):
		self.primero=None
		self.ulitmo=None
		self.size=0

	def vacia(self):
		return self.primero==None

	def agregar_final(self,UsuarioBase,Oponente,TirosRealizados,TirosAcertados,TirosFallados,Victoria,TirosRecibidos):
		if self.vacia():
			self.primero=self.ulitmo=NodoLista(UsuarioBase,Oponente,TirosRealizados,TirosAcertados,TirosFallados,Victoria,TirosRecibidos)
		else:
			aux=self.ulitmo
			self.ulitmo=aux.siguiente=NodoLista(UsuarioBase,Oponente,TirosRealizados,TirosAcertados,TirosFallados,Victoria,TirosRecibidos)
			self.ulitmo.anterior=aux
		self.size +=1

	def agregar_inicio(self,UsuarioBase,Oponente,TirosRealizados,TirosAcertados,TirosFallados,Victoria,TirosRecibidos):
		if self.vacia():
			self.primero=self.ulitmo=NodoLista(UsuarioBase,Oponente,TirosRealizados,TirosAcertados,TirosFallados,Victoria,TirosRecibidos)
		else:
			aux=NodoLista(UsuarioBase,Oponente,TirosRealizados,TirosAcertados,TirosFallados,Victoria,TirosRecibidos)
			aux.siguiente=self.primero
			self.primero.anterior=aux
			self.primero=aux
		self.size +=1

	def recorrer_inicio_fin(self):
		aux	=self.primero
		while aux:
			print "UsuarioBase, Oponente, TirosRealizados, TirosAcertados, TirosFallados, Victoria, TirosRecibidos"
			print aux.UsuarioBase +" " + aux.Oponente +" " + aux.TirosRealizados +" " + aux.TirosAcertados +" " + aux.TirosFallados +" " + aux.Victoria +" " + aux.TirosRecibidos
			aux=aux.siguiente

	def recorrer_fin_inicio(self):
		aux=self.ulitmo
		while aux:
			print aux.dato,
			aux=aux.anterior

	def ExisteUsuario(self,UsuarioBase):
		aux=self.primero
		self.UsuarioBase=UsuarioBase
		while  aux:
			if UsuarioBase==aux.UsuarioBase:
				#print "El usuario existe"
				print aux.UsuarioBase + " -> " + '"Oponente: '+aux.Oponente +'"'+ "+" +'"TirosRealizados: '+ aux.TirosRealizados +'"'+"+" +'"TirosAcertados: '+ aux.TirosAcertados +'"'+"+" + '"TirosFallados: '+aux.TirosFallados +'"'+"+" + '"Victoria: '+aux.Victoria +'"'+"+" +'"TirosRecibidos: '+ aux.TirosRecibidos+'"'
				g.edge(aux.UsuarioBase,"Oponente--"+aux.Oponente+"\n"+"Tiros Realizados--"+aux.TirosRealizados+"\n"+"Tiros Acertados--"+aux.TirosAcertados+"\n"+"Tiros Fallados--"+aux.TirosFallados+"\n"+"Victoria--"+aux.Victoria+"\n"+"Tiros Recibidos--"+aux.TirosRecibidos,aux.Oponente)
				aux=aux.siguiente
			else:
				aux=aux.siguiente
				if aux==self.ulitmo:
					print "El usuario no existe"
	
	def graficar(self):	
		g.view()