hora = float(input('Quanto você ganha por hora? '))
mes = float(input('Quantos dias você trabalha por mês? '))
bruto = hora * mes
ir = (bruto * 0.11)
inss = (bruto * 0.08)
sind = (bruto * 0.05)
liquido = bruto - ir - inss - sind
print('+ Salário Bruto : R${}.'.format(bruto))
print('- IR (11%) : R${}.'.format(ir))
print('- INSS (8%) : R${}.'.format(inss))
print('- Sindicato ( 5%) : R${}.'.format(sind))
print('= Salário Liquido : R${}.'.format(liquido))