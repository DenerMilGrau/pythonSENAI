def menu():
    print('[0]Sair\n[1]Farenheit\n[2]Kelvin\n[3]Ambos')
    opcao = input('>>')
    while opcao not in ['1', '2', '3', '0']:
        print('Tente novamente com números de 0 a 3')
        opcao = input('>>')
    return opcao


def entrada_celsius():
    while True:
        try:
            celsius = float(input('Informe a temperatura (°C): '))
            return celsius
        except ValueError:
            print('Entrada invalida')


def conversao_kelvin(celsius):
    kelvin = celsius + 273.15
    return kelvin


def conversao_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit


def exibir_mensagem(celsius, conversao_fahrenheit, conversao_kelvin, opcao):
    if opcao == opcao_farenheit:
        fahrenheit = conversao_fahrenheit(celsius)
        print(f'{celsius} °C são {fahrenheit} °F')
    elif opcao == opcao_kelvin:
        kelvin = conversao_kelvin(celsius)
        print(f'{celsius} °C são {kelvin} K')
    elif opcao == opcao_ambos:
        fahrenheit = conversao_fahrenheit(celsius)
        kelvin = conversao_kelvin(celsius)
        print(f'{celsius} °C são {fahrenheit} °F e {kelvin}K')


sair = '0'
opcao_farenheit = '1'
opcao_kelvin = '2'
opcao_ambos = '3'

while True:
    opcao = menu()
    if opcao == sair:
        print('Saindo do programa...')
        break
    celsius = entrada_celsius()
    exibir_mensagem(celsius, conversao_fahrenheit, conversao_kelvin, opcao)