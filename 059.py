n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
escolha = 0
while escolha != 5:
    print('''
[1] somar
[2] multiplicar
[3] maior
[4] novos numeros
[5] sair do pprograma
''')
    escolha = int(input('escolha o que você vai fazer com esse valores: '))
    if escolha == 1:
        soma = n1 + n2
        print(soma)
    elif escolha == 2:
        produto = n1 * n2
        print(produto)
    elif escolha == 3:
        escolha == 5
        if n1 > n2:
            maior = n1
            print(f'{maior} é o maior numero')
        else:
            maior = n2
            print(f'{maior} é o maior numero')
    elif escolha == 4:
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    else:
        print('finalizando...')

print('FIM')