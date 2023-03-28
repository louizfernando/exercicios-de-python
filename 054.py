from datetime import datetime
data = datetime.now()
tmaior = 0
tmenor = 0
print(data.year)
for pes in range(1, 8):
    nasc = int(input(f'Em que ano a {pes}° pessoa nasceu? '))
    ida = data.year - nasc
    if ida >= 18:
        tmaior += 1
    else:
        tmenor += 1
print(f'{tmenor} pessoas são menor de idade.')
print(f'{tmaior} pessoas são maior de idade.')