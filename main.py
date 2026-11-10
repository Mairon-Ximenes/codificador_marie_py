from conversores import *

def main():
    num = 0
    while True:
        try:
            print("==========CODIFICADOR MARIE==========")
            print("1- Tabuada")
            print("2- Sequência de Fibonacci")
            print("3- Codificador de Instruções")
            num = int(input("\nO que deseja fazer: "))
        except ValueError:
            print("Valor inválido. Tente novamente")
            continue
        options_num = [1,2,3,4]

        if num not in options_num:
            print("Valor inválido. Tente novamente")
            continue
        elif num == 1:
            pass
        elif num == 2:
            pass
        elif num == 3:
            print("\n==========Cod. Instruções==========")
            print("1- MARIE")
            print("2- Binário")
            print("3- Hexadecimal")
            while True:
                try:
                    tipo_input = int(input("\nInforme o tipo de entrada: "))
                except ValueError:
                    print("Valor inválido. Tente novamente")
                    continue
                options_entrada = [1,2,3]

                if tipo_input not in options_entrada:
                    print("Valor inválido. Tente novamente")
                    continue

                entrada = input("Entrada: ").upper().strip()

                saidas = {1: ["Saída Binária", "Saída Hexadecimal"], 2: ["Saída MARIE", "Saída Hexadecimal"],
                          3: ["Saída MARIE", "Saída Binária"]}

                saida1_txt = saidas.get(tipo_input)[0]
                saida2_txt = saidas.get(tipo_input)[1]

                saida1_code = ""
                saida2_code = ""

                if tipo_input == 1:
                    saida2_code = marie_para_hex(entrada)
                    saida1_code = hex_para_binario(saida2_code)
                elif tipo_input == 2:
                    entrada = entrada.replace(" ", "")
                    saida2_code = binario_para_hex(entrada)
                    saida1_code = hex_para_marie(saida2_code)
                elif tipo_input == 3:
                    saida1_code = hex_para_marie(entrada)
                    saida2_code = hex_para_binario(entrada)

                print()
                print(saida1_txt + ": " + saida1_code)
                print(saida2_txt + ": " + saida2_code)

                continuar = input("\nDeseja continuar? (s/n): ").lower()
                opcoes_continuar_yes = ['sim', 's', 'y']
                opcoes_continuar_nao = ['nao', 'n', 'n']
                if continuar not in opcoes_continuar_yes and continuar not in opcoes_continuar_nao:
                    break

        elif num == 4:
            break

if __name__ == "__main__":
    main()