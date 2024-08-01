def menu():
    print('')
    print('[0]Sair\n[1]Soma\n[2]Subtração\n[3]Multiplicação\n[4]Divisão\n[5]Todas juntas')
    opcao = input('>>')
    while opcao not in ['1', '2', '3', '4', '5', '0']:
        print('Tente novamente com números de 1 a 4')
        opcao = input('>>')
    return opcao


def entrada_numero(valor):
    while True:
        try:
            numero = float(input(f'Insira o número {valor} : '))
            return numero
        except ValueError:
            print('Entrada invalida')


def operacao_multiplicacao(numero_1, numero_2):
    multiplicacao = numero_1 * numero_2
    return multiplicacao


def operacao_divisao(numero_1, numero_2):
    divisao = numero_1 / numero_2
    return divisao


def operacao_soma(numero_1, numero_2):
    soma = numero_1 + numero_2
    return soma

def operacao_subtracao(numero_1, numero_2):
    subtracao = numero_1 - numero_2
    return subtracao


def exibir_mensagem(opcao, opcao_soma, opcao_subtracao, opcao_multiplicacao, opcao_divisao, operacao_subtracao, operacao_soma, operacao_divisao, operacao_multiplicacao):
    if opcao == opcao_soma:
        soma = operacao_soma(numero_1, numero_2)
        print(f'Soma = {soma}')
    elif opcao == opcao_divisao:
        divisao = operacao_divisao(numero_1, numero_2)
        print(f'Divisao = {divisao}')
    elif opcao == opcao_multiplicacao:
        multiplicacao = operacao_multiplicacao(numero_1, numero_2)
        print(f'Multiplicacao = {multiplicacao}')
    elif opcao == opcao_subtracao:
        subtracao = operacao_subtracao(numero_1, numero_2)
        print(f'Subtração = {subtracao}')
    elif opcao == opcao_todas:
        soma = operacao_soma(numero_1, numero_2)
        subtracao = operacao_subtracao(numero_1, numero_2)
        multiplicacao = operacao_multiplicacao(numero_1, numero_2)
        divisao = operacao_divisao(numero_1, numero_2)
        print(f'Soma = {soma}')
        print(f'Subtração = {subtracao}')
        print(f'Multiplicacao = {multiplicacao}')
        print(f'Divisao = {divisao}')


sair = '0'
opcao_soma = '1'
opcao_subtracao = '2'
opcao_multiplicacao = '3'
opcao_divisao = '4'
opcao_todas = '5'

while True:

    opcao = menu()
    if opcao == sair:
        print('\nSaindo do programa...')
        break


    numero_1 = entrada_numero('1')

    numero_2 = entrada_numero('2')
    exibir_mensagem(opcao, opcao_soma, opcao_subtracao, opcao_multiplicacao, opcao_divisao, operacao_subtracao, operacao_soma, operacao_divisao, operacao_multiplicacao)
