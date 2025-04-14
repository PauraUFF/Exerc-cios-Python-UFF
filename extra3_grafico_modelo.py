import matplotlib.pyplot as plt

categorias = ['Python', 'Java', 'C++', 'JavaScript']
alunos = [35, 25, 15, 40]

plt.bar(categorias, alunos)
plt.title("Linguagens favoritas da turma")
plt.xlabel("Linguagem")
plt.ylabel("Quantidade de alunos")
plt.show()