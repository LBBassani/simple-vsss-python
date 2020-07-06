""" Nome do módulo :        main
    Ano de criação :        2020/01
    Descrição do módulo :   função principal do python server
    Versão :                1.0
    Pré-requisitos :        nenhum
    Membros :               Lorena "Ino" Bassani
"""

# begin-imports
from pyscripts.webservices.server import run_aplication_server
from pyscripts.vsssdk_utils.game_info import get_game_info
from pyscripts.vsssdk_utils.move_team import move_team
from pyscripts.vsssdk_utils.com_kernel import Kernel
from pyscripts.velcontroller.controller import bot_vel_controller

import threading
import random

# end-imports

controllers = [bot_vel_controller(0,10,-10,0), bot_vel_controller(1,0,0,0), bot_vel_controller(2,0,0,0)]

kernel = Kernel()
def get_this_game_info():
    global kernel
    return (get_game_info(kernel))

def move_this_team(robots_moves):
    global kernel
    for i in range(len(robots_moves)):
        robots_moves[i][0] = float(robots_moves[i][0])
        robots_moves[i][1] = float(robots_moves[i][1])
        controllers[i].move(robots_moves[i][0], robots_moves[i][1],0)
    return move_team(kernel,robots_moves)

# Roda serviços da simulação
functions = {
    "echo" : (lambda s: s),
    "get_game_info" : get_this_game_info,
    "move_team" : move_this_team,
    "tell_the_controllers" : (lambda : [[controllers[0].vel_x, controllers[0].vel_y],[controllers[1].vel_x, controllers[1].vel_y],[controllers[2].vel_x, controllers[2].vel_y]]),
}

x = threading.Thread(target=run_aplication_server, args = (functions,))
x.start()