from datetime import datetime
ano = int(input('Em que ano você nasceu? '))
#datetime serve pra trabalharmos com datas dentro do python
#.now() nos podemos saber a data atual com base no nosso computador
atual = datetime.now()
if atual.year - ano < 18:
    print('Ainda não chegou a hora de você se alistar.')
    print(f'Faltam {18 - (atual.year - ano)} anos para você poder se alistar.')
elif atual.year - ano == 18:
    print('Está na hora de você se alistar.')
else:
    print('Já passou a hora de você se alistar.')
    print(f'Já passaram-se {(atual.year - ano) - 18} anos do tempo de você se alistar.')