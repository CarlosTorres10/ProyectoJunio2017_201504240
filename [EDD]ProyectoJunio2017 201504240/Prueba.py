#from ArbolErick import arbolBinario
#from ABB_Enteros import ArbolABB
#from Arbol_ABB import ArbolABB
#from Nodo_Arbol_Espejo import Nodo
#from Arbol_Binario_Busqueda_Espejo import arbolBinario

from ArbolPrueba import arbolBinario
from NodoArbolPrueba import Nodo 
from ListaDoblePrueba import ListaDoblePruebas



#arboltexto=arbolBinario()

#arboltexto.insertar("Juan","123","123")
#arboltexto.insertar("Pedro","123","123")
#arboltexto.insertar("Maria","123","123")
#arboltexto.insertar("Roberto","123","123")
#arboltexto.insertar("Teodoro","123","123")
#arboltexto.insertar("Manuel","123","123")
#arboltexto.insertar("Diego","123","123")
#arboltexto.insertar("Alejandro","123","123")

#arboltexto.inorden()
#arboltexto.Buscar(arboltexto.raiz,"Teodoro")
#arboltexto.graficar()

PruebaArbol=arbolBinario()
ListaDoble=ListaDoblePruebas()

ListaDoble.agregar_final("Mord86","Stin94","51","26","25","0","10")
ListaDoble.agregar_final("Mord86","Asro25","57","29","28","1","19")
ListaDoble.agregar_final("Mord86","Idin94","46","22","24","0","12")
ListaDoble.agregar_final("Mord86","Jado86","53","27","26","1","14")
ListaDoble.agregar_final("Asro25","Erll88654","49","20","29","1","999999999")
ListaDoble.agregar_final("Stin94","Mord86","46","21","25","1","13")
ListaDoble.agregar_final("Stin94","Asro25","45","23","22","0","16")
ListaDoble.agregar_final("Stin94","Imre78","56","29","27","0","9")
ListaDoble.agregar_final("Imre78","Erll88","49","20","29","1","9")
ListaDoble.agregar_final("Pepe","Erll88","49","20","29","1","999999999")
ListaDoble.agregar_final("Pepito","Erll8887987","49","20","29","1","999999999")



#ListaDoble.ExisteUsuario("Mord86")
#ListaDoble.graficar()


NoditoPrueba=Nodo("Mord86",str(123),str(0))
NoditoPrueba.setListaDoble(ListaDoble)
PruebaArbol.agregar(NoditoPrueba)
NoditoPrueba=Nodo("Diego",str(123),str(0))
NoditoPrueba.setListaDoble(ListaDoble)
PruebaArbol.agregar(NoditoPrueba)
NoditoPrueba=Nodo("Stin94",str(123),str(0))
NoditoPrueba.setListaDoble(ListaDoble)
PruebaArbol.agregar(NoditoPrueba)
NoditoPrueba=Nodo("Imre78",str(123),str(0))
NoditoPrueba.setListaDoble(ListaDoble)
PruebaArbol.agregar(NoditoPrueba)
NoditoPrueba=Nodo("Pepito",str(123),str(0))
NoditoPrueba.setListaDoble(ListaDoble)
PruebaArbol.agregar(NoditoPrueba)
NoditoPrueba=Nodo("Roberto",str(123),str(0))
NoditoPrueba.setListaDoble(ListaDoble)
PruebaArbol.agregar(NoditoPrueba)
NoditoPrueba=Nodo("Pepe",str(123),str(0))
NoditoPrueba.setListaDoble(ListaDoble)
PruebaArbol.agregar(NoditoPrueba)
NoditoPrueba=Nodo("Asro25",str(123),str(0))
NoditoPrueba.setListaDoble(ListaDoble)
PruebaArbol.agregar(NoditoPrueba)
NoditoPrueba=Nodo("Pepita",str(123),str(0))
NoditoPrueba.setListaDoble(ListaDoble)
PruebaArbol.agregar(NoditoPrueba)




PruebaArbol.cerrarArchivo()


#PruebaArbol.buscar("Mord86")

#PruebaArbol.graficarUsuarios()


