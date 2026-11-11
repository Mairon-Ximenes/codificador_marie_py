from config import OPCODES_MARIE, HEX_PARA_MARIE, OPS_SEM_ENDERECO, CONDICOES_SKIPCOND, MAPEAMENTO_INV

def validador_marie(marie_str):
    if not marie_str:
        return False

    partes = marie_str.upper().split()
    if not partes:
        return False

    opcode = partes[0]

    # 1) verifica se o opcode existe na MARIE
    if opcode not in OPCODES_MARIE:
        return False

    # 2) instruções sem endereço não podem ter argumentos adicionais
    if opcode in OPS_SEM_ENDERECO:
        return len(partes) == 1

    # 3) validação do SKIPCOND (tem que ser 000, 400 ou 800)
    if opcode == "SKIPCOND":
        if len(partes) != 2:
            return False
        if partes[1] not in CONDICOES_SKIPCOND:
            return False

    # 4) Instruções com endereço (LOAD, STORE, ADD, JUMP, etc.)
    if opcode not in OPS_SEM_ENDERECO and opcode != "SKIPCOND":
        if len(partes) != 2:
            return False
        endereco = partes[1]
        if len(endereco) != 3:
            return False
        for c in endereco:
            if c not in "0123456789ABCDEF":
                return False

    return True


def validador_hex(hex_str):
    if not hex_str or len(hex_str) != 4:
        return False

    hex_str = hex_str.upper()
    for c in hex_str:
        if c not in "0123456789ABCDEF":
            return False

    op_hex = hex_str[0]
    endereco_hex = hex_str[1:]

    # verifica se o primeiro dígito é um opcode válido
    if op_hex not in HEX_PARA_MARIE:
        return False

    op_nome = HEX_PARA_MARIE.get(op_hex)

    # instrução sem endereço precisa ter '000' no final
    if op_nome in OPS_SEM_ENDERECO:
        if endereco_hex != "000":
            return False

    # validação do SKIPCOND em hexadecimal
    if op_nome == "SKIPCOND":
        if endereco_hex not in CONDICOES_SKIPCOND:
            return False

    return True


def validador_bin(bin_str):
    if not bin_str:
        return False

    bin_limpo = bin_str.replace(" ", "").strip()

    if len(bin_limpo) != 16 or not all(c in "01" for c in bin_limpo):
        return False

    # converte o binário limpo para hexadecimal
    hex_equiv = ""
    for i in range(0, 16, 4):
        grupo = bin_limpo[i:i+4]
        hex_equiv += MAPEAMENTO_INV.get(grupo, "")

    # reutiliza as regras semânticas do validador hexadecimal
    return validador_hex(hex_equiv)