soma_idade = 0
maior_idade_homem = 0
nome_velho = ''
idade_mulher = 0
for p in range(1, 3):
    print(f'--- {p}° PESSOA ---')
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: '))
    soma_idade += idade
    if p == 1 and sexo in 'Mn':
        maior_idade_homem = idade
        nome_velho = nome
    if sexo in 'Mn' and idade > maior_idade_homem:
        maior_idade_homem = idade
        nome_velho = nome
    if sexo in 'Ff' and idade < 20:
        idade_mulher += 1
print(f'A média das idade do grupo é de {soma_idade / p :.1f} anos.')
print(f'O homem mais velho tem {maior_idade_homem} e se chama {nome_velho}')
print(f'No grupo existem {idade_mulher} mulheres com menos de 20 anos')
