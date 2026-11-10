def tipo_entrada(entrada_str):
    if len(entrada_str) > 16:
        return "bin"
    if len(entrada_str) > 4:
        return "marie"

    return "hex"