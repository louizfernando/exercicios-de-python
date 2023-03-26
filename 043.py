p = float(input('Digite o seu peso: KG '))
h = float(input('Digite a sua altura em metros: '))
imc = p / (h ** 2)
print(f'Seu imc é de {imc:.2f}', end=', ')
if imc < 18.5:
    print('\033[1;31mABAIXO DO PESO!\033[m')
elif imc >= 18.5 and imc < 25:
    print('\033[1;32mPESO IDEAL!\033[m')
elif imc >= 25 and imc < 30:
    print('\033[1;33mSOBREPESO!\033[m')
elif imc >= 30 and imc < 40:
    print('\033[1;33mOBESIDADE!\033[m')
else:
    print('\033[1;31mOBESIDADE MÓRBIDA!\033[m')
