from typing import Any

from config import HEX_PARA_MARIE, OPCODES_MARIE, OPS_SEM_ENDERECO, CONDICOES_SKIPCOND

def marie_para_hex(instrucao_str): # LOAD 015
    instrucao_list = instrucao_str.split()
    opcode = instrucao_list[0]
    hex_code = OPCODES_MARIE.get(opcode)

    if opcode in OPS_SEM_ENDERECO:
        hex_code += "000"
        return hex_code

    segunda_parte = instrucao_list[1]
    hex_code += str(segunda_parte)
    return hex_code

def hex_para_marie(hex_str):
    opcode = hex_str[0] # 1
    segunda_parte = hex_str[1:] # 015
    marie_code = HEX_PARA_MARIE.get(opcode) # LOAD

    if marie_code in OPS_SEM_ENDERECO:
        return marie_code

    marie_code += " " + segunda_parte
    return marie_code

def hex_para_binario(hex_str):
    pass
