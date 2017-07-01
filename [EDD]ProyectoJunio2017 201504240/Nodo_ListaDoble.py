class NodoLista:
	def __init__(self,UsuarioBase,Oponente,TirosRealizados,TirosAcertados,TirosFallados,Victoria,TirosRecibidos):
		self.UsuarioBase=UsuarioBase
		self.Oponente=Oponente
		self.TirosRealizados=TirosRealizados
		self.TirosAcertados=TirosAcertados
		self.TirosFallados=TirosFallados
		self.Victoria=Victoria
		self.TirosRecibidos=TirosRecibidos
		self.siguiente=None
		self.anterior=None