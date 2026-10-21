---
aliases:
  - ROC
  - Receiver Operating Characteristic
  - Curva Característica de Operação do Receptor
tags:
  - metricas
  - avaliacao
  - classificacao
  - machine-learning
---

# Curva ROC

A **Curva ROC** (*Receiver Operating Characteristic* — Curva Característica de Operação do Receptor) é uma das ferramentas gráficas mais poderosas e universalmente consagradas no [[Aprendizado de Máquina]] para avaliar a capacidade discriminativa de modelos de classificação binária (como a [[Regressão Logística]] e as [[Árvores de Decisão]]) através de **todos os limiares de decisão possíveis**.

Originalmente desenvolvida por engenheiros de radar militares durante a Segunda Guerra Mundial para distinguir sinais de aeronaves inimigas de ruídos espúrios causados por bandos de pássaros e nuvens, a técnica foi posteriormente incorporada pela psicofísica, medicina diagnóstica e ciência da computação.

---

## 1. O Conceito e a Dinâmica dos Limiares

Classificadores probabilísticos emitem uma pontuação contínua de propensão $\hat{p} \in [0, 1]$. Para transformar essa probabilidade contínua em uma decisão categórica discreta ($\hat{Y} \in \{0, 1\}$), a prática tradicional adota um ponto de corte estático ($\theta = 0,50$).

Entretanto, avaliar um algoritmo baseado em um único limiar arbitrário mascara seu potencial latente. A Curva ROC supera essa limitação traçando o desempenho do classificador em **todo o contínuo de corte $\theta \in [0, 1]$**, tornando visível o trade-off exato entre a taxa de detecção correta e a taxa de alarmes falsos.

---

## 2. Coordenadas e Construção da Curva

A curva é traçada em um plano cartesiano unitário $[0, 1] \times [0, 1]$:

```
    TPR (Recall / Sensibilidade)
    1.0 +--------------------+ (Ponto Ideal: 0, 1)
        |                 .-'|
        |              .-'   |      Curva do Modelo Preditivo
        |           .-'      |
        |        .-'         |
        |     .-'            |
        |  .-'               |
        |.'                  |      Linha Diagonal: Classificador Aleatório (y = x)
    0.0 +--------------------+
       0.0                  1.0     FPR (1 - Especificidade / Alarmes Falsos)
```

- **Eixo Y (Ordenadas) — Taxa de Verdadeiros Positivos ($\text{TPR}$)**:
  Representa o [[Recall]] ou Sensibilidade:
  $$\text{TPR} = \frac{TP}{TP + FN}$$
- **Eixo X (Abscissas) — Taxa de Falsos Positivos ($\text{FPR}$)**:
  Representa o complemento da [[Especificidade]] (ou taxa de alarmes falsos):
  $$\text{FPR} = \frac{FP}{TN + FP} = 1 - \text{Especificidade}$$

### O Processo de Varredura do Limiar ($\theta$)
1. **Limiar Extremo ($\theta = 1,0$)**: O modelo não classifica ninguém como positivo. Portanto, $TP = 0$ e $FP = 0$, posicionando o ponto inicial na origem cartesiana **$(0, 0)$**.
2. **Redução Progressiva de $\theta$**: Conforme o limiar cai, o modelo passa a rotular instâncias como positivas. Os verdadeiros positivos sobem rapidamente (deslocamento para cima), enquanto alguns alarmes falsos surgem (deslocamento para a direita).
3. **Limiar Extremo ($\theta = 0,0$)**: O modelo classifica todas as instâncias como positivas. Logo, todos os positivos reais são capturados ($TPR = 1,0$), mas todos os negativos reais são classificados erroneamente como positivos ($FPR = 1,0$), culminando no ponto **$(1, 1)$**.

---

## 3. Interpretação das Zonas do Gráfico

- **Ponto $(0, 1)$ — O Canto Superior Esquerdo**: Representa a perfeição teórica. O modelo atinge $100\%$ de [[Recall]] ($\text{TPR} = 1,0$) com exatamente $0\%$ de falsos alarmes ($\text{FPR} = 0,0$). Quanto mais a curva se aproxima desse vértice, superior é o classificador.
- **A Diagonal de 45° ($y = x$)**: Corresponde a um modelo puramente aleatório (equivalente a jogar cara ou coroa). Para cada acerto positivo obtido, comete-se uma proporção idêntica de alarmes falsos.
- **Região Abaixo da Diagonal**: Indica um modelo sistematicamente invertido. Se invertermos as regras de predição do modelo (trocar $1$ por $0$), ele se tornará um modelo excelente posicionado acima da diagonal.

A integral da área delimitada abaixo dessa curva é a consagrada métrica escalar **[[AUC]]** (*Area Under the Curve*).

---

## 4. Gráfico Interativo da Curva ROC (Plotly)

Visualização dinâmica pronta para exploração via plugin `obsidian-plotly`:

```plotly
data:
  - x: [0, 0.02, 0.05, 0.10, 0.18, 0.30, 0.55, 1.0]
    y: [0, 0.65, 0.82, 0.90, 0.95, 0.97, 0.99, 1.0]
    type: scatter
    mode: lines+markers
    name: 'Modelo Analítico (AUC = 0.94)'
    line:
      color: '#1f77b4'
      width: 3
  - x: [0, 1]
    y: [0, 1]
    type: scatter
    mode: lines
    name: 'Linha de Base Aleatória (AUC = 0.50)'
    line:
      dash: dash
      color: '#d62728'
      width: 2
layout:
  title: 'Curva Característica de Operação do Receptor (ROC)'
  xaxis:
    title: 'Taxa de Falsos Positivos (1 - Especificidade)'
    range: [0, 1]
  yaxis:
    title: 'Taxa de Verdadeiros Positivos (Recall / Sensibilidade)'
    range: [0, 1]
```

---

## 5. Implementação Prática em R com o Pacote ROCR

O pacote `ROCR` é a ferramenta de referência em [[Introdução ao R|R]] para computação e traçado da Curva ROC:

```r
library(ROCR)

# Vetores de probabilidades contínuas emitidas e classes reais
probabilidades <- c(0.95, 0.88, 0.80, 0.72, 0.65, 0.55, 0.40, 0.30, 0.20, 0.05)
classes_reais  <- c(1,    1,    1,    1,    0,    1,    0,    0,    0,    0)

# 1. Criação do objeto de predição do ROCR
objeto_predicao <- prediction(predictions = probabilidades, labels = classes_reais)

# 2. Computação das medidas TPR (Sensibilidade) e FPR (1 - Especificidade)
objeto_desempenho <- performance(objeto_predicao, measure = "tpr", x.measure = "fpr")

# 3. Traçado do gráfico com linha diagonal de referência
plot(objeto_desempenho, col = "blue", lwd = 2.5, main = "Curva ROC no R")
abline(a = 0, b = 1, col = "red", lty = 2)

# 4. Cálculo da métrica AUC
auc_objeto <- performance(objeto_predicao, measure = "auc")
auc_valor  <- auc_objeto@y.values[[1]]
cat("Área sob a Curva ROC (AUC):", round(auc_valor, 4), "\n")
```

Para uma análise quantitativa da pontuação escalar dessa curva, consulte [[AUC]] e estude os impactos na [[Matriz de Confusão]].
