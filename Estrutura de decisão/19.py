n = str(input('Digite um numero menor que 1000: '))

if len(n) == 3:
    c = n[0]
    d = n[1]
    e = n[2]
    print(f'''
    {c} centenas
    {d} dezenas
    {e} unidades
    ''')
elif len(n)==2:
    d = n[0]
    e = n[1]
    print(f'''
    0 centenas
    {d} dezenas
    {e} unidades
    ''')
elif len(n)==1:
    e = n[0]
    print(f'''
    0 centenas
    0 dezenas
    {e} unidades
    ''')