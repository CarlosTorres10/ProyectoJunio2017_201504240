class Node:
	def __init__(self, usuario=None, password=None, conectado=None, parent=None, is_root=False, is_left=False, is_right=False):
		self.usuario=usuario
		self.password=password
		self.conectado=conectado
		self.left=None
		self.right=None
		self.parent=parent
		self.is_root=is_root
		self.is_left=is_left
		self.is_right=is_right	