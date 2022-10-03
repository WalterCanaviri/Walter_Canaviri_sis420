import random

# Mira si existe una "c" (camino) en los ejes cardinales
def mapeo_de_caminos(pared_aleatoria):
	s_caminos = 0
	if (laberinto[pared_aleatoria[0]-1][pared_aleatoria[1]] == 'c'):
		s_caminos += 1
	if (laberinto[pared_aleatoria[0]+1][pared_aleatoria[1]] == 'c'):
		s_caminos += 1
	if (laberinto[pared_aleatoria[0]][pared_aleatoria[1]-1] == 'c'):
		s_caminos +=1
	if (laberinto[pared_aleatoria[0]][pared_aleatoria[1]+1] == 'c'):
		s_caminos += 1
	return s_caminos

#INICIALIZACION DE VARIABLES
pared = 'w'
camino = 'c'
vacio = 'u'
alto = 7
ancho = 8
laberinto = []

# Indicar todas las celdas como vacio
for i in range(0, alto):
	columna = []
	for j in range(0, ancho):
		columna.append(vacio)
	laberinto.append(columna)

# Lo que hace es que crea un margen de un cuadro para que no se genere el inicio en los margenes
inicio_alto = random.randint(0, alto)
inicio_ancho = random.randint(0, ancho)
if (inicio_alto == 0):
	inicio_alto += 1
if (inicio_alto == alto-1):
	inicio_alto -= 1
if (inicio_ancho == 0):
	inicio_ancho += 1
if (inicio_ancho == ancho-1):
	inicio_ancho -= 1
laberinto[inicio_alto][inicio_ancho] = camino

# al encontrar el punto de inicio, se define los 4 puntos cardinales del punto de inicio
paredes = []
paredes.append([inicio_alto - 1, inicio_ancho])
paredes.append([inicio_alto, inicio_ancho - 1])
paredes.append([inicio_alto, inicio_ancho + 1])
paredes.append([inicio_alto + 1, inicio_ancho])

# Se usa los puntos cardinales obtenidos y se coloca "w" (pared) 
laberinto[inicio_alto-1][inicio_ancho] = 'w'
laberinto[inicio_alto][inicio_ancho - 1] = 'w'
laberinto[inicio_alto][inicio_ancho + 1] = 'w'
laberinto[inicio_alto + 1][inicio_ancho] = 'w'

