d = int(input('Diga a distância da sua viagem: '))
if d <= 200:
    c = d * 0.50
    print('A sua viagem vai custar R$ {:.2f}'.format(c))
else:
    c = d * 0.45
    print('A sua viagem vai custar R$ {:.2f}'.format(c))
