import conversores
from validadores import *


def main():
    print("==========CODIFICADOR MARIE==========\n")
    print("1- Tabuada")
    print("2- Sequência de Fibonacci")
    print("3- Codificador de Instruções")
    num = int(input("O que deseja fazer: "))

    if num == 3:
        print()
        while True:
            entrada = input("Entrada: ").upper()
            #identificar o tipo de entrada
            tipo = tipo_entrada(entrada)
            if tipo == "bin":
                while True:
                    if not validador_bin():
                        break
                    codigo_hex = conversores.binario_para_hex(entrada)
                    codigo_marie = conversores.hex_para_marie(codigo_hex)
                    print("Saída MARIE: " + codigo_marie)
                    print("Saída Hexadecimal: " + codigo_hex)
                    if input() != "Sim":
                        break

            elif tipo == "marie":
                while True:
                    codigo_hex = conversores.marie_para_hex(entrada)
                    codigo_bin = conversores.hex_para_binario(codigo_hex)
                    print("Saída Binária: " + codigo_bin)
                    print("Saída Hexadecimal: " + codigo_hex)
                    if input() != "Sim":
                        break

            elif tipo == "hex":
                while True:
                    codigo_marie = conversores.hex_para_marie(entrada)
                    codigo_binario = conversores.hex_para_binario(entrada)
                    print("Saída MARIE: " + codigo_marie)
                    print("Saída Binária: " + codigo_binario)
                    if input() != "Sim":
                        break


if __name__ == "__main__":
    main()