a = float(input('Digite o seu salário: '))
if a <= 280:
    x = a * 1.2
    y = a *0.2
    print(f'''
    ANTIGO SALÁRIO - {a} reais
    AUMENTO DE 20%
    VALOR DE AUEMNTO - {y} reais.
    NOVO SALÁRIO - {x:.2f} reais.
    ''')
elif a > 280 and a <= 700:
    x = a * 1.15
    y = a *0.15
    print(f'''
    ANTIGO SALÁRIO - {a} reais
    AUMENTO DE 15%
    VALOR DE AUEMNTO - {y} reais.
    NOVO SALÁRIO - {x:.2f} reais.
    ''')

elif a > 700 and a <= 1500:
    x = a * 1.1
    y = a *0.1
    print(f'''
    ANTIGO SALÁRIO - {a} reais
    AUMENTO DE 20%
    VALOR DE AUEMNTO - {y} reais.
    NOVO SALÁRIO - {x:.2f} reais.
    ''')

elif a > 1500:
    x = a * 1.05
    y = a *0.05
    print(f'''
    ANTIGO SALÁRIO - {a} reais
    AUMENTO DE 5%
    VALOR DE AUEMNTO - {y} reais.
    NOVO SALÁRIO - {x:.2f} reais.
    ''')