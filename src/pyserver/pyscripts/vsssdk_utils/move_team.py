""" Nome do módulo :        move_robot
    Ano de criação :        2020/01 
    Descrição do módulo :   movimenta um time de robôs
    Versão :                1.0
    Pré-requisitos :        json
                            kernel
    Membros :               Lorena "Ino" Bassani
"""

from .com_kernel import Kernel

""" Nome da função :     move_team
    Intenção da função : movimentar um time
    Pré-requisitos :     kernel iniciado
    Efeitos colaterais : movimenta os robôs do time que o kernel comanda
    Parâmetros :         kernel : Kernel
                         robots_moves : List([vel1, vel2]*3)
    Retorno :            True
"""
def move_team(kernel : Kernel, robots_moves):
    kernel.send_command(robots_moves)
    return True