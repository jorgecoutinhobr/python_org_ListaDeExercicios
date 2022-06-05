n = str(input('Digite seu nome: ')).strip()
s = str(input('Digite sua senha: ')).strip()
while n == s:
    print('Digite uma senha diferente do seu nome!!')
    n = str(input('Digite seu nome: ')).strip()
    s = str(input('Digite sua senha: ')).strip()
else:
    print('Cadastro finalizado.')