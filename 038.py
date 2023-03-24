a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
if a > b:
    print('O primeiro valor é maior.')
elif b > a:
    print('O segundo valor é maior.')
else:
    print('\033[7;40mNão existe valor maior, os dois são iguais!\033[m')