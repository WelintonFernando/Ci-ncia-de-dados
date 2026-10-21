---
aliases:
  - Entropy
  - Entropia de Shannon
  - Ganho de Informação
  - Information Gain
tags:
  - teoria-da-informacao
  - arvores-de-decisao
  - machine-learning
---

# Entropia (Teoria da Informação)

A **Entropia** — formalizada por Claude Shannon em 1948 na Teoria Matemática da Comunicação — é uma medida que quantifica o nível fundamental de **incerteza, desordem ou aleatoriedade** associado à distribuição de probabilidades de uma variável aleatória discreta.

No contexto do [[Aprendizado de Máquina]], a Entropia é empregada por algoritmos de indução de [[Árvores de Decisão]] (como o **ID3** e o **C4.5**) para medir a impureza de nós e calcular o **Ganho de Informação** (*Information Gain*) gerado por divisões de atributos.

---

## 1. Formulação Matemática

Para um nó $t$ que contém observações distribuídas entre $c$ classes categóricas distintas, onde $p_i(t)$ é a proporção relativa de instâncias pertencentes à classe $i$:

$$\text{Entropia}(t) = - \sum_{i=1}^{c} p_i(t) \cdot \log_2[p_i(t)]$$

*Convenção matemática necessária*: se $p_i(t) = 0$, define-se:
$$\lim_{p \to 0^+} p \log_2(p) = 0$$

Como a base logarítmica adotada é a base $2$, a unidade de medida da entropia é o **bit** (ou *shannon*).

---

## 2. Comportamento e Valores Limítrofes

Para o caso clássico de duas classes ($c = 2$):

1. **Homogeneidade Total (Nó Perfeitamente Puro)**:
   Se todas as observações pertencem exclusivamente a uma única classe ($p_1 = 1, p_2 = 0$):
   $$\text{Entropia} = - (1 \cdot \log_2 1 + 0) = - (1 \cdot 0 + 0) = \mathbf{0,00 \text{ bits}}$$
   A incerteza é nula: qualquer nova observação retirada deste nó terá sua classe conhecida com certeza absoluta.
2. **Heterogeneidade Máxima (Nó Equitativo 50%/50%)**:
   Se as duas classes estão perfeitamente balanceadas ($p_1 = 0,5, p_2 = 0,5$):
   $$\text{Entropia} = - \left( 0,5 \cdot \log_2(0,5) + 0,5 \cdot \log_2(0,5) \right) = - \left( 0,5 \cdot (-1) + 0,5 \cdot (-1) \right) = \mathbf{1,00 \text{ bit}}$$
   A desordem é máxima: é impossível prever a classe sem obter informação adicional.

---

## 3. O Ganho de Informação (*Information Gain*)

O **Ganho de Informação** ($IG$) mensura a redução líquida de incerteza obtida ao particionar um nó ancestral $P$ (com $N$ observações) em $k$ nós filhos ($v_1, \dots, v_k$), onde cada filho recebe $N(v_j)$ instâncias:

$$IG = \text{Entropia}(P) - \sum_{j=1}^{k} \frac{N(v_j)}{N} \cdot \text{Entropia}(v_j)$$

O algoritmo avalia todos os preditores candidatos e elege a divisão que gera o **maior Ganho de Informação**, como demonstrado nos cálculos analíticos passo a passo em [[Árvores de Decisão]].

---

## 4. Comparativo: Entropia versus Índice Gini

- A Entropia atinge pico máximo de $1,0$ bit para $2$ classes, enquanto o [[Índice Gini]] atinge pico de $0,50$.
- A curvatura de ambas as funções é estritamente côncava e muito semelhante no intervalo $[0, 1]$.
- O algoritmo CART prefere o [[Índice Gini]] pelo ganho computacional decorrente de não computar a função transcendental $\log_2(x)$.

---

## 5. Implementação Prática em R

```r
# Função para cálculo da Entropia de Shannon em 2 classes
entropia <- function(f, n) {
  p1 <- f / n
  p2 <- (n - f) / n
  
  k1 <- if (p1 == 0) 0 else p1 * log2(p1)
  k2 <- if (p2 == 0) 0 else p2 * log2(p2)
  
  return(-(k1 + k2))
}

# Exemplos práticos
cat("Entropia nó puro (6 de 6):", entropia(6, 6), "bits\n")       # 0.0
cat("Entropia nó 5 de 6:", round(entropia(5, 6), 4), "bits\n")     # 0.6500
cat("Entropia nó 50/50 (3 de 6):", entropia(3, 6), "bits\n")      # 1.0
```

Para compreender a aplicação da entropia na seleção de atributos categóricos e numéricos, consulte [[Árvores de Decisão]].
