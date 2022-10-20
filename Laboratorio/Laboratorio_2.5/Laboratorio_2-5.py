# El programa creado, se tarda 0.15 segundos en resolver el rompecabgezas
# Lo que realiza es comparar la lista de inicio y final, desde el primer dato y si no son iguales, busca en toda la lista el dato y lo mueve hasta la posicion que deve estar (segun la lista "fin")
# Esta aclaro que no se usa un metodo generico, sino uno creado por mi
# Se puede decir que se usa un tipo de metodo de busqueda informada, ya que se sabe a que lista se tiene que llegar y busca en la lista uno por uno el dato hasta que sean iguales las lista "inicio" y "fin"

import time
def intercambio(indice_aux, list_actual):
    #Intercambia los datos segun el indice que nos da
    temp = list_actual[indice_aux]
    list_actual[indice_aux] = list_actual[indice_aux+1]
    list_actual[indice_aux+1] = temp
    return list_actual

def procedimiento(inicio,fin):
    print(inicio)
    estado=1
    indice = 0
    pasos = 0
    list_actual = inicio
    while(estado):
        if(list_actual[indice] == fin[indice]):
            #Si los datos son iguales en el inicio y el final, entonces se procedera a aumentar el indice +1 para seguie con el otro numero a igualar
            if(indice < len(fin)-1):
                indice = indice + 1
            else:
                estado = 0
        else:
            # Si no son iguales, significa que hay que seguir moviendo las posiciones hasta llegar al orden (fin)
            # Se crea indice_aux, para guardar el indice de donde se intercambiara las fichas
            indice_aux = -1
            for dato in list_actual:
                indice_aux = indice_aux + 1
                if(dato == fin[indice]):
                    list_actual = intercambio(indice_aux-1, list_actual)
                    pasos = pasos + 1
                    print(list_actual)
    print("Cantidad de movimientos realizados son: ",pasos)

inicio = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
fin = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

start = time.time()
procedimiento(inicio,fin)
end =time.time()
print('Tiempo de ejecucion : ',end-start, 'seg.','\n')
