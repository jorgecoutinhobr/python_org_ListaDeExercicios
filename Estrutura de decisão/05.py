nota1 =float(input('Digite sua primeira nota: '))
nota2 =float(input('Digite sua segunda nota: '))
media = (nota1 + nota2)/2
if media >= 7 and media < 10:
    print('APROVADO!')
elif media == 10:
    print('APROVADO COM DISTINÇÃO')
else:
    print('REPROVADO')