from utils import *

# Variáveis para verificar a escolha
sair = '0'
opcao_resistencia = '1'
opcao_corrente = '2'
opcao_tensao = '3'
opcao_resistor = '4'

print('Calculadora de resistência, corrente e tensão')

escolha = menu()

while True:

    if escolha == sair:
        print('Ok!Encerrando')
        break

    elif escolha == opcao_resistencia:
        print('Ok! Realizando cálculo da resistência')

        exibir_resultado('resistência', resistencia_calculo(), 'Ω')

    elif escolha == opcao_corrente:
        print('Ok! Realizando cálculo da corrente')

        exibir_resultado('corrente', corrente_calculo(), 'Amper')

    elif escolha == opcao_tensao:
        print('Ok! Realizando cálculo da tensão')


        exibir_resultado('tensão', tensao_calculo(), 'Volts')

    elif escolha == opcao_resistor:
        print('Ok! Realizando cálculo do resistor')

        exibir_resultado('resistência do resistor', resistor_calculo(), 'Ω')

    else:
        print('Entrada inválida. Experimente valores de 0 a 4')

    escolha = menu()