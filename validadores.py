from config import OPCODES_MARIE, OPS_SEM_ENDERECO


def validador_marie(marie_str):
    if not marie_str:
        return False

    partes = marie_str.split()
    if not partes:
        return False

    opcode = partes[0]

    # Verifica se o opcode existe
    if opcode not in OPCODES_MARIE:
        return False

    # Se não tem endereço, não deve ter segunda parte
    if opcode in OPS_SEM_ENDERECO:
        if len(partes) == 1:
            return True
        else:
            return False

    # Verifica se tem o endereço, se tiver, ele deve ter três casas
    if len(partes) == 2:
        endereco = partes[1]
        if len(endereco) == 3:
            for c in endereco:
                if c not in "0123456789ABCDEF":
                    return False
        return False

    return True


def validador_hex(hex_str):
    if not hex_str or len(hex_str) != 4:
        return False

    for c in hex_str:
        if c not in "0123456789ABCDEF":
            return False

    return True


def validador_bin(bin_str):
    if not bin_str:
        return False

    bin_limpo = bin_str.replace(" ", "")

    if len(bin_limpo) != 16:
        return False

    for c in bin_limpo:
        if c not in "01":
            return False

    return True