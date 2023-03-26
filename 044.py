p = float(input('Qual o preço do produto? '))
print('''
[1] A VISTA COM 10% DE DESCONTO (dinheiro/cheque) 
[2] A VISTA COM 5% DE DESCONTO (cartão)
[3] 2x NO CARTÃO
[4] 3X NO CARTÃO COM ACRÉSCIMO DE 20%''')
fp = float(input('Escolha alguma das formas de pagamento acima: '))
fdp = 1, 2, 3, 4
if fdp == 1:
    print(f'O valor da sua compra é de R$ {p * 0.90:.2f}, você ganhou um desconto de 10%')
elif fdp == 2:
    print(f'O valor da sua compra é de R$ {p * 0.95:.2f}')
elif fdp == 3:
    print(f'O valor da sua compra é de R$ {p:.2f}')
else:
    print(f'O valor da sua compra é de R$ {p * 1.20:.2f}')
