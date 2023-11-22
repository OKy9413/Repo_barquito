import funciones as fun
import variables as var

fun.suspense()

fun.contador_turnos()

fun.disparo_jugador()

fun.mostrar_tableros()

fun.colocar_barco_aleatorio()

fun.get_celdas_alrededor()

fun.posicionar_barco()

fun.colocar_barco()

fun.colocar_barco_maquina()

fun.disparo_jugador()

fun.disparo_maquina()

fun.condicion_victoria()




QUEDA ORGANIZAR PARA QUE SE EJECUTE (LO ULTIMO)

while True:
    mostrar_tableros()
    contador_turnos()
    disparo_jugador()
    if break_point != 0:
        print(f'¡Te veo a la próxima, {id_jugador}!')
        break
    if hay_ganadore != 0:
        mostrar_tableros()
        break
    mostrar_tableros()
    disparo_maquina()
    if hay_ganadore != 0:
        mostrar_tableros()
        break
        
