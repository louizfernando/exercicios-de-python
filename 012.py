l = float(input('Largura da parede: '))
h = float(input('Altura da parede: '))
print('A sua parede tem a dimensão de {}x{} e sua área é de {}m²'.format(l, h, l * h))
print('Para pintar a sua parede são necessários {:.3f}l'.format((l * h) / 2))
