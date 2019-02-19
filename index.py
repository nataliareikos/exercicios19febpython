from datetime import datetime, timedelta

pessoa = {
    # 'ano ': '',
    # 'mes ': '',
    'dia ': ''
}

for chave in pessoa:
    pessoa[str(chave)] = int(input('digite o '  +str(chave)))
    print(f'{chave}: {pessoa[chave]}')
    print(pessoa)

data_nascimento = timedelta(days=pessoa['dia '])

data_hoje = datetime.now()
delta_data_hoje = timedelta(days=data_hoje.day)

diferenca_de_dias = data_nascimento - delta_data_hoje
print(diferenca_de_dias)