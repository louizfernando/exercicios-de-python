from math import radians, sin, cos
ang = int(input('Digite um angulo: '))
seno = sin(radians(ang))
coss = cos(radians(ang))
print('O cosseno de e a seno de {} são respectivamento {:.2f}, {:.2f}'.format(ang, seno, coss))
