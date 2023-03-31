from random2 import randint
escolha = ''
print('Eu vou pensar em um numero entre 1 e 10, tente adivinhar')
computador = randint(1, 10)
jogador = int(input('Digite um numero entre 1 e 10: '))
while computador == jogador:
    if computador != jogador:
        escolha = str(input('Você \033[31merrou\033[m, quer tentar novamente? [S/N] ')).strip().upper()[0]
        if escolha in 'S':
            computador = randint(1, 10)
            jogador = int(input('Digite um numero entre 1 e 10: '))
        else:
            print(end='')
    if computador == jogador:
        escolha = str(input('Você \033[32macertou\033[m, quer tentar novamente? [S/N] ')).strip().upper()[0]
        if escolha in 'S':
            computador = randint(1, 10)
            jogador = int(input('Digite um numero entre 1 e 10: '))
        else:
             print(end='')
while computador != jogador:
    if computador != jogador:
        escolha = str(input('Você errou quer tentar novamente? [S/N] ')).strip().upper()[0]
        computador = randint(1, 10)
        if escolha == 'S':
            jogador = int(input('Digite um numero entre 1 e 10: '))
            if computador == jogador:
                escolha = str(input('Você \033[32macertou\033[m, quer tentar novamente? [S/N] ')).strip().upper()[0] 
            else:
                print(end='')        
        else:
            computador = jogador
        if escolha == 'N':
            computador = jogador
print('Obrigado por jogar')
