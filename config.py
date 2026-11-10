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

# dict invertido para caso precise buscar o opcode e pegar o comando. Ex: {"LOAD": "1"} -> {"1": "LOAD"}
HEX_PARA_MARIE = {v: k for k, v in OPCODES_MARIE.items()}

OPS_SEM_ENDERECO = {"HALT", "INPUT", "OUTPUT", "CLEAR"}

CONDICOES_SKIPCOND = {"000", "400", "800"}