import matplotlib.pyplot as plt

meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun']
empresa1 = [1000, 1200, 1100, 1500, 1700, 1600]
empresa2 = [900, 1000, 950, 1300, 1250, 1400]

x = range(len(meses))
plt.bar(x, empresa1, width=0.4, label='Empresa A', align='center')
plt.bar([i + 0.4 for i in x], empresa2, width=0.4, label='Empresa B', align='center')

plt.xticks([i + 0.2 for i in x], meses)
plt.title("Faturamento - 1º Semestre")
plt.legend()
plt.show()