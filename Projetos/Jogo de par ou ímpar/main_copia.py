import random

pontuacao_user = 0
pontuacao_cpu = 0

print('Jogo de par ou ímpar')
print('Powered by LevelUp')
print('Escolha par ou ímpar e insira um número de 0 a 10')


while True:
    try:

        usuario_escolha = int(input('\nVocê deseja ser par ou ímpar?\n\n[1]Ímpar\n[2]Par\n'))

        numero_aleatorio = random.randint(1, 5)

        while usuario_escolha != 1 and usuario_escolha != 2:
            print('Tente novamente com 1 ou 2')
            usuario_escolha = int(input('\nVocê deseja ser par ou ímpar?\n\n[1]Ímpar\n[2]Par\n'))

        if usuario_escolha == 1:
            print('Ok! sou par')
            numero_usuario = int(input('digite um número entre 0 e 5: '))
            while numero_usuario < 0 or numero_usuario > 5:
                print('Tente novamente entre 0 e 10')
                numero_usuario = int(input('digite um número entre 0 e 5: '))
            total = numero_usuario + numero_aleatorio
            print(f'CPU: {numero_aleatorio} + User: {numero_usuario} = {total}')
            if total % 2 == 0:
                print('ponto pra mim')
                pontuacao_cpu += 1
            else:
                print('Ponto pra voce')
                pontuacao_user += 1

        elif usuario_escolha == 2:
            print('OK! sou impar')
            numero_usuario = int(input('digite um número entre 0 e 5: '))
            while numero_usuario < 0 or numero_usuario > 5:
                print('Tente novamente entre 0 e 10')
                numero_usuario = int(input('digite um número entre 0 e 5: '))
            total = numero_usuario + numero_aleatorio
            print(f'CPU: {numero_aleatorio} + User: {numero_usuario} = {total}')
            if total % 2 == 0:
                print('ponto pra voce')
                pontuacao_user += 1
            else:
                print('Ponto pra mim')
                pontuacao_cpu += 1

        jogar_novamente = int(input('Deseja jogar novamente?\n[0]Sair\n[1]Jogar novamente\n'))

        while jogar_novamente != 1 and jogar_novamente != 0:
            jogar_novamente = int(input('Deseja jogar novamente?\n[0]Sair\n[1]Jogar novamente\n'))

        if jogar_novamente == 0:
            print(f'PONTUAÇÃO\nCPU: {pontuacao_cpu}\nUser: {pontuacao_user}')
            print('OK! Encerrando')
            break

    except ValueError:
        print('Tente novamente!! Entrada inválida')
