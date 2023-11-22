from colorama import Fore, Back, Style
import numpy as np
import random
import time
import variables as var

def bienvenida():
    global var.id_jugador
    print(f"{Fore.CYAN}Bienvenid@ al juego de 'Hundir la Flota'{Style.RESET_ALL}")
    var.id_jugador= input(f"¿Cómo te gustaría que te llamara?")
    time.sleep(1)
    print(f"{Fore.CYAN}Encantado de conocerte: \U0001F99A{Style.BRIGHT}{Fore.WHITE}{Back.BLACK}\033[4m{var.id_jugador}\033[0m{Style.RESET_ALL}, {Fore.CYAN}soy tu oponente: \U0001F916{Fore.WHITE}{Back.BLACK}\033[4mShipBrainy\033[0m{Style.RESET_ALL}{Fore.CYAN}, un experimentado estratega, asi que prepárate para perder...{Style.RESET_ALL}" )
    time.sleep(4.5)
    print(f"{Fore.CYAN}Estas son las instrucciones del juego:{Style.RESET_ALL}")
    time.sleep(4.5)
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
    time.sleep(10)
    print(f"\U0001F99A{Style.BRIGHT}{Fore.CYAN}{var.id_jugador}{Style.RESET_ALL}, {Fore.CYAN}¿Tienes las instrucciones claras(S/N)?{Style.RESET_ALL}")
    comprobar = True
    while comprobar:
          var.id_jugador= input(f"\U0001F99A{Style.BRIGHT}{Fore.WHITE}{Back.BLACK}\033[4m{var.id_jugador}\033[0m{Style.RESET_ALL},{Fore.CYAN}¿Tienes las instrucciones claras(Y/N)?")
          if var.id_jugador == "S": 
               print(f"{Fore.CYAN}Comienza el ¡¡DESAFÍO!!{Style.RESET_ALL}")
               comprobar = False
               continue  
          elif var.id_jugador =="N":
               print(f"{Fore.CYAN}Eres un poco {Style.BRIGHT}TORPE{Style.RESET_ALL}{Fore.CYAN}...😈😈😈, asi que, léete de nuevo las instrucciones que te he dado 😂")
               print(f"{Fore.CYAN}Si estás preparad@ pulsa: S, y si quieres comenzar de nuevo: N.")
               input(f"Si estás preparad@ pulsa: S, y si quieres comenzar de nuevo: N.{Style.RESET_ALL}")
               if var.id_jugador == "S":
                    continue
               elif var.id_jugador == "N":
                    comprobar == False
          else:
               print(f"{Fore.CYAN}Error: ingresa la letra correcta: S o N{Style.RESET_ALL}")
    
    comprobar = True
    while comprobar:
          if var.id_jugador == "S":
               print(f"{Fore.CYAN}¿Algo que decirme antes de comenzar?") 
               input(f"{Fore.CYAN}¿Algo que decirme antes de comenzar?")
               print(f"{Fore.CYAN}Si,si...lo que tu digas😂..¡¡PREPÁRATE!!😠😠...{Style.RESET_ALL}")
               print(f"{Fore.CYAN}Sabes que perderás😂😂😂😂😂, comienza el ¡¡DESAFÍO!!{Style.RESET_ALL} ")
               comprobar = False
          elif var.id_jugador == "N":
               
              
          
            return bienvenida

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
    if turnos == 0:                                                     
        print('¡Este es el campo de batalla!', end= '\n\n')
        time.sleep(1)
        print(f'Tu tablero:\n{tablero_jugador}\nTablero de ShipBrainy:\n{tablero_niebla} \n')
        time.sleep(3)
        print('Ahora, ¡A los cañones!', end= '\n\n')
    else:
        time.sleep(3)
        print(f'Tu tablero:\n{tablero_jugador}\nTablero de ShipBrainy:\n{tablero_niebla} \n')


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
    for x, y in coordenadas:
        tablero[x][y] = 'O'

def colocar_barco():
    for tam_barco, cantidad in barcos_jugador.items():
        for i in range(cantidad):
            colocar_barco_aleatorio(tablero_jugador, tan_barco)

def colocar_barco_maquina():
    for tam_barco, cantidad in barcos_maquina.items():
        for i in range(cantidad):
            colocar_barco_aleatorio(tablero_maquina, tam_barco)


def obtener_coordenadas():
    global disparo_jugador_x
    global disparo_jugador_y
    global break_point
    while True:
        disparo_jugador_x = input("Ingresa la coordenada X (entre 0 y 9): ")
        #if disparo_jugador_x.lower() == 'exit':  # Verifica si se ingresa 'exit' para salir del programa
        #    print("Has elegido salir del programa.")
        #    break_point += 1
        #    break
        
        disparo_jugador_y = input("Ingresa la coordenada Y (entre 0 y 9): ")
        #if disparo_jugador_y.lower() == 'exit':  # Verifica si se ingresa 'exit' para salir del programa
        #    print("Has elegido salir del programa.")
        #    break_point += 1
        #    break
        try:
            disparo_jugador_x = int(disparo_jugador_x)
            disparo_jugador_y = int(disparo_jugador_y)
            
            if 0 <= disparo_jugador_x <= (filas-1) and 0 <= disparo_jugador_y <= (columnas-1):
                break
            else:
                print("Las coordenadas no están en el rango válido (0 a 9). Inténtalo de nuevo.")
        except ValueError:
            print("Ha ocurrido un error. Asegúrate de ingresar números enteros válidos para las coordenadas.")

def disparo_jugador():
    ej = True
    contador = 0
    comprobar = True
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
        
        time.sleep(1)
        print(f"Disparo efectuado a las coordenadas ({disparo_jugador_x}, {disparo_jugador_y}).\n")
        suspense()

        if tablero_maquina[disparo_jugador_x, disparo_jugador_y] == c_barco:
            print('¡Impacto! ¡Barco alcanzado!\n')
            tablero_niebla[disparo_jugador_x, disparo_jugador_y] = c_tocado
            tablero_maquina[disparo_jugador_x, disparo_jugador_y] = c_tocado
            if condicion_victoria():
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
            print('¡Le toca a ShipBrainy de nuevo! \n')
        else:
            print('¡Es el turno de la máquina!')
        disparo_maquina_x = np.random.randint(0,10)
        disparo_maquina_y = np.random.randint(0,10)
        time.sleep(2)
        print(f"ShipBrainy dispara a las coordenadas ({disparo_maquina_x}, {disparo_maquina_y}).\n")
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
    if (c_barco in tablero_jugador) == False:
        suspense()
        print(f'Lo siento {var.id_jugador}, gana ShipBrainy.')
        hay_ganadore +=1
        ganador = True
    elif (c_barco in tablero_maquina) == False:
        suspense()
        print(f'¡Enhorabuena, {var.id_jugador}! ¡Has ganado! \n Has tardado {turnos} turnos.')
        hay_ganadore +=1
        ganador = True
    return ganador
    
    
    