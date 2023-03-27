n = int(input('Digite um numero para ver a sua tabuada: '))
mult = 0
for c in range(1, 11):
    mult = mult + 1
    r = n * mult
    print(f' {n} x {mult} = {r} ')
