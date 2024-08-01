def entrada(dados, unidade):
    while True:
        try:
            valor = float(input(f'{dados} ({unidade}): '))
            if valor < 0:
                raise ValueError
            break
        except ValueError:
            print('Entrada invalida. Tente novamente.')
    return valor


def calculo_imc(peso, altura):
    imc = peso / (altura*altura)
    return imc


def classificador(imc):
    if imc < 18.5:
        return 'Abaixo do peso'
    elif imc >= 18.5 and imc < 25:
        return 'Peso ideal'
    elif imc >= 25 and imc < 30:
        return 'Sobrepeso'
    elif imc >= 30 and imc < 40:
        return 'Obesidade'
    elif imc >= 40:
        return 'Obesidade extrema'


def exibir_mensagem(imc, classificacao):
    print(f'Seu IMC é igual a {imc}, é considerado {classificacao}')


altura = entrada('Altura', 'm')
peso = entrada("Peso", "kg")
imc = calculo_imc(peso, altura)
classificacao = classificador(imc)
exibir_mensagem(imc, classificacao)
