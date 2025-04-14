import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(f"C:/Users/User/Downloads/exercicios_python_uff_completos/data.csv")
print(df.head())

contagem = df['Cidade'].value_counts()
contagem.plot(kind='bar')
plt.title("Quantidade de Alunos por Cidade")
plt.xlabel("Cidade")
plt.ylabel("Quantidade")
plt.show()