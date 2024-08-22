for num in range (1000, 10000):
    menor = num % 100
    maior = num // 100
    raiz = menor + maior

    if (raiz * raiz) == num:
        print(num)
        print(menor)
        print(menor)
        print(raiz)
print('terminou')
print('saiu ', num)