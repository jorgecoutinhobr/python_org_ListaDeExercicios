tamanho = float(input('Digite o tamanho do arquivo que você deseja baixar MB: '))
vel = float(input('Digite a velocidade da sua internet em MMps: '))
segundos = tamanho / vel 
minutos = segundos / 60
print(f'O download vai demorar {minutos:.2f} minutos.')
