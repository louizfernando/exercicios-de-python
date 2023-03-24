c = float(input('Qual o valor da casa desejada? R$ '))
s = float(input('Quanto você receber por mês? R$ '))
t = int(input('Em quantos anos você vai pagar? '))
p = c / (t * 12)
if p > s * 0.30:
    print('\033[1;31mSEU EMPRESTIMO FOI NEGADO.\033[m')
    print('\033[1;31mO valor da sua parcela excedeu 30% do seu salário.\033[m')
#elif é a mesma coisa que 'SENÃO SE" é a junção dessas duas palavras.
elif p < s * 0.30:
    print('\033[1;32mPARABÉNS! O SEU EMPRESTIMO FOI APROVADO!\033[1;32m')
    print(f'\033[1;32mSerão {t * 12} parelas no valor de R$ \033[4;32m{p:.2f}\033[m')
