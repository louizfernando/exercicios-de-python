frase = 'Curso em Video'
print(frase[2:3:3])
print(frase[::3])
print(len(frase))
print(frase.count('e', 0, 12))
print(frase.find('deo'))
print(frase.find('android'))
print('curso' in frase)
print(frase.replace('video', 'android'))
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())

frase = '   Curso em Video   '
print(frase.strip())
print(frase.rstrip())
print(frase.lstrip())

frase = 'Curso em Video'
print(frase.split())
print('.'.join(frase))
print('-'.join(frase))
print('*'.join(frase))
print(' '.join(frase))
