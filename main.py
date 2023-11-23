from colorama import Fore,Back,Style
import funciones as fun
import variables as var
fun.bienvenida()
fun.suspense()
fun.colocar_barcos()
fun.normal_test()
while True:
    fun.mostrar_tableros()
    fun.contador_turnos()
    fun.disparo_jugador()
    if var.break_point != 0:
        print(f'¡Te veo a la próxima, {var.id_jugador}!')
        break
    if var.hay_ganadore != 0:
        fun.mostrar_tableros()
        break
    fun.mostrar_tableros()
    fun.disparo_maquina()
    if var.hay_ganadore != 0:
        fun.mostrar_tableros()
        break   