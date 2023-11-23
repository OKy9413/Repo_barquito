from colorama import Fore, Back, Style
import numpy as np
import random
import time
# from variables import *
import variables as var

def bienvenida():
    global id_jugador
    print(f"{Fore.CYAN}Bienvenid@ al juego de 'Hundir la Flota'{Style.RESET_ALL}")
    var.id_jugador = input(f"¿Cómo te gustaría que te llamara? ")
    time.sleep(1)
    print(f"{Fore.CYAN}Encantado de conocerte: \U0001F99A{Style.BRIGHT}{Fore.WHITE}{Back.BLACK}\033[4m{var.id_jugador}\033[0m{Style.RESET_ALL}, {Fore.CYAN}soy tu oponente: \U0001F916{Fore.WHITE}{Back.BLACK}\033[4mShipBrainy\033[0m{Style.RESET_ALL}{Fore.CYAN}, un experimentado estratega, asi que prepárate para perder...{Style.RESET_ALL}" )
    time.sleep(3)
    print(f"{Fore.CYAN}Estas son las instrucciones del juego:{Style.RESET_ALL}")
    time.sleep(2)
    print(f"""
    
      🏴‍☠️   {Fore.RED}{Fore.YELLOW}- Jugarás contra la máquina\n
      🏴‍☠️ - En primer lugar, deberás colocar tus 10 barcos, con la siguiente distribución:\n
                🚢 - {Fore.GREEN}{Back.MAGENTA}4 barcos de 1 posición de eslora{Style.RESET_ALL}
                ⛵ - {Fore.GREEN}{Back.MAGENTA}3 barcos de 2 posiciones de eslora{Style.RESET_ALL}
                ⛵ - {Fore.GREEN}{Back.MAGENTA}2 barcos de 3 posiciones de eslora{Style.RESET_ALL}
                🚤 - {Fore.GREEN}{Back.MAGENTA}1 barco de 4 posiciones de eslora{Style.RESET_ALL}\n
      🏴‍☠️  {Fore.RED}{Fore.YELLOW}- Cuando comience el juego, tendrás un tablero para observar los disparos del contrincante, así como uno para comprobar tu jugada.\n
      🏴‍☠️ - El juego se desarrolla por turnos, donde si algún jugador acierta durante el mismo, volverá a repetir turno y en caso contrario, se producirá un cambio de turno al oponente.\n
      🏴‍☠️ - Para {Style.BRIGHT}\033[4mdisparar\033[0m{Style.RESET_ALL}{Fore.RED}{Fore.YELLOW} tendrás que introducir \033[4muna coordenada X(fila) y otra Y(columna)\033[0m{Fore.RED}{Fore.YELLOW}, con la cual marcarás dónde quieres disparar en el tablero del oponente,
           y podrás ver los tableros nuevamente. En caso de introducir {Style.BRIGHT}\033[4mcoordenadas fuera del tablero\033[0m {Fore.RED}{Fore.YELLOW}, te saltará un error para que introduzcas coordenadas válidas.{Style.RESET_ALL}\n
      🏴‍☠️ {Fore.RED}{Fore.YELLOW}- El primer jugador que hunda todos los barcos del oponente, habrá ganado, finalizando el juego.{Style.RESET_ALL}""")
    time.sleep(3)
    # print(f"\U0001F99A{Style.BRIGHT}{Fore.CYAN}{id_jugador}{Style.RESET_ALL}, {Fore.CYAN}¿Tienes las instrucciones claras(S/N)?{Style.RESET_ALL}")

    while True:
          respuesta = input(f"\U0001F99A{Style.BRIGHT}{Fore.WHITE}{Back.BLACK}\033[4m{var.id_jugador}\033[0m{Style.RESET_ALL},{Fore.CYAN}¿Tienes las instrucciones claras(S/N)? ")
          if respuesta.upper() == "S": 
               print(f"{Fore.CYAN}Comienza el ¡¡DESAFÍO!!{Style.RESET_ALL}")
               break  
          elif respuesta.upper() =="N":
               print(f"{Fore.CYAN}Eres un poco {Style.BRIGHT}TORPE{Style.RESET_ALL}{Fore.CYAN}...😈😈😈, asi que, léete de nuevo las instrucciones que te he dado 😂")
               print(f"{Fore.CYAN}Si estás preparad@ pulsa: S, y si quieres comenzar de nuevo: N.")
               continue
          else:
               print(f"{Fore.CYAN}Error: ingresa la letra correcta: S o N{Style.RESET_ALL}")
               continue
    
    # print(f"{Fore.CYAN}¿Algo que decirme antes de comenzar?") 
    input(f"{Fore.CYAN}¿Algo que decirme antes de comenzar? ")
    print(f"{Fore.CYAN}Si,si...lo que tu digas😂..¡¡PREPÁRATE!!😠😠...{Style.RESET_ALL}")
    time.sleep(2)
    print(f"{Fore.CYAN}Sabes que perderás😂😂😂😂😂, comienza el ¡¡DESAFÍO!!{Style.RESET_ALL} ")
               

