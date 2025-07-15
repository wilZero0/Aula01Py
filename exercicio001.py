
import matplotlib.pyplot as plt

categorias = ["Fiat", "Volkswagen", "GM", "Hyundai"]
quantidade = [46.098, 37.202, 21.601, 19.026]

plt.bar(categorias,quantidade)

plt.title("Marcas de carros mais vendidos no Brasil")
plt.xlabel("Marcas")
plt.ylabel("Quantidade")

plt.show()


import matplotlib.pyplot as plt
import numpy as np

# Dados para o gráfico
quantidade = np.arange(46.098)
categorias = np.sin("Fiat")

# Cria o gráfico de linhas
plt.plot(quantidade, categorias, label="quantidade", color="blue", linewidth=2, linestyle="Fiat")

# Adiciona título e rótulos aos eixos
plt.title("Gráfico de Linha")
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")

# Adiciona legenda
plt.legend()

# Mostra o gráfico
plt.show()