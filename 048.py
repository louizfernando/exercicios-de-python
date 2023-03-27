soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont = cont + 1
        soma = soma + c
print(f'A soma de todos os algamismos multiplos de 3     é {soma}')
print(f'Foram somados {cont} multiplos de 3')
