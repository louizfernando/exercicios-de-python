media = 0
maior_idade_h = 0
menos_de_vinte = 0
nome_velho = ''
plural_m = ''
for c in range(1, 4):
    print(F'----- {c}ª PESSOA -----')
    nome  = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo M/F: ')).upper()
    media += idade
    if c == 1 and sexo in 'M':
        maior_idade_h = idade
        nome_velho = nome
    if sexo in 'M' and idade > maior_idade_h:
        maior_idade_h = idade
        nome_velho = nome
    if idade < 20 and sexo in 'F':
        menos_de_vinte += 1
        if menos_de_vinte > 1:
            plural_m = 'es'
        else:
            plural_m = ''
print(f'{nome_velho} tem {maior_idade_h} anos, ele é o homem mais velho do grupo.')
print(f'{menos_de_vinte} mulher{plural_m} tem menos de vinte anos.')
