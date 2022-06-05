a = float(input('Digite sua primeira nota: '))
b = float(input('Digite sua segundaa nota: '))
c = float(input('Digite sua terceira nota: '))
media = round((a + b+ c)/3, 2)
if media >= 7 and media < 10:
    print(f'Sua média foi de {media} e você doi aprovado.')
elif media ==10:
    print(f'Sua média doi de {media}, você foi aprovado com distinção.')
elif media <7:
    print(f'Sua media foi de {media}, logo você foi a reprovado.')
    
