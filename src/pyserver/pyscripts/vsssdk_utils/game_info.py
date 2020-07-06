""" Nome do módulo :        game_info
    Ano de criação :        2020/01
    Descrição do módulo :   Informações sobre o estado de jogo
    Versão :                1.0
    Pré-requisitos :        nenhum
    Membros :               Lorena "Ino" Bassani
"""

from .com_kernel import Kernel, state_to_dict
import json

""" Nome da função :     get_game_info
    Intenção da função : retorna um estado de jogo dado um kernel
    Pré-requisitos :     kernel já inicializado
    Efeitos colaterais : recebe um estado de jogo
    Parâmetros :         kernel : Kernel
    Retorno :            state : json
"""
def get_game_info(kernel : Kernel):
    return state_to_dict(kernel.receive_state())

