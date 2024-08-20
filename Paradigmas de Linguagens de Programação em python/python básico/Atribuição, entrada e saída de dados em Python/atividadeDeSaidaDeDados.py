preco_arroz = 10.00
preco_feijao = 8.50
preco_macarrao = 5.25

quantidade_arroz = int(input("Quantos sacos de arroz você deseja? "))
quantidade_feijao = int(input("Quantos sacos de feijão você deseja? "))
quantidade_macarrao = int(input("Quantos sacos de macarrão você deseja? "))

preco_total = (preco_arroz * quantidade_arroz) + (preco_feijao * quantidade_feijao) + (preco_macarrao * quantidade_macarrao)

print("O preço total do seu pedido é: R$", preco_total)