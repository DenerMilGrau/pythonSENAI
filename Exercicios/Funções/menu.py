from datetime import datetime


def menu_calculadora():
    print("\nMenu principal")
    print('1- Adição')
    print('2- Subtração')
    print('3- Multiplicação')
    print('4- Divisão')

def ola_nome(nome):
    print(f'Ola {nome}')

def calculo_idade(ano_nascimento):
    ano_atual = datetime.now().year
    idade = ano_atual - ano_nascimento
    return idade
def exibir_idade(idade):
    print(f'A sua idade é {calculo_idade(ano_nascimento)} anos')

def solicita_ano_nasc():
    while True:
        try:
            ano_nascimento = int(input('Digite o ano de nascimento: '))
            if ano_nascimento > datetime.now().year:
                print("digite um ano válido")
            else:
                return ano_nascimento
        except ValueError:
            print('Erro no valor')

ano_nascimento = solicita_ano_nasc()
exibir_idade(calculo_idade(ano_nascimento))



#ola_nome('negraum')
#menu_calculadora()

#menu_calculadora()