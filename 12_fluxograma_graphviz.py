# Instalar a biblioteca
pip install graphviz

from graphviz import Digraph

# Criar um gráfico
dot = Digraph()

# Iniciar um nó
dot.node('A', 'Iniciar')

# Decisão 1
dot.node('B', 'Está chovendo?', shape='diamond')

# Decisão 2
dot.node('D', 'Você tem um guarda-chuva?', shape='diamond')

# Nós de processamento
dot.node('C', 'Fique em casa')
dot.node('E', 'Leve seu guarda-chuva e saia')
dot.node('F', 'Saia sem um guarda-chuva')
dot.node('G', 'Fim')

# Conexões
dot.edge('A', 'B')
dot.edge('B', 'C', label='Não')
dot.edge('B', 'D', label='Sim')
dot.edge('D', 'E', label='Sim')
dot.edge('D', 'F', label='Não')
dot.edge('C', 'G')
dot.edge('E', 'G')
dot.edge('F', 'G')

# Crie o gráfico e gere um arquivo - fluxograma.png
dot.render('fluxograma', format='png', cleanup=True)
