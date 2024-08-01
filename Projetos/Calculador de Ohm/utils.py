def menu():
    print('')
    print('Você deseja descobrir qual valor?')
    print('0 - Sair')
    print('1 - Resistência')
    print('2 - Corrente')
    print('3 - Tensão')
    print('4 - Resistência do resistor')
    return input('>>')


def resistencia_in():
    while True:
        try:
            resistencia = float(input('Qual o valor da resistencia elétrica (Ω): '))
            if resistencia <= 0:
               raise ValueError
            return resistencia
        except ValueError:
            print('Entrada invalida. Tente novamente')


def corrente_in():
    while True:
        try:
            corrente = float(input('Qual o valor da corrente elétrica (Amper): '))
            if corrente <= 0:
                raise ValueError
            return corrente
        except ValueError:
            print('Entrada invalida. Tente novamente')


def tensao_in():
    while True:
        try:
            tensao = float(input('Qual o valor da tensão elétrica (Volts): '))
            if tensao <= 0:
                raise ValueError
            return tensao
        except ValueError:
            print('Entrada invalida. Tente novamente')


def resistencia_calculo():

    corrente = corrente_in()
    tensao = tensao_in()
    resistencia = tensao / corrente
   #print(f'O valor da resistencia é {resistencia} Ω')
    return resistencia

def corrente_calculo():
    resistencia = resistencia_in()
    tensao = tensao_in()
    corrente = tensao / resistencia
    #print(f'O valor da corrente é {corrente} A')

    return corrente


def tensao_calculo():
    resistencia = resistencia_in()
    corrente = corrente_in()
    tensao = corrente * resistencia
    #print(f'O valor da tensão é {tensao} V')
    return tensao


def resistor_calculo():
    while True:
        try:
            tensao_fonte = float(input('Qual o valor da tensão elétrica da fonte (Volts): '))
            if tensao_fonte <= 0:
                raise ValueError
            tensao_disp = float(input('Qual o valor da tensão elétrica do dispositivo (Volts): '))
            if tensao_disp <= 0:
                raise ValueError
            corrente = float(input('Qual o valor da corrente elétrica do dispositivo (Amper): '))
            if corrente <= 0:
                raise ValueError
            resist_resistor = (tensao_fonte - tensao_disp) / corrente
            #print(f'O valor da resistência do resistor é {resist_resistor} Ω')
            break
        except ValueError:
            print('Entrada inválida')
    return resist_resistor


def exibir_resultado(unidade, resultado, un):
    print(f'\nO valor da {unidade} é {resultado} ({un})')