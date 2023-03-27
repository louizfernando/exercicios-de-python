soma = 0
#LAÇO DE REPETIÇÃO FOR 
for c in range(0, 6):
    n = int(input('Digite um numero: '))
    if n % 2 == 0:
        soma = soma + n
print(f'A soma dos numeros pares é {soma}')