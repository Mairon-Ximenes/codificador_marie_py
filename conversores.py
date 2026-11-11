from config import *

def marie_para_hex(instrucao_str):
    # aqui a gnt pega o valor da instrução em string, transforma em uma lista e faz a conversão
    instrucao_list = instrucao_str.split()
    opcode = instrucao_list[0]

    # pega o valor correspondente no dictionary
    hex_code = OPCODES_MARIE.get(opcode)

    # verifica se o opcode não tem endereço e adiciona 000 pra completar o codigo em hexadecimal
    if opcode in OPS_SEM_ENDERECO:
        hex_code += "000"
        return hex_code

    # aqui ele só adiciona o resto do endereço
    segunda_parte = instrucao_list[1]
    return hex_code + str(segunda_parte)

def hex_para_marie(hex_str):
    # aqui pegamos o primeiro elemento do valor hexadecimal
    opcode = hex_str[0]

    # aqui pegamos o resto
    segunda_parte = hex_str[1:] # 015

    # pegar o comando. Ex: LOAD
    marie_code = HEX_PARA_MARIE.get(opcode)

    # se esta na lista que não tem endereço, retorna somente o comando. Ex: CLEAR
    if marie_code in OPS_SEM_ENDERECO:
        return marie_code

    # aqui só faz a formatação e junta com o resto do endereço
    return marie_code.title() + " " + segunda_parte.upper()

def hex_para_binario(hex_str):  
    bin_code = ""

    # percorre cada caractere do valor em hexadecimal e adiciona o valor em binario relacionado
    for char in hex_str:
        # aqui só verifica pra colocar espaços no meio
        if bin_code:
            bin_code += " "
        bin_code += MAPEAMENTO.get(char)
    return bin_code

def binario_para_hex(bin_str):
    # faz esse replace pra tirar os espaços e juntar todos os caracteres
    bin_str = bin_str.replace(" ", "")
    hex_code = ""

    # loop for pegando string a cada 4 caracteres
    for i in range(0, len(bin_str), 4):
        # aqui usa slicing pra começar no elemento i até 4 casas dps
        string = bin_str[i:i+4]
        hex_code += MAPEAMENTO_INV.get(string).upper()

    return hex_code
