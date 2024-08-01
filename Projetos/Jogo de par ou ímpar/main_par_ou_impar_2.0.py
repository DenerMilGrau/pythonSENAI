import random

resultado = ''
pontuacao_user = 0
pontuacao_cpu = 0
par = '2'
impar = '1'

print('Jogo de par ou ímpar\n')
print('Powered by LevelUp\n')
print('Escolha par ou ímpar e insira um número de 0 a 5')

while True:
    try:
        usuario_escolha = input('Selecione par ou impar:\n[1]Impar\n[2]Par:\n')
        while usuario_escolha not in ['1', '2']:
            print('Entrada inválida. Experimente com 1 ou 2.')
            usuario_escolha = input('Selecione par ou impar:\n[1]Impar\n[2]Par:\n')
        if usuario_escolha == '1':
            print('OK! você é impar e eu sou par\n')
        else:
            print('OK! você é par e eu sou impar\n')
        while True:
            try:
                numero_aleatorio = random.randint(1, 5)
                numero_usuario = int(input('Digite um número de 0 a 5: '))
                while numero_usuario < 0 or numero_usuario > 5:
                    print('Tente novamente com valores entre 0 e 5')
                    numero_usuario = int(input('Digite um número de 0 a 5: '))

                total = numero_usuario + numero_aleatorio
                print(f'\nCPU: {numero_aleatorio} + User: {numero_usuario} = {total}')
                if total % 2 == 0:
                    resultado = par
                    print('Deu par!')
                elif total % 2 != 0:
                    resultado = impar
                    print('Deu impar!')
                if resultado == usuario_escolha:
                    print('boa! ponto pra vc')
                    pontuacao_user += 1
                else:
                    print('ahaa! ponto pra mim')
                    pontuacao_cpu += 1
                break
            except ValueError:
                print('Tente novamente. Entrada inválida')

        jogar_novamente = input('\nVoce quer jogar novamente?\n[1]Sim\n[0]Não\n')
        while jogar_novamente not in ['1', '0']:
            print('Tente novamente. Experimente com "0" ou "1" ')
            jogar_novamente = input('\nVoce quer jogar novamente?\n[1]Sim\n[0]Não\n')
        if jogar_novamente == '0':
            print('\nPontuação:')
            print(f'User: {pontuacao_user}')
            print(f'CPU: {pontuacao_cpu}')
            print('Obrigado por jogar!!!😁')
            break
    except ValueError:
        print('tente novamente')
