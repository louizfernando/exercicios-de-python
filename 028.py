import random2
print('Vou pensar em um numero entre 0 e 5.')
num = random2.randint(0, 5)
n = int(input('Tente adivinhar: '))
if num == n:
    print('PARABÉNS,VOCÊ ACERTOU!')
else:
    print('VOCÊ ERROU!')
    print('Eu pensei no numero {}'.format(num))
