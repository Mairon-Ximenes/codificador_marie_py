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
            hex_code = conversores.marie_para_hex(entrada)
            print(hex_code)
            break


if __name__ == "__main__":
    main()