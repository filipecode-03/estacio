escolha = input("Escolha uma opção de função 1 ou 2: ")

if escolha == '1':
    def func1(x):
        return x + 1
    x = func1(10)
    print(x)
else:
    def func2(x):
        return x + 2
    x = func2(10)
    print(x)
