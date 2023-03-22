v = float(input('Qula o valor do produto? R$'))
print('Se o produto for pago a vista terá um desconto e vai ustar R${:.2f}'.format(v * 0.95))
print('Se for pago a prazo terá um aumento e vai custar R${:.2f}'.format(v * 1.08))