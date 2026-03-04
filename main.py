import math
import matplotlib.pyplot as plt

# Valores de n (limitado por causa do crescimento do fatorial)
n_values = list(range(1, 21))

# Cálculo das complexidades
O_1 = [1 for n in n_values]
O_log_n = [math.log2(n) for n in n_values]
O_n = [n for n in n_values]
O_n_log_n = [n * math.log2(n) for n in n_values]
O_n2 = [n**2 for n in n_values]
O_2n = [2**n for n in n_values]
O_fact = [math.factorial(n) for n in n_values]

# Criando o gráfico único
plt.figure(figsize=(10, 6))

plt.plot(n_values, O_1, label="O(1)")
plt.plot(n_values, O_log_n, label="O(log n)")
plt.plot(n_values, O_n, label="O(n)")
plt.plot(n_values, O_n_log_n, label="O(n log n)")
plt.plot(n_values, O_n2, label="O(n²)")
plt.plot(n_values, O_2n, label="O(2^n)")
plt.plot(n_values, O_fact, label="O(n!)")

# Escala log para melhor visualização
plt.yscale("log")

plt.title("Comparação de Complexidades de Algoritmos")
plt.xlabel("n")
plt.ylabel("Crescimento (escala log)")
plt.legend()
plt.grid(True)

plt.show()
