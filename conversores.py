from config import *

def marie_para_hex(instrucao_str): # LOAD 015
    instrucao_list = instrucao_str.split()
    opcode = instrucao_list[0]
    hex_code = OPCODES_MARIE.get(opcode)

    if opcode in OPS_SEM_ENDERECO:
        hex_code += "000"
        return hex_code

    segunda_parte = instrucao_list[1]
    return hex_code + str(segunda_parte)

def hex_para_marie(hex_str):
    opcode = hex_str[0] # 1
    segunda_parte = hex_str[1:] # 015
    marie_code = HEX_PARA_MARIE.get(opcode) # LOAD

    if marie_code in OPS_SEM_ENDERECO:
        return marie_code

    return (marie_code + " " + segunda_parte).title()

def hex_para_binario(hex_str):
    bin_code = ""
    for char in hex_str[1:]:
        if bin_code:
            bin_code += " "
        bin_code += MAPEAMENTO.get(char)
    return bin_code

def binario_para_hex(bin_str):
    # TODO: VERIFICAR SE TANDO CERTO AQUI
    bin_str = bin_str.replace(" ", "")
    hex_code = ""

    # for pegando string a cada 4 caracteres
    for i in range(0, len(bin_str), 4):
        string = bin_str[i:i+4]
        hex_code += MAPEAMENTO_INV.get(string)

    return hex_code
