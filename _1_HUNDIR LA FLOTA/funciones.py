from colorama import Fore, Back, Style
import numpy as np
import random
import time
import variables as var

def suspense(periodo = 0.7):
    for _ in range(5):
        time.sleep(periodo)
        print('.', end=' ')
    time.sleep(1)

def contador_turnos():
    global turnos
    turnos += 1

def mostrar_tableros():
    global turnos
    if turnos == 0:                                                     # Si es el primer turno muestra mensajes especiales
        print('¡Este es el campo de batalla!', end= '\n\n')
        time.sleep(1)
        print(f'Tu tablero:\n{tablero_jugador}\nTablero de la máquina:\n{tablero_niebla} \n')
        time.sleep(3)
        print('Ahora, ¡A los cañones!', end= '\n\n')
    else:
        time.sleep(3)
        print(f'Tu tablero:\n{tablero_jugador}\nTablero de la máquina:\n{tablero_niebla} \n')


def colocar_barco_aleatorio(tablero, tam_barco):
    while True:
        orientacion = np.random.choice(['horizontal', 'vertical'])
        fila = np.random.randint(0, filas)
        columna = np.random.randint(0, columnas)

        if orientacion == 'horizontal' and columna + tam_barco <= columnas:
            coordenadas = [(fila, c) for c in range(columna, columna + tam_barco)]
        elif orientacion == 'vertical' and fila + tam_barco <= filas:
            coordenadas = [(f, columna) for f in range(fila, fila + tam_barco)]
        else:
            continue 

        ocupado = any(tablero[x][y] == c_barco for x, y in coordenadas if 0 <= x < filas and 0 <= y < columnas)
        ocupado_alrededor = any(tablero[x][y] == c_barco for x, y in get_celdas_alrededor(coordenadas) if 0 <= x < filas and 0 <= y < columnas)
        if not ocupado and not ocupado_alrededor:
            posicionar_barco(tablero, coordenadas)
            break

def get_celdas_alrededor(coordenadas):
    celdas_alrededor = set()
    for x, y in coordenadas:
        celdas_alrededor.update([(x-1, y), (x+1, y), (x, y-1), (x, y+1)])
    return celdas_alrededor

def posicionar_barco(tablero, coordenadas):
    for x, y in coordenadas: #for coordenada in coordenadas:
        tablero[x][y] = 'O'

def colocar_barco():
    for tam_barco, cantidad in barcos_jugador.items():
        for i in range(cantidad):
            colocar_barco_aleatorio(tablero_jugador, tam_barco)

def colocar_barco_maquina():
    for tam_barco, cantidad in barcos_maquina.items():
        for i in range(cantidad):
            colocar_barco_aleatorio(tablero_maquina, tam_barco)

def disparo_jugador():
    ej = True
    contador = 0
    global break_point
    while ej:
        time.sleep(3)
        if contador != 0:                           # El primer if comprueba si ya ha tirado en este turno o no, y muestra mensajes y tableros en función de eso.
            print('¡Te toca de nuevo! \n')
            mostrar_tableros()
        else:
            print('¡Es tu turno!')
        time.sleep(1.5)
        disparo_jugador_x = input('Introduce la coordenada X de tu disparo: [0,9]')     # Pedimos el input de la primera coordenada
        if disparo_jugador_x == 'exit':                                                 # Aquí hay una puerta trasera, para poder salir del juego escribimos "exit"
            break_point += 1
            break
        disparo_jugador_x = int(disparo_jugador_x)
        disparo_jugador_y = int(input('Introduce la coordenada Y de tu disparo: [0,9]'))    # Pedimos la segunda coordenada
        time.sleep(1)
        print(f"Disparo efectuado a las coordenadas ({disparo_jugador_x}, {disparo_jugador_y}).\n")
        suspense()
        if tablero_maquina[disparo_jugador_x, disparo_jugador_y] == c_barco:                # En este conjunto de if comprobamos qué hay en las coordnadas, actualizamos los tableros y damos la infor por pantalla.
            print('¡Impacto!¡Barco alcanzado!\n')
            tablero_niebla[disparo_jugador_x, disparo_jugador_y] = c_tocado
            tablero_maquina[disparo_jugador_x, disparo_jugador_y] = c_tocado
            if condicion_victoria() == True:                                                # Comprobamos si con este tiro ha ganado.
                break
            contador += 1
        elif tablero_maquina[disparo_jugador_x, disparo_jugador_y] == c_agua:
            print('Agua...\n')
            tablero_niebla[disparo_jugador_x, disparo_jugador_y] = c_agua_tiro
            ej = False
        elif tablero_maquina[disparo_jugador_x, disparo_jugador_y] == c_tocado:
            print('Ya habías disparado ahí.\n')
            ej = False
        elif tablero_maquina[disparo_jugador_x, disparo_jugador_y] == c_agua_tiro:
            print('Agua, y ya habías disparado ahí.\n')
            ej = False

def disparo_maquina():
    ej = True
    contador = 0
    while ej:
        time.sleep(3)
        if contador != 0:
            print('¡Le toca a la maquína de nuevo! \n')
        else:
            print('¡Es el turno de la máquina!')
        disparo_maquina_x = np.random.randint(0,10)
        disparo_maquina_y = np.random.randint(0,10)
        time.sleep(2)
        print(f"La máquina dispara a las coordenadas ({disparo_maquina_x}, {disparo_maquina_y}).\n")
        suspense(0.5)
        if tablero_jugador[disparo_maquina_x, disparo_maquina_y] == c_barco:
            print('¡Impacto!¡Barco alcanzado!\n')
            tablero_jugador[disparo_maquina_x, disparo_maquina_y] = c_tocado
            if condicion_victoria() == True:
                break
            contador += 1
        elif tablero_jugador[disparo_maquina_x, disparo_maquina_y] == c_agua:
            print('Agua...\n')
            tablero_jugador[disparo_maquina_x, disparo_maquina_y] = c_agua_tiro
            ej = False
        elif tablero_jugador[disparo_maquina_x, disparo_maquina_y] == c_tocado:
            print('Ya habías disparado ahí.\n')
            ej = False
        elif tablero_jugador[disparo_maquina_x, disparo_maquina_y] == c_agua_tiro:
            print('Agua, y ya habías disparado ahí.\n')
            ej = False


def condicion_victoria():
    global hay_ganadore
    ganador = False
    if (c_barco in tablero_jugador) == False:                           # Comprobamos si hay algún barco en pie y sino declaramos ganador.
        suspense()
        print(f'Lo siento {id_jugador}, gana la máquina.')
        hay_ganadore +=1
        ganador = True
    elif (c_barco in tablero_maquina) == False:
        suspense()
        print(f'¡Enhorabuena, {id_jugador}! ¡Has ganado! \n Has tardado {turnos} turnos.')
        hay_ganadore +=1
        ganador = True
    return ganador