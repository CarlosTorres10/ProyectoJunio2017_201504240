class Nodo:
	def __init__(self, usuario=None, password=None, conexion=None, izq=None, der=None):
		self.usuario=usuario
		self.password=password
		self.conexion=conexion
		self.ListaDoble=None
		self.izq=izq
		self.der=der
		#self.id=correlativo+correlativo

	def setListaDoble(self,ListaDoble):
		self.ListaDoble=ListaDoble

	def getListaDoble(self):
		return self.ListaDoble