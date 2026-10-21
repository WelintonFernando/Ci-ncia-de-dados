---
aliases:
  - F1 Score
  - F-Score
  - F-Measure
  - F-Beta Score
tags:
  - metricas
  - avaliacao
  - classificacao
  - machine-learning
---

# F1-Score

O **F1-Score** (também denominado *F-Measure* ou Pontuação $F_1$) é a métrica padrão no [[Aprendizado de Máquina]] para avaliar o equilíbrio entre a [[Precisão]] e o [[Recall]] de um classificador binário por meio de um único valor escalar sintético.

Em cenários reais com desbalanceamento amostral severo, a [[Acurácia]] falha como indicador de qualidade. Por outro lado, avaliar a [[Precisão]] e o [[Recall]] separadamente pode ser inconclusivo quando um algoritmo supera o outro em apenas uma das duas dimensões. O $F_1$-Score resolve esse dilema agregando ambos os critérios em uma métrica unificada em [[Métricas de Avaliação de Modelos]].

---

## 1. Formulação Matemática

O $F_1$-Score é definido como a **média harmônica** entre a [[Precisão]] e o [[Recall]]:

$$F_1 = 2 \cdot \frac{\text{Precisão} \cdot \text{Recall}}{\text{Precisão} + \text{Recall}}$$

### Expressão Direta pelos Quadrantes da Matriz de Confusão
Lembrando que:
$$\text{Precisão} = \frac{TP}{TP + FP} \quad \text{e} \quad \text{Recall} = \frac{TP}{TP + FN}$$

Substituindo na expressão da média harmônica e simplificando algebricamente os termos da [[Matriz de Confusão]]:

$$F_1 = \frac{2TP}{2TP + FP + FN}$$

Propriedades fundamentais:
- O valor varia estritamente no intervalo fechado: $0 \le F_1 \le 1$ (ou de $0\%$ a $100\%$);
- Não depende do número de Verdadeiros Negativos ($TN$), tornando-o **completamente imune à distorção por excesso de instâncias negativas fáceis**.

---

## 2. Por que Média Harmônica e Não Aritmética?

A média aritmética simples entre duas variáveis $A$ e $B$ é dada por $\frac{A + B}{2}$. Se utilizássemos a média aritmética para combinar Precisão e Recall:

- Considere um classificador ingênuo com $\text{Precisão} = 1,0$ ($100\%$) e $\text{Recall} = 0,01$ ($1\%$);
- Média aritmética simples: $\frac{1,0 + 0,01}{2} = 0,505$ ($50,5\%$). Transmitiria a falsa impressão de que o modelo tem performance aceitável!

A **média harmônica** possui a propriedade matemática de convergir assintoticamente para o menor valor da dupla sempre que um deles aproxima-se de zero:

$$F_1 = 2 \cdot \frac{1,0 \cdot 0,01}{1,0 + 0,01} = \frac{0,02}{1,01} \approx 0,0198 \quad (1,98\%)$$

> [!IMPORTANT]
> Para que um modelo obtenha um $F_1$-Score elevado, ele é matematicamente obrigado a apresentar **alta performance em AMBAS as métricas**: tanto na [[Precisão]] quanto no [[Recall]].

---

## 3. Generalização: A Família $F_\beta$-Score

Quando o domínio de negócio não atribui o mesmo peso à Precisão e ao Recall, utiliza-se a formulação paramétrica generalizada **$F_\beta$**:

$$F_\beta = (1 + \beta^2) \cdot \frac{\text{Precisão} \cdot \text{Recall}}{(\beta^2 \cdot \text{Precisão}) + \text{Recall}}$$

Onde o hiperparâmetro $\beta > 0$ calibra a importância relativa:
- **$\beta = 1$ ($F_1$-Score)**: Atribui pesos perfeitamente idênticos à Precisão e ao Recall.
- **$\beta = 2$ ($F_2$-Score)**: Atribui **peso duas vezes maior ao [[Recall]]** do que à Precisão. Indicado em diagnóstico médico e detecção de fraudes financeiras.
- **$\beta = 0,5$ ($F_{0,5}$-Score)**: Atribui **peso duas vezes maior à [[Precisão]]** do que ao Recall. Indicado em filtros de spam e sistemas de recomendação de alto risco.

---

## 4. Implementação Prática em R

```r
library(caret)

reais    <- factor(c(1, 1, 1, 1, 0, 0, 1, 0, 1, 0))
preditos <- factor(c(1, 1, 1, 0, 0, 1, 1, 0, 1, 0))

# 1. Cálculo Manual
tp <- sum(reais == 1 & preditos == 1)
fp <- sum(reais == 0 & preditos == 1)
fn <- sum(reais == 1 & preditos == 0)

precisao <- tp / (tp + fp)
recall   <- tp / (tp + fn)

f1_manual <- 2 * (precisao * recall) / (precisao + recall)
cat("Precisão:", round(precisao, 4), "\n")
cat("Recall:  ", round(recall, 4), "\n")
cat("F1-Score Manual:", round(f1_manual, 4), "\n")

# 2. Extração via pacote caret
mc <- confusionMatrix(data = preditos, reference = reais, positive = "1")
cat("F1-Score (caret):", round(mc$byClass["F1"], 4), "\n")
```

Para uma visão sistemática de avaliação e comparação visual entre múltiplos modelos, consulte [[Métricas de Avaliação de Modelos]] e os gráficos de desempenho em [[Visualização de Dados com Plotly]].
