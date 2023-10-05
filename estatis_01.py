
# Exemplo de cálculo da média em Python
dados = [10, 15, 20, 25, 30]
media = sum(dados) / len(dados)
print("Média:", media)


#Parte 2: Visualização de Dados

import matplotlib.pyplot as plt

# Exemplo de histograma
dados = [10, 15, 20, 25, 30, 30, 35, 40]
plt.hist(dados, bins=5)
plt.xlabel("Valores")
plt.ylabel("Frequência")
plt.title("Histograma")
plt.show()


#Parte 3: Correlação e Regressão

import numpy as np

# Exemplo de correlação
x = [1, 2, 3, 4, 5]
y = [2, 3, 4, 5, 6]
correlacao = np.corrcoef(x, y)[0, 1]
print("Correlação:", correlacao)
