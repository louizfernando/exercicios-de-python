from emoji import emojize

print('Vamos ver ser você consegue formar um trangulo!')
a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))
if a + b > c:
    print(emojize(':smiling_face_with_sunglasses: PARABÉNS! VOCÊ CONSEGUIU FORMAR UM TRIÂNGULO. :smiling_face_with_sunglasses:'))
else:
    print(emojize(':man_facepalming::crying_face: NÃO FOI DESSA VEZ :crying_face::man_facepalming:'))
