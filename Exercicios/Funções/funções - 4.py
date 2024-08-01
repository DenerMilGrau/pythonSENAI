def entrada_lados(n):
    while True:
        try:
            lado = float(input(f'Digite o lado {n}: '))
            break
        except ValueError:
            print('Entrada inválida. Tente novamente.')
    return lado


def classificacao_triangulo(lado_1, lado_2, lado_3):
    if lado_1 == lado_2 and lado_2 == lado_3:
        return 'equilátero'
    elif lado_1 != lado_2 and lado_1 != lado_3 and lado_2 != lado_3:
        return 'escaleno'
    else:
        return 'isóceles'


def exibir_mensagem(class_triangulo):
    print(f'O triângulo é {class_triangulo}')


lado_1 = entrada_lados('1')
lado_2 = entrada_lados('2')
lado_3 = entrada_lados('3')
class_triangulo = classificacao_triangulo(lado_1, lado_2, lado_3)
exibir_mensagem(class_triangulo)