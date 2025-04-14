import matplotlib.pyplot as plt

labels = ['Estudo', 'Trabalho', 'Lazer', 'Sono']
valores = [25, 40, 20, 15]

plt.pie(valores, labels=labels, autopct='%1.1f%%')
plt.title("Divisão de Tempo Semanal")
plt.show()