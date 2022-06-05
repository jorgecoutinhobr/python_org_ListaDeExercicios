a = str(input('Em qual turno você estuda? M - maturino, V - vespertino, N - noturno ')).lower()
if a == 'm':
    print('Bom dia!')
elif a == 'v':
    print('Boa tarde!')
elif a == 'n':
    print('Boa noite!')
else:
    print('Opção inválida!')
