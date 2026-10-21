---
aliases:
  - Gini
  - Gini Impurity
  - Impureza de Gini
tags:
  - metricas
  - arvores-de-decisao
  - machine-learning
---

# Índice Gini (Impureza de Gini)

O **Índice Gini** — ou Impureza de Gini (*Gini Impurity*) — é uma métrica matemática utilizada para mensurar o grau de heterogeneidade ou impureza da distribuição de classes em um conjunto de observações. No contexto do [[Aprendizado de Máquina]], o Índice Gini é o critério padrão adotado pelo algoritmo **CART** (*Classification and Regression Trees*) para determinar as melhores divisões em [[Árvores de Decisão]].

---

## 1. Formulação Matemática

Seja $c$ o número total de classes da variável dependente categórica e $p_i(t)$ a proporção relativa de observações pertencentes à classe $i$ no nó $t$:

$$\text{Gini}(t) = 1 - \sum_{i=1}^{c} [p_i(t)]^2$$

Onde $\sum_{i=1}^{c} p_i(t) = 1$.

### Interpretação Probabilística
O Índice Gini calcula a probabilidade de um elemento selecionado aleatoriamente do nó ser classificado incorretamente se lhe fosse atribuído um rótulo de classe sorteado de acordo com a distribuição de probabilidades empíricas daquele nó.

---

## 2. Valores Notáveis do Índice Gini

Para uma classificação binária ($c = 2$):

1. **Nó Perfeitamente Puro ($p_1 = 1, p_2 = 0$)**:
   $$\text{Gini} = 1 - (1^2 + 0^2) = 1 - 1 = \mathbf{0,00}$$
   Todas as observações do nó pertencem à mesma classe. A impureza é nula.
2. **Nó com Impureza Máxima ($p_1 = 0,5, p_2 = 0,5$)**:
   $$\text{Gini} = 1 - (0,5^2 + 0,5^2) = 1 - (0,25 + 0,25) = 1 - 0,5 = \mathbf{0,50}$$
   A incerteza é total; as classes estão perfeitamente misturadas em partes iguais.

---

## 3. Impureza Coletiva da Divisão e Ganho de Divisão

Ao avaliar a divisão de um nó pai com $N$ instâncias em nós filhos $v_1, \dots, v_k$, calcula-se a **Impureza Coletiva Ponderada**:

$$I_{\text{split}} = \sum_{j=1}^{k} \frac{N(v_j)}{N} \cdot \text{Gini}(v_j)$$

O algoritmo CART busca o atributo e o ponto de corte que **minimizam $I_{\text{split}}$**, maximizando a pureza dos nós filhos resultantes.

---

## 4. Comparação: Índice Gini versus Entropia

| Critério | Índice Gini | [[Entropia]] de Shannon |
| :--- | :---: | :---: |
| **Fórmula** | $1 - \sum p_i^2$ | $- \sum p_i \log_2(p_i)$ |
| **Custo Computacional** | **Mais Rápido** (operações puramente quadráticas) | Mais lento (exige cálculo de logaritmos) |
| **Intervalo para 2 Classes** | $[0; 0,5]$ | $[0; 1,0]$ |
| **Algoritmo de Referência** | CART (`rpart` em R) | ID3, C4.5 |

Na prática empírica, ambos os critérios convergem para árvores com estruturas e acurácias quase idênticas na grande maioria dos problemas reais.

---

## 5. Implementação em R

```r
# Função para cálculo do Índice Gini binário
gini <- function(f, n) {
  p1 <- f / n
  p2 <- (n - f) / n
  return(1 - (p1^2 + p2^2))
}

# Exemplos do caderno do curso
cat("Gini nó puro (6 de 6):", gini(6, 6), "\n")       # 0.0
cat("Gini nó quase puro (5 de 6):", gini(5, 6), "\n")  # 0.2778
cat("Gini nó 50/50 (3 de 6):", gini(3, 6), "\n")       # 0.50
```

Para a aplicação detalhada do Índice Gini na indução e poda de modelos preditivos, consulte [[Árvores de Decisão]].
