c_barco = 'O'
c_tocado = 'X'
c_agua = ' '
c_agua_tiro = '/'
c_niebla = '~'
turnos = 0
hay_ganadore = 0
break_point = 0
id_jugador = 'Sara'
filas = 10
columnas = 10
coordenadas = []
barcos_jugador = {1: 4, 2: 3, 3: 2, 4: 1}
barcos_maquina = {1: 4, 2: 3, 3: 2, 4: 1}

tablero_niebla = np.full((filas, columnas), c_niebla)
tablero_maquina = np.full((filas, columnas), c_agua)
tablero_jugador = np.full((filas, columnas), c_agua)
