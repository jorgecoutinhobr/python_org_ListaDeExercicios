while True:
  nota = float(input('Digite uma nota entra 0 e 10: '))
  if nota == 999:
    print("fim")
    break
  while nota < 0 and nota > 10:
    nota = float(input('Digite uma nota entra 0 e 10: '))
  if nota >= 0 and nota <=10:
    print(f'Nota válida {nota}.')