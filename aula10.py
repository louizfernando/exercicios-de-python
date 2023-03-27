temp = float(input('Quantos anos o seu carro tem? '))
if temp <= 3:
    print('carro novo')
else:
    print('carro velho da porra')
print('--FIM--')

#ou#

temp = float(input('Quantos anos o seu carro tem? '))
print('carro novo'if temp <= 3 else 'carro velho')
print('--FIM--')
