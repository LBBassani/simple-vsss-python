""" Nome do módulo :        main
    Ano de criação :        2020/01
    Descrição do módulo :   função principal do python server
    Versão :                1.0
    Pré-requisitos :        nenhum
    Membros :               Lorena "Ino" Bassani
"""

# begin-imports
from pyscripts.webservices.server import run_aplication_server
from pyscripts.webservices.game_info import get_game_info
from pyscripts.webservices.move_team import move_team
from pyscripts.vsssdk_utils.com_kernel import Kernel

# end-imports

kernel = Kernel()
def get_this_game_info():
    global kernel
    return (get_game_info(kernel))

def move_this_team(robots_moves):
    global kernel
    return move_team(kernel,robots_moves)

# Roda serviços da simulação
functions = {
    "echo" : (lambda s: s),
    "get_game_info" : get_this_game_info,
    "move_team" : move_this_team,
}

run_aplication_server(functions)