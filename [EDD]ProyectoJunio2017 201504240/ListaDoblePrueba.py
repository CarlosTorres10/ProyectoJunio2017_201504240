from NodoListaDoblePrueba import NodoListaDoble
from graphviz import Digraph
#archivo=open("UsuariosListas.txt","w")
#from ArbolPrueba import arbolBinario
#g = Digraph('g', filename='ArbolUsuariosConLista.pdf', node_attr={'shape': 'record', 'style':'filled', 'fillcolor': 'seashell2','height': '.1'})
#arbol=arbolBinario()
class ListaDoblePruebas:
	def __init__(self):
		self.primero=None
		self.ulitmo=None
		self.size=0
		self.contador=0
		#self.arbolito=arbol


	def vacia(self):
		return self.primero==None

	def agregar_final(self,UsuarioBase,Oponente,TirosRealizados,TirosAcertados,TirosFallados,Victoria,TirosRecibidos):
		if self.vacia():
			self.primero=self.ulitmo=NodoListaDoble(UsuarioBase,Oponente,TirosRealizados,TirosAcertados,TirosFallados,Victoria,TirosRecibidos)
			print "UsuarioBase: "+UsuarioBase+" Oponente: "+Oponente+" TirosRealizados: "+TirosRealizados+" TirosAcertados: "+TirosAcertados+" TirosFallados: "+TirosFallados+" Victoria: "+Victoria+" TirosRecibidos: "+TirosRecibidos
		else:
			print "UsuarioBase: "+UsuarioBase+" Oponente: "+Oponente+" TirosRealizados: "+TirosRealizados+" TirosAcertados: "+TirosAcertados+" TirosFallados: "+TirosFallados+" Victoria: "+Victoria+" TirosRecibidos: "+TirosRecibidos
			aux=self.ulitmo
			self.ulitmo=aux.siguiente=NodoListaDoble(UsuarioBase,Oponente,TirosRealizados,TirosAcertados,TirosFallados,Victoria,TirosRecibidos)
			self.ulitmo.anterior=aux
		self.size +=1

	def agregar_inicio(self,UsuarioBase,Oponente,TirosRealizados,TirosAcertados,TirosFallados,Victoria,TirosRecibidos):
		if self.vacia():
			self.primero=self.ulitmo=NodoListaDoble(UsuarioBase,Oponente,TirosRealizados,TirosAcertados,TirosFallados,Victoria,TirosRecibidos)
		else:
			aux=NodoListaDoble(UsuarioBase,Oponente,TirosRealizados,TirosAcertados,TirosFallados,Victoria,TirosRecibidos)
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
				if (self.contador==0):
					print aux.UsuarioBase + " -> " + '"Oponente--'+aux.Oponente +'"'+ "+" +'"TirosRealizados--'+ aux.TirosRealizados +'"'+"+" +'"TirosAcertados--'+ aux.TirosAcertados +'"'+"+" + '"TirosFallados--'+aux.TirosFallados +'"'+"+" + '"Victoria--'+aux.Victoria +'"'+"+" +'"TirosRecibidos--'+ aux.TirosRecibidos+'"',
				#	archivo.write(aux.UsuarioBase + " -> " + '"Oponente--'+aux.Oponente +'"'+ "+" +'"TirosRealizados--'+ aux.TirosRealizados +'"'+"+" +'"TirosAcertados--'+ aux.TirosAcertados +'"'+"+" + '"TirosFallados--'+aux.TirosFallados +'"'+"+" + '"Victoria--'+aux.Victoria +'"'+"+" +'"TirosRecibidos--'+ aux.TirosRecibidos+'"')
					self.contador +=1
				else:
					print " -> " + '"\nOponente--'+aux.Oponente +'"'+ "+" +'"\nTirosRealizados--'+ aux.TirosRealizados +'"'+"+" +'"\nTirosAcertados--'+ aux.TirosAcertados +'"'+"+" + '"\nTirosFallados--'+aux.TirosFallados +'"'+"+" + '"\nVictoria--'+aux.Victoria +'"'+"+" +'"\nTirosRecibidos--'+ aux.TirosRecibidos+'"',
				#	archivo.write(" -> " + '"Oponente--'+aux.Oponente +'"'+ "+" +'"TirosRealizados--'+ aux.TirosRealizados +'"'+"+" +'"TirosAcertados--'+ aux.TirosAcertados +'"'+"+" + '"TirosFallados--'+aux.TirosFallados +'"'+"+" + '"Victoria--'+aux.Victoria +'"'+"+" +'"TirosRecibidos--'+ aux.TirosRecibidos+'"')
					self.contador +=1
				#g.edge(aux.UsuarioBase,"Oponente--"+aux.Oponente+"\n"+"Tiros Realizados--"+aux.TirosRealizados+"\n"+"Tiros Acertados--"+aux.TirosAcertados+"\n"+"Tiros Fallados--"+aux.TirosFallados+"\n"+"Victoria--"+aux.Victoria+"\n"+"Tiros Recibidos--"+aux.TirosRecibidos,aux.Oponente)
				#arbol.g.edge(aux.UsuarioBase,"Oponente--"+aux.Oponente+"\n"+"Tiros Realizados--"+aux.TirosRealizados+"\n"+"Tiros Acertados--"+aux.TirosAcertados+"\n"+"Tiros Fallados--"+aux.TirosFallados+"\n"+"Victoria--"+aux.Victoria+"\n"+"Tiros Recibidos--"+aux.TirosRecibidos,aux.Oponente)
				aux=aux.siguiente
			else:
				aux=aux.siguiente
				if aux==self.ulitmo:
					print "El usuario no existe"
		self.contador=0	
	
	#def graficar(self):
		#archivo.close()	
		#g.view()