btc_brl = 320000
eth_brl = 18000

print("1 - Bitcoin (BTC)\n2 - Ethereum (ETH)")
op = input("Escolha a moeda (1 ou 2): ")
quant = float(input("Quantidade de moedas: "))

if op == "1":
    valor = quant * btc_brl
    print(f"{quant} BTC = R${valor:,.2f}")
elif op == "2":
    valor = quant * eth_brl
    print(f"{quant} ETH = R${valor:,.2f}")
else:
    print("Opção inválida.")