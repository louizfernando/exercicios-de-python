from time import sleep #biblioteca para fazer pausas
from emoji import emojize #biblioteca de emojis
print('\033[31mESCOLHA UMAS DAS OPÇÕES ABAIXO:\033[m')
#PAUSA POR SEGUNDOS
sleep(1)
print('''
[0] EXPLPODIR A BOMBA
[1] NÃO EXPLODIR A BOMBA
''')
e = int(input('Escolha uma opção: '))
#WHILE PARA REPETIR CASO A RESPOSTA SEJA INADEQUADA 
while e != 0 and e != 1:
    print('VOCÊ NÃO ESCOLHERU NENHUMA DAS OPÇÕES')
    e = int(input('Escolha uma opção: '))
if e == 0:
    e = str(input(emojize('Tem certeza:face_with_raised_eyebrow::face_with_raised_eyebrow:?? '))).upper()
#SE 'SIM' NÃO ESTIVER NA VARIÁVEL 'e'
    if 'SIM' not in e:
        print('Mudou de ideia né kakak')
        print(emojize('tmj, parceiro :call_me_hand:'))
#SE TIVER 'SIM' NA VARIAVEL 'e'
    elif 'SIM' in e:
        if 'SIM' in e:
            sleep(1)
            print(emojize('Então ta bom:face_with_rolling_eyes:'))
            sleep(1)
            print(emojize('A bomba explodirá em...'))
            for c in range(3, 0, -1 ): #FOR PARA TER UM LAÇO DE REPPETIÇÃO
                sleep(1)
                print(c)
                sleep(1)
            print(emojize('\033[31mBOOOOOOOOOM\033[m :collision::collision::collision::collision:'))
            sleep(1)
            print(emojize('TU MORREU!! KKAK :rolling_on_the_floor_laughing: MT BURRO NMRL:rolling_on_the_floor_laughing:'))
if e == 1:
    print(emojize('tmj, parceiro :call_me_hand:'))