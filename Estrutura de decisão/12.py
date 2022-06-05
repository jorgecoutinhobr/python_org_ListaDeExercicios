hora = float(input('Quantos horas você trabalhou no mês? '))
valor = float(input('Qual é o seu salário por hora? '))
bruto = round(hora * valor, 2)
if bruto <= 900:
    print('ISENTO DE IMPOSTO!')
    print(f'SALARIO LIQUIDO FINAL = {bruto} reais.')

elif bruto > 900 and bruto <= 1500:
    print('DESCONTO DE 5% DE IR.')
    ir = bruto * 0.05
    inss = bruto * 0.10
    fgts = bruto * 0.11
    desconto = ir + inss 
    liquido = round(bruto - desconto, 2)
    print(f'''
    
    Salário Bruto: ({hora} * {valor})   : R$ {bruto}
        (-) IR (5%)                     : R$   {ir}
        (-) INSS ( 10%)                 : R$  {inss}
        FGTS (11%)                      : R$  {fgts}
        Total de descontos              : R$  {desconto}
        Salário Liquido                 : R$  {liquido}
    ''')
elif bruto > 1500 and bruto <= 2500:
    print('DESCONTO DE 10% NO IR.')
    ir = bruto * 0.1
    inss = bruto * 0.10
    fgts = bruto * 0.11
    desconto = ir + inss
    liquido = round(bruto - desconto, 2)
    print(f'''
    
    Salário Bruto: ({hora} * {valor})   : R$ {bruto}
        (-) IR (10%)                     : R$   {ir}
        (-) INSS ( 10%)                 : R$  {inss}
        FGTS (11%)                      : R$  {fgts}
        Total de descontos              : R$  {desconto}
        Salário Liquido                 : R$  {liquido}
    ''')
elif bruto > 2500:
    print('DESCONTO DE 20% NO IR.')
    ir = bruto * 0.2
    inss = bruto * 0.10
    fgts = bruto * 0.11
    desconto = ir + inss
    liquido = round(bruto - desconto, 2)
    print(f'''
    
    Salário Bruto: ({hora} * {valor})   : R$ {bruto}
        (-) IR 20%)                     : R$   {ir}
        (-) INSS ( 10%)                 : R$  {inss}
        FGTS (11%)                      : R$  {fgts}
        Total de descontos              : R$  {desconto}
        Salário Liquido                 : R$  {liquido}
    ''')


