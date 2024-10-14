dicionario = {
    'nome': 'Alice',
    'idade': 25,
    'cidade': 'São paulo',
    'profissão': 'Engenheira',
}

print('iterando sobre o dicionário:')
for chaves, valores in dicionario.items():
    print(f'{chaves}: {valores}')
      