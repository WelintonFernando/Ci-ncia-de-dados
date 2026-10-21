---
aliases:
  - Confusion Matrix
  - Matriz de Erros
  - Tabela de Contingência
tags:
  - metricas
  - avaliacao
  - classificacao
  - machine-learning
---

# Matriz de Confusão

A **Matriz de Confusão** (*Confusion Matrix*) é a ferramenta analítica fundamental para inspecionar, diagnosticar e mensurar a performance de qualquer algoritmo de classificação no [[Aprendizado de Máquina]] supervisionado. Trata-se de uma tabela de contingência bidimensional que confronta, cruzamento a cruzamento, as previsões emitidas pelo modelo com os rótulos verdadeiros observados na realidade empírica.

Todas as métricas clássicas de desempenho para tarefas de classificação — incluindo [[Acurácia]], [[Precisão]], [[Recall]], [[Especificidade]] e [[F1-Score]] — são derivadas diretamente dos valores contidos nas células dessa matriz, como sintetizado em [[Métricas de Avaliação de Modelos]].

---

## 1. Estrutura Canônica da Matriz Binária ($2 \times 2$)

Para um problema de classificação binária com classes $1$ (Positivo) e $0$ (Negativo), a matriz estrutura-se da seguinte forma:

```
                            CLASSE REAL (OBSERVADA)
                         Positivo (1)         Negativo (0)
                     +--------------------+--------------------+
        Positivo (1) |   VERDADEIRO       |      FALSO         |
                     |   POSITIVO (TP)    |  POSITIVO (FP)     |
CLASSE               |     Acerto         | Erro Tipo I        |
PREDITA              +--------------------+--------------------+
        Negativo (0) |      FALSO         |   VERDADEIRO       |
                     |  NEGATIVO (FN)     |  NEGATIVO (TN)     |
                     | Erro Tipo II       |     Acerto         |
                     +--------------------+--------------------+
```

### 1.1. Os Quatro Quadrantes Elementares

1. **Verdadeiro Positivo ($TP$ — *True Positive*)**:
   - O evento real era positivo ($Y = 1$) e o modelo predisse corretamente como positivo ($\hat{Y} = 1$).
   - *Exemplo*: Um paciente portador de doença infecciosa cujo exame laboratorial retornou positivo.
2. **Falso Positivo ($FP$ — *False Positive*)**:
   - O evento real era negativo ($Y = 0$), mas o modelo predisse erroneamente como positivo ($\hat{Y} = 1$).
   - Na inferência estatística, é denominado **Erro do Tipo I** ou "alarme falso".
   - *Exemplo*: Um e-mail comercial importante descartado indevidamente na pasta de spam.
3. **Verdadeiro Negativo ($TN$ — *True Negative*)**:
   - O evento real era negativo ($Y = 0$) e o modelo confirmou corretamente como negativo ($\hat{Y} = 0$).
   - *Exemplo*: Um indivíduo perfeitamente saudável cujo teste diagnóstico indicou negativo.
4. **Falso Negativo ($FN$ — *False Negative*)**:
   - O evento real era positivo ($Y = 1$), mas o algoritmo predisse incorretamente como negativo ($\hat{Y} = 0$).
   - Na estatística, é denominado **Erro do Tipo II** ou "omissão perigosa".
   - *Exemplo*: Uma transação fraudulenta de clonagem de cartão aprovada sem bloqueio.

---

## 2. Mapa Completo das Métricas Derivadas

A partir do somatório das células da matriz, calcula-se o conjunto integral de indicadores de desempenho:

| Métrica Analítica | Fórmula em LaTeX | Interpretação Direta |
| :--- | :---: | :--- |
| **[[Acurácia]]** | $\frac{TP + TN}{TP + TN + FP + FN}$ | Proporção global de acertos do modelo sobre todo o espaço amostral. |
| **[[Precisão]] ($PPV$)** | $\frac{TP}{TP + FP}$ | Confiabilidade das predições positivas (de quem o modelo acusou, quantos eram reais). |
| **[[Recall]] ($TPR$)** | $\frac{TP}{TP + FN}$ | Taxa de captura e cobertura dos casos positivos reais existentes. |
| **[[Especificidade]] ($TNR$)** | $\frac{TN}{TN + FP}$ | Taxa de acerto na identificação dos casos negativos genuínos. |
| **Taxa de Falsos Positivos ($FPR$)** | $\frac{FP}{TN + FP} = 1 - \text{Espec.}$ | Proporção de alarmes falsos gerados sobre o total de negativos reais. |
| **Valor Preditivo Negativo ($NPV$)** | $\frac{TN}{TN + FN}$ | Probabilidade de um caso predito como negativo ser verdadeiramente negativo. |
| **[[F1-Score]]** | $\frac{2TP}{2TP + FP + FN}$ | Média harmônica que equilibra Precisão e Recall em um valor escalar único. |

---

## 3. Matrizes de Confusão em Problemas Multiclasse ($N \times N$)

Quando a variável alvo possui mais de duas categorias (por exemplo, classificação de crédito em `Baixo`, `Médio` e `Alto` risco em [[Árvores de Decisão]]), a matriz expande-se para dimensão $K \times K$:

- A **diagonal principal** representa todos os acertos do modelo;
- Todas as células fora da diagonal principal representam confusões específicas cometidas entre classes;
- O cálculo de métricas individuais é feito aplicando-se a estratégia **Um-contra-Todos** (*One-vs-Rest*), considerando a classe de interesse como positiva e o conjunto das demais como negativa.

---

## 4. Visualização Interativa em Heatmap (Plotly)

O plugin `obsidian-plotly` permite incorporar um mapa de calor interativo da matriz de confusão diretamente nas notas:

```plotly
data:
  - z:
      - [15, 1]
      - [2, 43]
    x: ['Predito Negativo (0)', 'Predito Positivo (1)']
    y: ['Real Negativo (0)', 'Real Positivo (1)']
    type: heatmap
    colorscale: 'Blues'
    showscale: true
layout:
  title: 'Matriz de Confusão: Estudo de Concessão de Crédito'
  xaxis:
    title: 'Classificação Emitida pelo Modelo'
  yaxis:
    title: 'Condição Real do Cliente'
```

---

## 5. Implementação Prática em R

A biblioteca `caret` é o padrão da linguagem [[Introdução ao R|R]] para tabular a matriz e gerar automaticamente o relatório de indicadores:

```r
library(caret)

# Vetores de validação
observado <- factor(c(1, 1, 0, 1, 0, 0, 1, 0, 1, 1))
predito   <- factor(c(1, 1, 0, 0, 0, 0, 1, 1, 1, 1))

# Gerando a Matriz de Confusão completa
resultado_mc <- confusionMatrix(
  data = predito, 
  reference = observado, 
  positive = "1"
)

# Visualizando a tabela de contingência
print(resultado_mc$table)

# Visualizando todas as métricas extraídas
print(resultado_mc$byClass)
```

Para estudar como a matriz de confusão varia ao alterar dinamicamente o limiar de decisão de probabilidades, consulte [[Curva ROC]] e [[AUC]].
