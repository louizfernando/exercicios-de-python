print('VAMOS VER SE UM NUMERO É PRIMO OU NÃO!')
tot = 0
n = int(input('Digite um numero: '))
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[34m', end='')
        tot += 1
print(f'O numero {n} foi divisivel {tot} vezes')
if tot <= 2:
    print(f'O numero {n} é primo.')
else:
    print(f'O numero {n} não é primo.')
