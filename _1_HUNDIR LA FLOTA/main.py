import funciones as fun
import variables as var

while True:
    fun.bienvenida()
    fun.mostrar_tableros()
    fun.contador_turnos()
    fun.disparo_jugador()
    if break_point != 0:
        print(f'¡Te veo a la próxima, {id_jugador}!')
        break
    if hay_ganadore != 0:
        fun.mostrar_tableros()
        break
    fun.mostrar_tableros()
    fun.disparo_maquina()
    if hay_ganadore != 0:
        fun.mostrar_tableros()
        break