def suspense(periodo = 0.3):
    for _ in range(5):
        time.sleep(periodo)
        print('.', end=' ')
    time.sleep(1)

def contador_turnos():
    global turnos
    var.turnos += 1

def mostrar_tableros():
    global turnos
    if var.turnos == 0:                                                     
        print('¡Este es el campo de batalla!', end= '\n\n')
        time.sleep(1)
        print(f'Tu tablero:\n{var.tablero_jugador}\nTablero de ShipBrainy:\n{var.tablero_niebla} \n')
        time.sleep(3)
        print('Ahora, ¡A los cañones!', end= '\n\n')
    else:
        time.sleep(3)
        print(f'Tu tablero:\n{var.tablero_jugador}\nTablero de ShipBrainy:\n{var.tablero_niebla} \n')


def colocar_barco_aleatorio(tablero, tam_barco):
    while True:
        orientacion = np.random.choice(['horizontal', 'vertical']) 
        fila = np.random.randint(0, var.filas)
        columna = np.random.randint(0, var.columnas)

        if orientacion == 'horizontal' and columna + tam_barco <= var.columnas:
            coordenadas = [(fila, c) for c in range(columna, columna + tam_barco)]
        elif orientacion == 'vertical' and fila + tam_barco <= var.filas:
            coordenadas = [(f, columna) for f in range(fila, fila + tam_barco)]
        else:
            continue 

        ocupado = any(tablero[x][y] == var.c_barco for x, y in coordenadas if 0 <= x < var.filas and 0 <= y < var.columnas)
        ocupado_alrededor = any(tablero[x][y] == var.c_barco for x, y in get_celdas_alrededor(coordenadas) if 0 <= x < var.filas and 0 <= y < var.columnas)
        if not ocupado and not ocupado_alrededor:
            posicionar_barco(tablero, coordenadas)
            break

def get_celdas_alrededor(coordenadas):
    celdas_alrededor = set()
    for x, y in coordenadas:
        celdas_alrededor.update([(x-1, y), (x+1, y), (x, y-1), (x, y+1)])
    return celdas_alrededor

def posicionar_barco(tablero, coordenadas):
    for x, y in coordenadas:
        tablero[x][y] = var.c_barco

def colocar_barcos():
    global tablero_jugador
    for tam_barco, cantidad in var.barcos_jugador.items():
        for i in range(cantidad):
            colocar_barco_aleatorio(var.tablero_jugador, tam_barco)

def colocar_barcos_maquina():
    global tablero_maquina
    for tam_barco, cantidad in var.barcos_maquina.items():
        for i in range(cantidad):
            colocar_barco_aleatorio(var.tablero_maquina, tam_barco)

def test(coor1 = 1, coor2 = 2):
    global tablero_maquina
    var.tablero_maquina[coor1,coor2] = var.c_barco

def normal_test():
    prueba = input('¿Quieres jugar el juego normal o una prueba? ')
    if prueba.lower() == 'prueba':
        print('Vamos con el testeo ')
        test()
    else:
        colocar_barcos_maquina()

def obtener_coordenadas():
    global disparo_jugador_x
    global disparo_jugador_y
    global break_point
    while True:
        var.disparo_jugador_x = input("Ingresa la coordenada X (entre 0 y 9) o escribe exit para salir del programa: ")
        if var.disparo_jugador_x.lower() == 'exit':  
           print("Has elegido salir del programa.")
           var.break_point += 1
           break
        
        var.disparo_jugador_y = input("Ingresa la coordenada Y (entre 0 y 9) o escribe exit para salir del programa: ")
        if var.disparo_jugador_y.lower() == 'exit':  
           print("Has elegido salir del programa.")
           var.break_point += 1
           break
        try:
            var.disparo_jugador_x = int(var.disparo_jugador_x)
            var.disparo_jugador_y = int(var.disparo_jugador_y)
            
            if 0 <= var.disparo_jugador_x <= (var.filas-1) and 0 <= var.disparo_jugador_y <= (var.columnas-1):
                break
            else:
                print("Las coordenadas no están en el rango válido (0 a 9). Inténtalo de nuevo.")
        except ValueError:
            print("Ha ocurrido un error. Asegúrate de ingresar números enteros válidos para las coordenadas.")

