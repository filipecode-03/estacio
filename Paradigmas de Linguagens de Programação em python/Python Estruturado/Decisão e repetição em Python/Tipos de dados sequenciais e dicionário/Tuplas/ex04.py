# imprimindo os tipos de cada elemento da tupla

tupla_heterogenea = (1, 'Olá', 3.14, [10, 20, 30], {'chaves': 'valor'})

for elemento in tupla_heterogenea:
    print(f'Elemento: {elemento}, tipo: {type(elemento)}')