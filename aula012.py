nome = str(input('Qual é o seu nome? ')).lower()
if nome == 'louiz':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'João' or nome == 'Maria':
    print('Seu nome é muito popular!')
else:
    print('Seu nome é bem normal.')
print(f'Tenha um bom dia, {nome}!')
