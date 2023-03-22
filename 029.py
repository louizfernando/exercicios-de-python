vel = float(input('Em que velocidade o seu carro esta? '))
m = (vel - 80) * 7
if vel > 80:
    print('MULTADO! Você exedeu o limite de velocidade permitida!')
    print('Você recebeu uma multa no valor de R$ {:.2f} '.format(m))
else:
    print('Tenha um bom dia, dirija com segurança!')
