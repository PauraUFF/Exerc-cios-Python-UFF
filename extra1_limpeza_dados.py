import pandas as pd

data = {
    "Nome": ["Ana", "Lucas", "João", "Carla", None, "Lucas"],
    "Idade": [20, 22, 21, 23, 20, 22],
    "Cidade": ["Niterói", "Rio", "Niterói", "São Gonçalo", "Rio", "Rio"]
}

df = pd.DataFrame(data)

print("Dados originais:")
print(df)

df_limpo = df.dropna()
df_limpo = df_limpo.drop_duplicates()

print("\nDados após limpeza:")
print(df_limpo)