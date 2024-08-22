# Adicionando um valor na lista
tupla_heterogenea = (1, 'Olá', 3.14, [10, 20, 30], {'chaves': 'valor'})

tupla_heterogenea[3].append(40)
print(f"Lista modificada: {tupla_heterogenea[3]}")