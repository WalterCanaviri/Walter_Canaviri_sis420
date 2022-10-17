# Implementar una funcion que permita expandir nodos hijos para n caracteres, los cuales deben ser establecidos al momento de iniciar el programa.
# Se define una funcion para llenar las listas nesesarias para ejecutar el programa

# Describir cual es el nivel maximo de numero de digitos que el rompecabezas se puede resolver en su maquina, explicando a que se deberia este limite y como se lo podria superara.
# Mi computadora es capaz de realizar hasta 7 digitos con un tiempo de 2 minutos con 14 segundos
# Y se pudiera aumentar el numero de digitos y reducir el tiempo, si usaramos un servidor en la nuve como COLAB

# hacer correr el mismo programa, pero utilizando una lista LIFO para la lista frontera.
# En la linea 59 esta como una lista fifo, y para pasar una lista lifo se tiene que comentar y descomentar la lista 60

class Nodo:
    def __init__(self, datos, hijo=None):
        self.datos = datos
        self.hijos = []
        self.padre = None
        self.costo = None
        self.set_hijo(hijo)
    def set_hijo(self, hijo):
        if (hijo is not None):
            self.hijos.append(hijo)
            if self.hijos is not None:
                #self.hijos[len(self.hijos)-1].padre = self
                for h in self.hijos:
                    h.padre = self
    def get_hijos(self):
        return self.hijos
    def set_padre(self, padre):
        self.padre = padre
    def get_padre(self):
        return self.padre
    def set_datos(self, datos):
        self.datos = datos
    def get_datos(self):
        return self.datos
    def set_costo(self, costo):
        self.costo = costo
    def get_costo(self):
        return self.costo
    def equal(self, nodo):
        if self.get_datos() == nodo.get_datos():
            return True
        else:
            return False
    def en_lista(self, lista_nodos):
        enlistado = False
        for n in lista_nodos:
            if self.equal(n):
                enlistado = True
        return enlistado
    def __str__(self):
        return str(self.get_datos())
def bpa(estado_inicio, estado_solucion):
    resuelto = False
    nodos_visitados = []
    nodos_frontera = []
    nodo_inicio = Nodo(estado_inicio)
    nodos_frontera.append(nodo_inicio)
    while resuelto == False and len(nodos_frontera) != 0:
        nodo_actual = nodos_frontera.pop(0) #Cola
        #nodo_actual = nodos_frontera.pop() #Pila
        nodos_visitados.append(nodo_actual)
        if nodo_actual.get_datos() == estado_solucion:
            resuelto = True
            return nodo_actual
        else:
            for i in range(len(estado_inicio)-1):
                for j in range(len(estado_inicio)-1): 
                    hijo_datos = nodo_actual.get_datos().copy()    
                    temp = hijo_datos[j]
                    hijo_datos[j] = hijo_datos[j+1]
                    hijo_datos[j+1] = temp
                    hijo = Nodo(hijo_datos)
                    if not hijo.en_lista(nodos_visitados) and not hijo.en_lista(nodos_frontera):
                        nodo_actual.set_hijo(hijo)
                        nodos_frontera.append(hijo)
def llenar_datos():
    tamaño = int(input("Digite el tamao de la lista a crear: "))
    print("Creando la lista ESTADO_INICIAL ...")
    estado_inicial = []
    contador = 0
    while (contador < tamaño):
        Dato = int(input("Digite un numero: "))
        estado_inicial.append(Dato)
        contador = contador + 1
    print("Creando la lista SOLUCION ...")
    solucion = []
    contador = 0
    while (contador < tamaño):
        Dato = int(input("Digite un numero: "))
        solucion.append(Dato)
        contador = contador + 1
    return estado_inicial,solucion
import time
if __name__ == "__main__":
    #estado_inicial = [4, 3, 2, 1]
    #solucion = [1, 2, 3, 4]
    estado_inicial,solucion = llenar_datos()

    start = time.time()
    nodo_solucion = bpa(estado_inicial, solucion)
    end =time.time()
    print('Tiempo de ejecucion : ',end-start, 'seg.','\n')
    
    resultado = []
    nodo_actual = nodo_solucion
    while nodo_actual.get_padre() is not None:
        resultado.append(nodo_actual.get_datos())
        nodo_actual = nodo_actual.get_padre()
    resultado.append(estado_inicial)
    resultado.reverse()
    
    print("Movimientos :")
    #print(resultado)
    for i in range(len(resultado)):
      print(resultado[i])