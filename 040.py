a = float(input('1° média do aluno: '))
b = float(input('2° média do aluno: '))
if (a + b) / 2 >= 7:
    print('\033[;32mAPROVADO\033[m')
elif (a + b) / 2 < 5:
    print('\033[;31mREPROVADO\033[m')
else:
    print('\033[;33mRECUPERAÇÂO\033[m')