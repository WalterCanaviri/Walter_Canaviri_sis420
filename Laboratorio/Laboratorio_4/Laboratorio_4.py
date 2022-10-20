import time
import random
class Nodo:
    def __init__(self, datos, hijo=None):
        self.datos = datos
        self.hijos = []
        self.padre = None
        self.costo = []
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
def verificar(lista_original, list_a_comparar):
    estado = False
    for dato in list_a_comparar:
        #print("dato a comparar = ",lista_original," con visitados ",dato)
        #print("--------------------------------------")
        if(lista_original == dato):
            estado = True
    return estado

def bpa(estado_inicio, solucion):
    resuelto = False
    nodos_visitados = []
    nodos_frontera = []
    nodo_inicio = Nodo(estado_inicio)
    #costos_generados = llenar_costos(len(estado_inicial))
    costos_generados =[1,8,2,8]
    nodo_inicio.set_costo(costos_generados)
    #print("Lista de costos = ", costos_generados)
    nodos_frontera.append(nodo_inicio.get_costo())
    #estado_solucion = ordenar(costos_generados)
    estado_solucion = [1,2,8,8]
    #print("Lista de costos ordenado = ", estado_solucion)
    while resuelto == False and len(nodos_frontera) != 0:
        #print("nodo frontera = ",nodos_frontera)
        nodo_actual = nodos_frontera.pop(0) #Cola
        #nodo_actual = nodos_frontera.pop() #Pila
        nodos_visitados.append(nodo_actual)
        #print("nodo actual, tipo = ",type(nodo_actual))
        #print("Nodo Actual = ",nodo_actual," Estado solucion = ",estado_solucion)
        if nodo_actual == estado_solucion:
            resuelto = True
            #print("Nodo Inicio = ",nodo_inicio," Nodo Actual = ",nodo_actual)
            return nodo_inicio, nodo_actual
        else:
            for i in range(len(estado_inicio)-1):
                for j in range(len(estado_inicio)-1): 
                    hijo_datos = nodo_inicio.get_datos().copy() 
                    costo_datos = nodo_actual.copy()
                    temp = hijo_datos[j]
                    temp_2 = costo_datos[j]
                    hijo_datos[j] = hijo_datos[j+1]
                    costo_datos[j] = costo_datos[j+1]
                    hijo_datos[j+1] = temp
                    costo_datos[j+1] = temp_2
                    hijo = Nodo(hijo_datos)
                    hijo.set_costo(costo_datos)
                    #print("Costos = ",hijo.get_costo(),"Hijo creado = ",hijo.get_datos())
                    #print("tipo de nodos visitados = ",type(nodos_visitados))
                    #print("Tipo de nodos frontera = ", type(nodos_frontera))
                    #hijo.verificar(nodos_visitados)
                    #print("--------------------------------------")
                    #hijo.verificar(nodos_frontera)
                    #print("--------------------------------------")
                    if not verificar(hijo.get_costo(),nodos_visitados) and not verificar(hijo.get_costo(),nodos_frontera):
                        #print("ENTRO")
                        nodo_inicio.set_hijo(hijo)
                        nodos_frontera.append(costo_datos)
                        #print("Nuevo nodo frontera = ", nodos_frontera)
        #print("Tamaño del nodo frontera = ",len(nodos_frontera))
def ordenar(estado_inicial):
    #INICIO DE CAMBIO DE LISTA
    list_inicio = []
    for data in estado_inicial:
        #print("datos = ",data)
        list_inicio.append(data)
    #FIN DE CAMVBIO D LISTA
    for i in range(0,len(list_inicio)):
        for j in range(i+1,len(list_inicio)):
            # modificar < para menor a mayor
            if(list_inicio[j] < list_inicio[i]):
                aux = list_inicio[i]
                list_inicio[i]=list_inicio[j]
                list_inicio[j]=aux
    return list_inicio

def llenar_costos(n):
    list_aux = []
    for dato in range(0,n):
        list_aux.append(random.randint(1,9))
    return list_aux


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

if __name__ == "__main__":
    estado_inicial = [4, 3, 2, 1]
    solucion = [1, 2, 3, 4]
    #estado_inicial,solucion = llenar_datos()
    
    #list_aux = ordenar(estado_inicial)
    #print(list_aux)

    start = time.time()
    nodo_solucion, costo_solucion = bpa(estado_inicial, solucion)
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