
import matplotlib.pyplot as plt

categorias = ["Python", "Java", "JavaScript", "HTMLS", "CSS"]
quantidade = [80, 65, 40, 69, 71]

plt.bar(categorias,quantidade)

plt.title("Linguagens mais usadas")
plt.xlabel("Linguagem")
plt.ylabel("Quantidade")

plt.show()
