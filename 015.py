t = float(input('Por quantos dias o carro foi alugado? '))
km = float(input('Qunatos quilômetros você andou com o carro? '))
print('Total a pagar é de R${:.2f}'.format((t * 60) + (km * 0.15)))
print('Você andou {:.2f}km por dia com o carro.'.format(km / t))