while (paredes):
	# Se elige una de los puntos cardinales al azar  
	pared_aleatoria = paredes[int(random.random()*len(paredes))-1]
	# Compruebe si es una pared izquierda
	if (pared_aleatoria[1] != 0 and laberinto[pared_aleatoria[0]][pared_aleatoria[1]-1] == 'u' and laberinto[pared_aleatoria[0]][pared_aleatoria[1]+1] == 'c'):
		# Encuentre el número de celdas circundantes
		s_caminos = mapeo_de_caminos(pared_aleatoria)
		if (s_caminos < 2):
			# Se reemplaza la pared con una "c" (camino)
			laberinto[pared_aleatoria[0]][pared_aleatoria[1]] = 'c'
			# Se definen las paredes el 3 puntos cardinales
			# Celda superior
			if (pared_aleatoria[0] != 0):
				if (laberinto[pared_aleatoria[0]-1][pared_aleatoria[1]] != 'c'):
					laberinto[pared_aleatoria[0]-1][pared_aleatoria[1]] = 'w'
				if ([pared_aleatoria[0]-1, pared_aleatoria[1]] not in paredes):
					paredes.append([pared_aleatoria[0]-1, pared_aleatoria[1]])
			# Celda inferior
			if (pared_aleatoria[0] != alto-1):
				if (laberinto[pared_aleatoria[0]+1][pared_aleatoria[1]] != 'c'):
					laberinto[pared_aleatoria[0]+1][pared_aleatoria[1]] = 'w'
				if ([pared_aleatoria[0]+1, pared_aleatoria[1]] not in paredes):
					paredes.append([pared_aleatoria[0]+1, pared_aleatoria[1]])
			# Celda más a la izquierda
			if (pared_aleatoria[1] != 0):	
				if (laberinto[pared_aleatoria[0]][pared_aleatoria[1]-1] != 'c'):
					laberinto[pared_aleatoria[0]][pared_aleatoria[1]-1] = 'w'
				if ([pared_aleatoria[0], pared_aleatoria[1]-1] not in paredes):
					paredes.append([pared_aleatoria[0], pared_aleatoria[1]-1])
		# Eliminar la pared de la lista para que ya no se use en la siguiente iteracion
		for pared in paredes:
			if (pared[0] == pared_aleatoria[0] and pared[1] == pared_aleatoria[1]):
				paredes.remove(pared)
		continue

	# Comprobar si es una pared superior
	if (pared_aleatoria[0] != 0 and laberinto[pared_aleatoria[0]-1][pared_aleatoria[1]] == 'u' and laberinto[pared_aleatoria[0]+1][pared_aleatoria[1]] == 'c'):
		s_caminos = mapeo_de_caminos(pared_aleatoria)
		if (s_caminos < 2):
			laberinto[pared_aleatoria[0]][pared_aleatoria[1]] = 'c'
			if (pared_aleatoria[0] != 0):
				if (laberinto[pared_aleatoria[0]-1][pared_aleatoria[1]] != 'c'):
					laberinto[pared_aleatoria[0]-1][pared_aleatoria[1]] = 'w'
				if ([pared_aleatoria[0]-1, pared_aleatoria[1]] not in paredes):
					paredes.append([pared_aleatoria[0]-1, pared_aleatoria[1]])
			if (pared_aleatoria[1] != 0):
				if (laberinto[pared_aleatoria[0]][pared_aleatoria[1]-1] != 'c'):
					laberinto[pared_aleatoria[0]][pared_aleatoria[1]-1] = 'w'
				if ([pared_aleatoria[0], pared_aleatoria[1]-1] not in paredes):
					paredes.append([pared_aleatoria[0], pared_aleatoria[1]-1])
			if (pared_aleatoria[1] != ancho-1):
				if (laberinto[pared_aleatoria[0]][pared_aleatoria[1]+1] != 'c'):
					laberinto[pared_aleatoria[0]][pared_aleatoria[1]+1] = 'w'
				if ([pared_aleatoria[0], pared_aleatoria[1]+1] not in paredes):
					paredes.append([pared_aleatoria[0], pared_aleatoria[1]+1])
		for pared in paredes:
			if (pared[0] == pared_aleatoria[0] and pared[1] == pared_aleatoria[1]):
				paredes.remove(pared)
		continue

	# Revisa la pared inferior
	if (pared_aleatoria[0] != alto-1 and laberinto[pared_aleatoria[0]+1][pared_aleatoria[1]] == 'u' and laberinto[pared_aleatoria[0]-1][pared_aleatoria[1]] == 'c'):
		s_caminos = mapeo_de_caminos(pared_aleatoria)
		if (s_caminos < 2):
			laberinto[pared_aleatoria[0]][pared_aleatoria[1]] = 'c'
			if (pared_aleatoria[0] != alto-1):
				if (laberinto[pared_aleatoria[0]+1][pared_aleatoria[1]] != 'c'):
					laberinto[pared_aleatoria[0]+1][pared_aleatoria[1]] = 'w'
				if ([pared_aleatoria[0]+1, pared_aleatoria[1]] not in paredes):
					paredes.append([pared_aleatoria[0]+1, pared_aleatoria[1]])
			if (pared_aleatoria[1] != 0):
				if (laberinto[pared_aleatoria[0]][pared_aleatoria[1]-1] != 'c'):
					laberinto[pared_aleatoria[0]][pared_aleatoria[1]-1] = 'w'
				if ([pared_aleatoria[0], pared_aleatoria[1]-1] not in paredes):
					paredes.append([pared_aleatoria[0], pared_aleatoria[1]-1])
			if (pared_aleatoria[1] != ancho-1):
				if (laberinto[pared_aleatoria[0]][pared_aleatoria[1]+1] != 'c'):
					laberinto[pared_aleatoria[0]][pared_aleatoria[1]+1] = 'w'
				if ([pared_aleatoria[0], pared_aleatoria[1]+1] not in paredes):
					paredes.append([pared_aleatoria[0], pared_aleatoria[1]+1])
		for pared in paredes:
			if (pared[0] == pared_aleatoria[0] and pared[1] == pared_aleatoria[1]):
				paredes.remove(pared)
		continue

	# Revisa la pared derecha
	if (pared_aleatoria[1] != ancho-1 and laberinto[pared_aleatoria[0]][pared_aleatoria[1]+1] == 'u' and laberinto[pared_aleatoria[0]][pared_aleatoria[1]-1] == 'c'):
		s_caminos = mapeo_de_caminos(pared_aleatoria)
		if (s_caminos < 2):
			laberinto[pared_aleatoria[0]][pared_aleatoria[1]] = 'c'
			if (pared_aleatoria[1] != ancho-1):
				if (laberinto[pared_aleatoria[0]][pared_aleatoria[1]+1] != 'c'):
					laberinto[pared_aleatoria[0]][pared_aleatoria[1]+1] = 'w'
				if ([pared_aleatoria[0], pared_aleatoria[1]+1] not in paredes):
					paredes.append([pared_aleatoria[0], pared_aleatoria[1]+1])
			if (pared_aleatoria[0] != alto-1):
				if (laberinto[pared_aleatoria[0]+1][pared_aleatoria[1]] != 'c'):
					laberinto[pared_aleatoria[0]+1][pared_aleatoria[1]] = 'w'
				if ([pared_aleatoria[0]+1, pared_aleatoria[1]] not in paredes):
					paredes.append([pared_aleatoria[0]+1, pared_aleatoria[1]])
			if (pared_aleatoria[0] != 0):	
				if (laberinto[pared_aleatoria[0]-1][pared_aleatoria[1]] != 'c'):
					laberinto[pared_aleatoria[0]-1][pared_aleatoria[1]] = 'w'
				if ([pared_aleatoria[0]-1, pared_aleatoria[1]] not in paredes):
					paredes.append([pared_aleatoria[0]-1, pared_aleatoria[1]])
		for pared in paredes:
			if (pared[0] == pared_aleatoria[0] and pared[1] == pared_aleatoria[1]):
				paredes.remove(pared)
		continue
	for pared in paredes:
		if (pared[0] == pared_aleatoria[0] and pared[1] == pared_aleatoria[1]):
			paredes.remove(pared)


# Se reemplaza los puestos vacios con una pares
for i in range(0, alto):
	for j in range(0, ancho):
		if (laberinto[i][j] == 'u'):
			laberinto[i][j] = 'w'

# Establecer entrada y salida
for i in range(0, ancho):
	if (laberinto[1][i] == 'c'):
		laberinto[0][i] = 'c'
		break

for i in range(ancho-1, 0, -1):
	if (laberinto[alto-2][i] == 'c'):
		laberinto[alto-1][i] = 'c'
		break

#Imprimir el laberinto
for lab in laberinto:
    print(lab)