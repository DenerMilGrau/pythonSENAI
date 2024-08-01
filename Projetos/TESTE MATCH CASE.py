string = 'Hello World'
teste = input('abc')
while teste != '0':

    match teste:
        case 'a':
            print('vc digitou a')
        case 'b':
            print('vc digitou b')
        case 'c':
            print('vc digitou c')
        case _:
            print('digitou outra letra')
    teste = input('abc')

print(string)
