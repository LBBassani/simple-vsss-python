""" Nome do módulo :        main
    Ano de criação :        2020/01
    Descrição do módulo :   função principal do python server
    Versão :                1.0
    Pré-requisitos :        nenhum
    Membros :               Lorena "Ino" Bassani
"""

# begin-imports
from webservices.server import run_aplication_server

# end-imports

# Roda um pequeno serviço de soma e subtração de dois números
functions = {
    "echo" : (lambda s: s),
    "add" : (lambda a, b: a + b),
    "sub" : (lambda a, b: a - b),
}

run_aplication_server(functions)