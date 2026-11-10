import conversores

def main():
    print("==========CODIFICADOR MARIE==========\n")
    print("1- Tabuada")
    print("2- Sequência de Fibonacci")
    print("3- Codificador de Instruções")
    num = int(input("O que deseja fazer: "))

    if num == 3:
        print()
        while True:
            entrada = input("Informe o dado de entrada: ").upper()
            #codigo = conversores.marie_para_hex(entrada)
            #codigo = conversores.hex_para_marie(entrada)
            codigo = conversores.hex_para_binario(entrada)
            print(codigo)
            break


if __name__ == "__main__":
    main()