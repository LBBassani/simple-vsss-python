""" Nome do módulo :        move_robot
    Ano de criação :        2020/01 
    Descrição do módulo :   movimenta um time de robôs
    Versão :                1.0
    Pré-requisitos :        json
                            kernel
    Membros :               Lorena "Ino" Bassani
"""

from ..vsssdk_utils.com_kernel import Kernel

def move_team(kernel : Kernel, robots_moves):
    kernel.send_command(robots_moves)
    return True