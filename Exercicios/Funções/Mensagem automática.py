from datetime import datetime

tempo = datetime.now()

hora = tempo.hour

def solicita_nome():
    nome = input('Digite seu nome: ')
    return nome

def periodo(hora):
    if hora < 5:
        periodo = 'madrugada'
    elif hora < 12:
        periodo = 'manhã'
    elif hora < 18:
        periodo = 'tarde'
    else:
        periodo = 'noite'
    return periodo

def exibir_mensagem(nome,periodo):
    print(f'Olá {nome}, boa {periodo}')

nome = solicita_nome()
periodo = periodo(hora)
exibir_mensagem(nome,periodo)