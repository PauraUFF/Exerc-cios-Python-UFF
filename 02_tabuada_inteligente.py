try:
    numero = int(input("Digite um número entre 1 e 10: "))
    if 1 <= numero <= 10:
        print(f"\nTabuada do {numero}")
        for i in range(1, 11):
            print(f"{numero} x {i} = {numero * i}")
    else:
        print("Número fora do intervalo permitido.")
except ValueError:
    print("Entrada inválida. Por favor, digite um número inteiro.")