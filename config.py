OPCODES_MARIE = {
    "JNS": "0",
    "LOAD": "1",
    "STORE": "2",
    "ADD": "3",     
    "SUBT": "4",
    "INPUT": "5",
    "OUTPUT": "6",
    "HALT": "7",
    "SKIPCOND": "8",
    "JUMP": "9",
    "CLEAR": "A",
    "ADDI": "B",
    "JUMPI": "C",
    "STOREI": "D"
}

# Dicionário invertido para busca rápida
HEX_PARA_MARIE = {v: k for k, v in OPCODES_MARIE.items()}

# Instruções que NÃO usam endereço de memória
OPS_SEM_ENDERECO = {"HALT", "INPUT", "OUTPUT", "CLEAR"}

# Condições válidas permitidas para a instrução SKIPCOND
CONDICOES_SKIPCOND = {"000", "400", "800"}

MAPEAMENTO = {
    '0': '0000', '1': '0001', '2': '0010', '3': '0011',
    '4': '0100', '5': '0101', '6': '0110', '7': '0111',
    '8': '1000', '9': '1001', 'A': '1010', 'B': '1011',
    'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'
}

MAPEAMENTO_INV = {v: k for k, v in MAPEAMENTO.items()}