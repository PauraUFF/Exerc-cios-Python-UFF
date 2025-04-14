dados = {
    "nome": input("Digite seu nome completo: "),
    "idade": input("Digite sua idade: "),
    "pai": input("Digite o nome do seu pai: "),
    "mãe": input("Digite o nome da sua mãe: "),
    "escola": input("Digite o nome da última escola onde estudou: "),
    "mat_UFF": input("Digite sua matricula na UFF: ")
}

print("\n--- Cartão de Apresentação ---")
for chave, valor in dados.items():
    print(f"{chave.capitalize()}: {valor}")