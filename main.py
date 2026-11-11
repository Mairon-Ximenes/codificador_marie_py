from conversores import *
from validadores import *

def main():
    while True:
        try:
            # menu bonitinho
            print("==========CODIFICADOR MARIE==========")
            print("1- MARIE")
            print("2- Binário")
            print("3- Hexadecimal")
            print("4- Sair")
            tipo_input = int(input("\nInforme o tipo de entrada: "))
        except ValueError:
            # except caso coloque valor inválido. Ex: a
            print("Valor inválido. Tente novamente\n")
            continue

        if tipo_input == 4:
            print("Obrigado por usar nosso Codificador de Instruções MARIE!")
            break

        # verifica se está dentro dessas opções
        if tipo_input not in [1, 2, 3]:
            print("Opção inválida. Tente novamente\n")
            continue

        while True:
            # apenas formata a entrada
            entrada = input("Entrada: ").upper().strip()

            # validação do tipo
            entrada_valida = True
            if tipo_input == 1:
                entrada_valida = validador_marie(entrada)
            elif tipo_input == 2:
                entrada_valida = validador_bin(entrada)
            elif tipo_input == 3:
                entrada_valida = validador_hex(entrada)

            if not entrada_valida:
                print("Formato inválido para o tipo escolhido! Verifique o padrão e tente novamente.\n")
                continue

            # dict com as saídas pra padronizar e fazer dois únicos prints no final
            saidas = {
                1: ["Saída Binária", "Saída Hexadecimal"],
                2: ["Saída MARIE", "Saída Hexadecimal"],
                3: ["Saída MARIE", "Saída Binária"]
            }

            saida1_txt = saidas.get(tipo_input)[0]
            saida2_txt = saidas.get(tipo_input)[1]

            saida1_code = ""
            saida2_code = ""

            # aqui só faz as conversões e salva os valores
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

            # print das saídas formatadas
            print()
            print(f"{saida1_txt}: {saida1_code}")
            print(f"{saida2_txt}: {saida2_code}")

            # loop até o usuário responder certo
            while True:
                continuar = input("\nDeseja continuar com o mesmo tipo de entrada? (s/n): ").lower()

                # verificacao da resposta do usuário
                if continuar not in ['nao', 'n'] and continuar not in ['sim', 's']:
                    print("Opção inválida. Tente novamente")
                else:
                    break

            if continuar in ['nao', 'n']:
                print()
                break

if __name__ == "__main__":
    main()