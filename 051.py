p = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite uma razão para essa PA; '))
t = p +  (10 - 1) * r
for c in range(p, t + r, r):
    print(f'{c}', end=' - ')
print('FIM')
