# Annotated Plot - Gráfico de linhas anotado

import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4, 5]
y = [2, 4, 1, 3, 5]

# Create the plot
plt.plot(x, y, marker='o')

# Add annotations
plt.annotate('Maximum Value', xy=(5, 5), xytext=(4, 4.5),
             arrowprops=dict(facecolor='black', shrink=0.05),
             fontsize=10)
plt.annotate('Minimum Value', xy=(3, 1), xytext=(2, 1.5),
             arrowprops=dict(facecolor='black', shrink=0.05),
             fontsize=10)

# Add labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Annotated Plot Example')

# Show the plot
plt.grid(True)
plt.show()