def disparo_jugador():
    ej = True
    contador = 0
    global break_point
    while ej:
        time.sleep(3)
        if contador != 0:
            print('¡Te toca de nuevo! \n')
            mostrar_tableros()
        else:
            print('¡Es tu turno!')
            time.sleep(1.5)
        
        obtener_coordenadas()
        if var.break_point != 0:
            break
        
        time.sleep(1)
        print(f"Disparo efectuado a las coordenadas ({var.disparo_jugador_x}, {var.disparo_jugador_y}).\n")
        suspense()

        if var.tablero_maquina[var.disparo_jugador_x, var.disparo_jugador_y] == var.c_barco:
            print('¡Impacto! ¡Barco alcanzado!\n')
            var.tablero_niebla[var.disparo_jugador_x, var.disparo_jugador_y] = var.c_tocado
            var.tablero_maquina[var.disparo_jugador_x, var.disparo_jugador_y] = var.c_tocado
            if condicion_victoria():
                break
            contador += 1
        elif var.tablero_maquina[var.disparo_jugador_x, var.disparo_jugador_y] == var.c_agua:
            print('Agua...\n')
            var.tablero_maquina[var.disparo_jugador_x, var.disparo_jugador_y] = var.c_agua_tiro
            var.tablero_niebla[var.disparo_jugador_x, var.disparo_jugador_y] = var.c_agua_tiro
            ej = False
        elif var.tablero_maquina[var.disparo_jugador_x, var.disparo_jugador_y] == var.c_tocado:
            print('Ya habías disparado ahí.\n')
            ej = False
        elif var.tablero_maquina[var.disparo_jugador_x, var.disparo_jugador_y] == var.c_agua_tiro:
            print('Agua, y ya habías disparado ahí.\n')
            ej = False

def disparo_maquina():
    ej = True
    contador = 0
    while ej:
        time.sleep(2)
        if contador != 0:
            print('¡Le toca a ShipBrainy de nuevo! \n')
        else:
            print('¡Es el turno de la máquina!')
        disparo_maquina_x = np.random.randint(0,10)
        disparo_maquina_y = np.random.randint(0,10)
        time.sleep(2)
        print(f"ShipBrainy dispara a las coordenadas ({disparo_maquina_x}, {disparo_maquina_y}).\n")
        suspense(0.5)
        if var.tablero_jugador[disparo_maquina_x, disparo_maquina_y] == var.c_barco:
            print('¡Impacto!¡Barco alcanzado!\n')
            var.tablero_jugador[disparo_maquina_x, disparo_maquina_y] = var.c_tocado
            if condicion_victoria():
                break
            contador += 1
        elif var.tablero_jugador[disparo_maquina_x, disparo_maquina_y] == var.c_agua:
            print('Agua...\n')
            var.tablero_jugador[disparo_maquina_x, disparo_maquina_y] = var.c_agua_tiro
            ej = False
        elif var.tablero_jugador[disparo_maquina_x, disparo_maquina_y] == var.c_tocado:
            print('Ya habías disparado ahí.\n')
            ej = False
        elif var.tablero_jugador[disparo_maquina_x, disparo_maquina_y] == var.c_agua_tiro:
            print('Agua, y ya habías disparado ahí.\n')
            ej = False

def condicion_victoria():
    global hay_ganadore
    ganador = False
    if (var.c_barco in var.tablero_jugador) == False:
        suspense()
        print(f'Lo siento {var.id_jugador}, gana ShipBrainy.')
        var.hay_ganadore +=1
        ganador = True
    elif (var.c_barco in var.tablero_maquina) == False:
        suspense()
        print(f'¡Enhorabuena, {var.id_jugador}! ¡Has ganado! \n Has tardado {var.turnos} turnos.')
        var.hay_ganadore +=1
        ganador = True
    return ganador