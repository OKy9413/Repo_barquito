def iniciar_juego():
    print('hola! estas son la reglas...')

def tablero_jugador(dimension):
    return np.full((dimension,dimension),"~")

def tablero_pc(dimension):
    return np.full((dimension,dimension),"~")

def tablero_niebla(dimension):
    return np.full((dimension,dimension),"~")



def colocar_barco_aleatorio(tablero, longitud):
    filas, columnas = tablero.shape
    orientaciones = ["N", "S", "E", "O"]
    while True:
        x = random.randint(0, filas - 1) #generar aleatoriamente las coordenadas iniciales x e y 
        y = random.randint(0, columnas - 1)
        orientacion = random.choice(orientaciones) #generar aleatoriamente una orientación de la lista
        coordenadas = [] # lista vacía para almacenar las posiciones
        comprobar_barco()

def comprobar_barco():
        for _ in range(longitud): #buble para la longitud del barco
            if x < 0 or x >= filas or y < 0 or y >= columnas or tablero[x][y] == 'O': #verificamos dentro del tablero y que no hay barco
                break
            coordenadas.append((x, y)) #si es valido se añade a coordenadas
            if orientacion == 'N': #aqui dependiendo de si la orientacion es valida, añado o no a la coordenada
                x -= 1
            elif orientacion == 'S':
                x += 1
            elif orientacion == 'E':
                y += 1
            else:
                y -= 1
        if len(coordenadas) == longitud: #verifico si coordenadas es la longitud que elegimos al inicio
            posicionar_barco(tablero, coordenadas)
            break

def generar_barco()

def disparar():



