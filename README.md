# AlgComp – Visualização de Complexidade Algorítmica

Este repositório apresenta um experimento computacional voltado à demonstração visual e quantitativa das principais classes de complexidade de tempo estudadas em Ciência da Computação.

O projeto utiliza Python para calcular e plotar o crescimento assintótico de diferentes funções de complexidade, permitindo comparar de forma clara o impacto da escolha algorítmica no desempenho de sistemas computacionais.

---

## 🎯 Objetivo

Demonstrar, por meio de simulação matemática e visualização gráfica:

O(1) < O(log n) < O(n) < O(n log n) < O(n²) < O(2^n) < O(n!)

A implementação evidencia como funções exponenciais e fatoriais crescem drasticamente mais rápido que funções polinomiais e lineares, justificando a importância da análise de algoritmos no desenvolvimento de soluções eficientes.

---

## 📊 Complexidades Analisadas

O experimento contempla as seguintes classes:

- O(1) — constante  
- O(log n) — logarítmica  
- O(n) — linear  
- O(n log n) — linearítmica  
- O(n²) — quadrática  
- O(2^n) — exponencial  
- O(n!) — fatorial  

---

## 🧠 Fundamentação Teórica

A análise de complexidade assintótica é um dos pilares da Ciência da Computação, permitindo estimar o comportamento de algoritmos conforme o tamanho da entrada cresce.

Este projeto ilustra:

- Diferença entre crescimento polinomial e exponencial  
- Impacto da explosão combinatória  
- Importância da escolha algorítmica em problemas de larga escala  

---

## ⚙️ Tecnologias Utilizadas

- Python 3  
- Biblioteca `math`  
- Biblioteca `matplotlib`  

---

## 🚀 Como Executar

1. Clone o repositório:

```

git clone [https://github.com/vitor-souza-ime/algcomp.git](https://github.com/vitor-souza-ime/algcomp.git)
cd algcomp

```

2. Instale as dependências:

```

pip install matplotlib

```

3. Execute o script principal:

```

python nome_do_arquivo.py

```

O programa irá:

- Exibir no terminal os valores numéricos das funções
- Gerar um gráfico comparativo em escala logarítmica

---

## 📈 Visualização

O gráfico é gerado utilizando escala logarítmica no eixo Y para permitir melhor comparação entre curvas de crescimento muito distintas.

Sem a escala logarítmica, as funções exponencial e fatorial dominariam completamente o gráfico, inviabilizando a análise visual das demais.

---

## 🔍 Resultados Observados

- O(1) permanece constante
- O(log n) cresce lentamente
- O(n) e O(n log n) apresentam crescimento moderado
- O(n²) cresce rapidamente
- O(2^n) e principalmente O(n!) apresentam crescimento explosivo

Para n = 20, por exemplo, O(n!) ultrapassa 2,4 × 10¹⁸, ilustrando o fenômeno da explosão combinatória.

---

## 📚 Aplicações Didáticas

Este projeto é indicado para:

- Disciplinas de Estruturas de Dados
- Análise e Projeto de Algoritmos
- Complexidade Computacional
- Introdução à Ciência da Computação

Pode ser utilizado como material complementar para visualização intuitiva do conceito de ordem de crescimento.

---

## 🔮 Trabalhos Futuros

Possíveis extensões incluem:

- Análise de complexidade de espaço
- Medição empírica de tempo real de execução
- Inclusão de O(n³) e O(n^k)
- Comparação entre algoritmos reais

---

## 👨‍💻 Autor

Vitor Souza  

---

## 📌 Conclusão

A escolha do algoritmo é decisiva para a viabilidade prática de um sistema computacional.

Este repositório demonstra de forma clara e visual como diferentes classes de complexidade impactam drasticamente o crescimento do custo computacional, reforçando a importância da análise algorítmica no desenvolvimento de software eficiente.