#from Lista_Doblemente_Enlazada import ListaDoble 
#import os
#os.system('cls')
#Lista=ListaDoble()
#Lista.agregar_final("Mord86","Stin94","51","26","25","0","10")
#Lista.agregar_final("Mord86","Asro25","57","29","28","1","19")
#Lista.agregar_final("Mord86","Idin94","46","22","24","0","12")
#Lista.agregar_final("Mord86","Jado86","53","27","26","1","14")
#Lista.agregar_final("Stin94","Mord86","46","21","25","1","13")
#Lista.agregar_final("Stin94","Asro25","45","23","22","0","16")
#Lista.agregar_final("Stin94","Imre78","56","29","27","0","9")
#Lista.agregar_final("Imre78","Erll88","49","20","29","1","9")
#Lista.recorrer_inicio_fin()
#Lista.ExisteUsuario("Mord86")
#Lista.ExisteUsuario("Stin94")
#Lista.graficar()




#AB=aBinarios()

#NodoArbol=Nodo(9)
#AB.agregar(NodoArbol)
#NodoArbol=Nodo(50)
#AB.agregar(NodoArbol)
#NodoArbol=Nodo(2)
#AB.agregar(NodoArbol)
#NodoArbol=Nodo(1)
#AB.agregar(NodoArbol)
#NodoArbol=Nodo(3)
#AB.agregar(NodoArbol)
#NodoArbol=Nodo(5000)
#AB.agregar(NodoArbol)
#NodoArbol=Nodo(70)
#AB.agregar(NodoArbol)
#NodoArbol=Nodo(4)
#AB.agregar(NodoArbol)
#NodoArbol=Nodo(7)
#AB.agregar(NodoArbol)
#NodoArbol=Nodo(15)
#AB.agregar(NodoArbol)

#AB.Recorrido_EnOrden(AB.getRaiz())

#Nodito=Nodo("e",str(123),str(0))
#z.agregar(Nodito)
#Nodito=Nodo("a",str(123),str(0))
#z.agregar(Nodito)
#Nodito=Nodo("b",str(123),str(0))
#z.agregar(Nodito)
#Nodito=Nodo("c",str(123),str(0))
#z.agregar(Nodito)
#Nodito=Nodo("d",str(123),str(0))
#z.agregar(Nodito)
#Nodito=Nodo("f",str(123),str(0))
#z.agregar(Nodito)
#Nodito=Nodo("g",str(123),str(0))
#z.agregar(Nodito)
#Nodito=Nodo("h",str(123),str(0))
#z.agregar(Nodito)
#Nodito=Nodo("i",str(123),str(0))
#z.agregar(Nodito)
#Nodito=Nodo("aa",str(123),str(0))
#z.agregar(Nodito)
#z.graficarUsuarios()

#Arbol=ArbolABB()

#Arbol.Insertar("d",str(123),str(0))
#Arbol.Insertar("c",str(123),str(0))
#Arbol.Insertar("b",str(123),str(0))
#Arbol.Insertar("luis",str(123),str(0))
#Arbol.Insertar("pepe",str(123),str(0))
#Arbol.Insertar("pedrito",str(123),str(0))
#Arbol.Insertar("lesly",str(123),str(0))
#Arbol.Insertar("karla",str(123),str(0))
#Arbol.Insertar("calar",str(123),str(0))
#Arbol.Insertar("celar",str(123),str(0))
#Arbol.Insertar("cilar",str(123),str(0))
#Arbol.Insertar("colar",str(123),str(0))
#Arbol.Insertar("cular",str(123),str(0))
#Arbol.Insertar("caalar",str(123),str(0))
#Arbol.Insertar("ceelar",str(123),str(0))
#Arbol.Insertar(8)
#Arbol.Insertar(10)
#Arbol.Insertar(3)
#Arbol.Insertar(14)
#Arbol.Insertar(13)
#Arbol.Insertar(1)
#Arbol.Insertar(6)
#Arbol.Insertar(4)
#Arbol.Insertar(7)
#Arbol.Insertar(5)
#Arbol.Insertar(9)
#Arbol.Insertar(3)


#Arbol.Recorrido_EnOrden(Arbol.root)
#Arbol.CodigoInternoABB(Arbol.root)
#Arbol.GraficarArbolABB(Arbol.root)
#Arbol.hola()

