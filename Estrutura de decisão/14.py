a = float(input('Digite a primeira nota: '))
b = float(input('Digite a segunda nota: '))
media = round((a + b)/2, 2)
if media >= 9 and media <= 10:
    print(f'As notas foram {a} e {b}, a media foi de {media} e o conceito foi A - APROVADO')
elif media >= 7.5 and media < 9:
    print(f'As notas foram {a} e {b}, a media foi de {media} e o conceito foi B - APROVADO')
elif media >= 6 and media < 7.5:
    print(f'As notas foram {a} e {b}, a media foi de {media} e o conceito foi C - APROVADO')
elif media >= 4 and media < 6:
    print(f'As notas foram {a} e {b}, a media foi de {media} e o conceito foi D - REPROVADO')
elif media >= 0 and media <4:
    print(f'As notas foram {a} e {b}, a media foi de {media} e o conceito foi E - REPROVADO')
