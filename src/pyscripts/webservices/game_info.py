""" Nome do módulo :        game_info
    Ano de criação :        2020/01
    Descrição do módulo :   Informações sobre o estado de jogo
    Versão :                1.0
    Pré-requisitos :        nenhum
    Membros :               Lorena "Ino" Bassani
"""

from ..vsssdk_utils.com_kernel import Kernel, state_to_dict
import json

def get_game_info(kernel : Kernel):
    state = state_to_dict(kernel.receive_state())
    return json.dumps(state)
