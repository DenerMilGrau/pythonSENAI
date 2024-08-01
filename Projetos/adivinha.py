import random

sair = '0'

print('Jogo de adivinhação\n')
print('Powered by LevelUp\n')
print('INSTRUÇÕES:\nSerá selecionado um número de 0 a 100 que você terá que adivinhar')
print('serão fornecidas dicas a cada tentativa de adivinhar')


while True:
    try:
        numero_aleatorio = random.randint(0, 100)
        while True:
            try:
                numero_usuario = int(input('Adivinhe o número: '))
                while numero_usuario < 0 or numero_usuario > 100:
                    print('Tente novamente. Experimente valore  de 0 a 100')
                    numero_usuario = int(input('Adivinhe o número: '))
                if numero_usuario == numero_aleatorio:
                    print('\nBOA! você acertou o número!!\n')
                    break
                else:
                    if numero_usuario < numero_aleatorio:
                        print('\nO número misterioso é maior\n')
                    elif numero_usuario > numero_aleatorio:
                        print('\nO número misterioso é menor\n')

            except ValueError:
                print('Tente novamente. Valor inválido')

        jogar_novamente = input('Quer jogar novamente?\n[0]Sair\n[1]Jogar de novo\n')

        while jogar_novamente != '1' and jogar_novamente != '0':
            print('Entrada inválida. Tente com 1 ou 0')
            jogar_novamente = input('Quer continuar?\n\n[0]Sair\n[1]Jogar de novo\n')
        if jogar_novamente == sair:
            print('OK! Encerrando o programa!')
            print('Obrigado por jogar!!!😁')

            break

    except ValueError:
        print('Tente novamente. Valor inválido')