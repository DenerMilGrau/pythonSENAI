def entrada_numero_1():
    while True:
        try:
            numero_1 = float(input('Insira o número 1: '))
            return numero_1
        except ValueError:
            print('Entrada invalida')


def entrada_numero_2():
    while True:
        try:
            numero_2 = float(input('Insira o número 2: '))
            return numero_2
        except ValueError:
            print('Entrada invalida')


def operacoes_basicas(numero_1, numero_2):
    soma = numero_1 + numero_2
    multiplicacao = numero_1 * numero_2
    subtracao = numero_1 - numero_2
    divisao = numero_1 / numero_2
    print(f'Soma: {soma}')
    print(f'Multiplicacao: {multiplicacao}')
    print(f'Divisao: {divisao}')
    print(f'Subtração: {subtracao}')


numero_1 = entrada_numero_1()
numero_2 = entrada_numero_2()
operacoes_basicas(numero_1, numero_2)