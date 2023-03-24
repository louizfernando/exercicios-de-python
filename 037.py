num = int(input('Digite um numero inteiro: '))
print('''
Escolha uma das bases para conversão 
[1] converter para BINÁRIO
[2] converter para OCTAL
[3] converter para HEXADECIMAL''')
opções = 1, 2, 3
opção = int(input('Sua opção: '))
#SISTEMA DE REPETIÇÃO WHILE
while opção != 1 and opção != 2 and opção != 3:
    print('Você não escolheu nenhuma das opções.')
    opção = int(input('tente novamente: '))
if opção == 1:
    print(f'{num} convertido para BINÁRIO é igual a \033[1;32m{bin(num)}\033[m')
elif opção == 2:
    print(f'{num} convertido para OCTAL é igual a \033[1;32m{oct(num)}\033[m')
elif opção == 3:
    print(f'{num} convertido para HEXADECIMAL é igual a \033[1;32m{hex(num)}\033[m')
