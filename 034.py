s = float(input('Diga o valor do seu salário: R$ '))
print('PARABÉNS VOCÊ GANHOU UM AUMENTO!')
#if é a mesma coisa que "se"
if s >= 1250.00:
    sa = s * 1.10
    print('O valor so seu salário será de R$ {:.2f}'.format(sa))
#else é a mesma coisa que "senão"
else:
    sa = s * 1.15
    print('O valor do seu salário será de R$ {:.2f}'.format(sa))
