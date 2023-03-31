sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Sexo M/F: ')).strip().upper()[0]
if sexo == 'M':
    sexo = 'masculino'
else:
    sexo = 'feminino'
print(f'Sexo {sexo} cadastrado com sucesso.')
