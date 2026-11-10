from config import OPCODES_MARIE, HEX_PARA_MARIE, OPS_SEM_ENDERECO, MAPEAMENTO, MAPEAMENTO_INV

def marie_para_hex(instrucao_str):
    instrucao_list = instrucao_str.upper().split()
    opcode = instrucao_list[0]
    hex_code = OPCODES_MARIE.get(opcode)

    if opcode in OPS_SEM_ENDERECO:
        return hex_code + "000"

    endereco = instrucao_list[1]
    return hex_code + endereco


def hex_para_marie(hex_str):
    hex_clean = hex_str.strip().upper()
    opcode_hex = hex_clean[0]
    segunda_parte = hex_clean[1:]
    marie_code = HEX_PARA_MARIE.get(opcode_hex)

    if marie_code in OPS_SEM_ENDERECO:
        return marie_code

    if marie_code == "SKIPCOND":
        return f"Skipcond {segunda_parte}"

    nome_formatado = marie_code.title()
    return f"{nome_formatado} {segunda_parte}"


def hex_para_binario(hex_str):
    hex_str = hex_str.strip().upper()
    bin_code = ""

    for char in hex_str:
        if bin_code:
            bin_code += " "
        bin_code += MAPEAMENTO.get(char)

    return bin_code


def binario_para_hex(bin_str):
    bin_clean = bin_str.replace(" ", "").strip()
    hex_code = ""

    for i in range(0, len(bin_clean), 4):
        grupo = bin_clean[i:i+4]
        hex_code += MAPEAMENTO_INV.get(grupo)

    return hex_code