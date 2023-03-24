idade = int(input('Idade do atleta: '))
if idade <= 9:
    categoria = 'MIRIM'
elif 9 < idade <= 14:
    categoria = 'INFANTIL'
elif 14 < idade <= 19:
    categoria = 'JÚNIOR'
elif idade == 20:
    categoria = 'SÊNIOR'
else:
    categoria = 'MASTER'
print(str(f'CATEGORIA: {categoria}'))
