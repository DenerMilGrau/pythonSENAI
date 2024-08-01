def entrada_valores():
    while True:
        try:
            valor = float(input('Digite um valor: '))
            if valor <= 0:
                raise ValueError
            break
        except ValueError:
            print('adicione um valor válido')
    return valor


def entrada_produto():
    produto = input('Digite o nome do produto: ')
    return produto


def entrada_codigo_produto():
    while True:
        codigo = input('Digite o codigo do produto: ')
        if codigo.isnumeric():
            if len(codigo) == 6:
                break
            elif len(codigo) != 6:
                print('tente novamente. O código deve ter 6 dígitos')
        else:
            print('Tente novamente. O código deve ser numerico')

    codigo_formatado = '{}.{}-{}' .format(codigo[:3], codigo[3:5], codigo[5:])
    return codigo_formatado

produtos = list()
valores = list()
codigos = list()
c = 0
print('Efetuar cadastro')
while c < 2:
    print('Cadastrando novo produto...\n')
    produto = entrada_produto()
    valor = entrada_valores()
    codigo_produto = entrada_codigo_produto()
    while codigo_produto in codigos:
        print('OPA! parece que um produto com esse código já foi cadastrado')
        codigo_produto = entrada_codigo_produto()

    print('\nOK! Produto cadastrado com sucesso')
    produtos.append(produto)
    valores.append(valor)
    codigos.append(codigo_produto)
    #opcao = input('\nDeseja continuar? [S/N] ')
    #if opcao == 'n':
        #break
    #while opcao not in ['s', 'n', 'S', 'N']:
        #print('\nopcao invalida. Tente novamente')
        #opcao = input('\nDeseja continuar? [S/N] ')
    c += 1

#combina as duas listas em uma lista de tuplas
produtos_valores_codigo = list(zip(produtos, valores, codigos))
#ordena a lista de tuplas com base na lista de valores
produtos_valores_codigo.sort(key=lambda x: x[1], reverse=True)
print(produtos_valores_codigo)
for posic, prod_valor_cod in enumerate(produtos_valores_codigo):
    print(f'Na posição {posic} achei o produto {prod_valor_cod[0]} custando {prod_valor_cod[1]}. Código: {prod_valor_cod[2]}')
#a posição se refere ao índice (que é igual dos produtos e seus respectivos valores), quando ele chama o índice 0, ele chama uma tupla com o produto e o valor Ex.: ('p1', 2)
#Por esse motivo para se referir ao produto pego o índice 0 da tupla e o valor ao índice 1, **quando ele troca de posição na lista ele tambem troca de tupla


# ao usar for x in range/lista, o x assume o valor dessa variável composta, por exemplo, ele assume o valor do que está no índice zero (independente do tipo de dado)
# ou seja, "para cada item na lista produtos ordenados" e o "x" passa a ser um item da lista



#Aqui teste 2 métodos diferentes pra printar os valores e nomes do produto, primeiro utilizando for e a lista de tuplas, ele "chama" o primeiro índice (uma tupla), com as 2 variáveis (x e y) ele seleciona produto (str) e o valor (float)
# sinceramente nem eu sei como funcionou testei só pra aprender a usar o laço for melhor

for x, y, z in produtos_valores_codigo:
    print(f'produto: {x}, valor: {y}. Código: {z}')
    print('')


#separa as listas novamente
produtos_ordenados, valores_ordenados, codigos_ordenados = zip(*produtos_valores_codigo)

produtos_ordenados = list(produtos_ordenados)
valores_ordenados = list(valores_ordenados)


# O segundo método é com while, ele precisa que as listas sejam separadas novamente, ele conta a quantidade de índices da lista de produtos (q é igual a de valores) usando a função(método talvez?) len
#ele precisa de um contador (x) que vai fazer ele printar o item com o índice correto
#esse foi o primeiro que eu fiz, antes do guanabara e stackoverflow me ajudarem

x = 0

qntd_produtos = len(produtos)

#while x < qntd_produtos:
    #print(produtos_ordenados[x],'=>', valores_ordenados[x])
    #x += 1










