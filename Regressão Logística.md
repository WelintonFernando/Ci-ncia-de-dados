---
aliases:
  - Regressão Logística
  - Logit
  - Classificação Binária
  - Odds Ratio
  - Razão de Chances
tags:
  - machine-learning
  - classificacao
  - regressao-logistica
  - r
---

# Regressão Logística

A **Regressão Logística** é o algoritmo fundamental de [[Aprendizado de Máquina]] supervisionado para tarefas de **classificação binária**, isto é, problemas onde a variável dependente de interesse ($Y$) assume apenas dois valores possíveis, categorizados classicamente como $0$ e $1$ (por exemplo: aprovado/reprovado, fraudulento/legítimo, água potável/não potável, doente/sadio).

Enquanto a [[Regressão Linear]] é projetada para prever valores numéricos em toda a reta real ($\mathbb{R}$), a regressão logística modela a **probabilidade condicional** $p = P(Y = 1 | X)$, garantindo que as estimativas estejam matematicamente restritas ao intervalo aberto $(0, 1)$.

---

## 1. Por que a Regressão Linear Falha na Classificação Binária?

Tentar aplicar os Mínimos Quadrados Ordinários (OLS) diretamente a um desfecho binário $Y \in \{0, 1\}$ gera três falhas metodológicas graves:

1. **Predições de Probabilidade Extrapoladas**: A reta de regressão linear não possui assíntotas horizontais. Para valores extremos de $X$, ela invariavelmente prediz valores absurdos como probabilidades negativas ($p < 0$) ou superiores a 100% ($p > 1$).
2. **Heterocedasticidade Intrínseca**: A variância de uma variável aleatória com distribuição de Bernoulli depende de sua própria média:
   $$\text{Var}(Y | X) = p(X) \cdot [1 - p(X)]$$
   Como $p(X)$ varia em função de $X$, a premissa de variância constante dos resíduos (homocedasticidade) é necessariamente violada.
3. **Distribuição dos Erros Não Normal**: Os resíduos só podem assumir dois valores discretos ($1 - \hat{p}$ ou $-\hat{p}$), invalidando os testes de significância baseados na distribuição Gaussiana.

---

## 2. A Função Logística (Sigmoide)

Para mapear qualquer combinação linear real $z \in (-\infty, +\infty)$ no espaço restrito de probabilidades $(0, 1)$, a regressão logística utiliza a **função logística padrão** (também chamada de curva sigmoide):

$$p(z) = \sigma(z) = \frac{1}{1 + e^{-z}} = \frac{e^z}{1 + e^z}$$

```plotly
data:
  - x: [-6, -5, -4, -3, -2.5, -2, -1.5, -1, -0.5, 0, 0.5, 1, 1.5, 2, 2.5, 3, 4, 5, 6]
    y: [0.002, 0.007, 0.018, 0.047, 0.076, 0.119, 0.182, 0.269, 0.378, 0.500, 0.622, 0.731, 0.818, 0.881, 0.924, 0.953, 0.982, 0.993, 0.998]
    type: scatter
    mode: lines
    name: 'Curva Sigmoide σ(z)'
    line:
      color: '#1f77b4'
      width: 3
  - x: [-6, 6]
    y: [0.5, 0.5]
    type: scatter
    mode: lines
    name: 'Limiar de Corte (p = 0.5)'
    line:
      color: '#d62728'
      dash: dash
      width: 2
  - x: [0]
    y: [0.5]
    type: scatter
    mode: markers
    name: 'Ponto de Inflexão (0, 0.5)'
    marker:
      color: '#d62728'
      size: 9
layout:
  title: 'Função Logística: Mapeamento de z em Probabilidade'
  xaxis:
    title: 'Combinação Linear: z = β₀ + β₁X₁ + ...'
  yaxis:
    title: 'Probabilidade Estimada: p(z)'
    range: [-0.05, 1.05]
  hovermode: 'closest'
```

Onde a combinação linear dos preditores é dada por:

$$z = \beta_0 + \beta_1 X_1 + \beta_2 X_2 + \dots + \beta_k X_k$$

Propriedades da curva sigmoide:
- Quando $z \to +\infty \implies p \to 1$;
- Quando $z \to -\infty \implies p \to 0$;
- Quando $z = 0 \implies p = 0,5$.

---

## 3. Razão de Chances (*Odds*) e a Função Logit

Para compreender o significado dos coeficientes $\beta$, é indispensável derivar as relações de **Chance** (*Odds*) e **Log-Odds** (*Logit*).

### 3.1. A Razão de Chances (*Odds Ratio*)
A chance de ocorrência do evento positivo ($Y = 1$) é definida pela razão entre a probabilidade de o evento ocorrer ($p$) e a probabilidade de ele não ocorrer ($1 - p$):

$$\text{Odds} = \frac{p}{1 - p}$$

- Se a probabilidade de aprovação de um crédito for $p = 0,80$, a probabilidade de recusa é $1 - p = 0,20$.
- A chance de aprovação é $\text{Odds} = \frac{0,80}{0,20} = 4$. Ou seja, as chances de aprovação são de 4 para 1.

### 3.2. A Transformação Logit
Substituindo a função sigmoide na equação da chance:

$$\frac{p}{1 - p} = \frac{\frac{e^z}{1 + e^z}}{1 - \frac{e^z}{1 + e^z}} = \frac{\frac{e^z}{1 + e^z}}{\frac{1}{1 + e^z}} = e^z$$

Aplicando o logaritmo natural ($\ln$) em ambos os lados, obtemos a **função logit**:

$$\text{logit}(p) = \ln\left( \frac{p}{1 - p} \right) = z = \beta_0 + \beta_1 X_1 + \beta_2 X_2 + \dots + \beta_k X_k$$

Essa linearização é elegante: o logaritmo da razão de chances é uma função linear dos parâmetros preditores!

---

## 4. Interpretação dos Coeficientes $\beta$

Ao contrário da regressão linear, onde o coeficiente representa um impacto aditivo em $Y$, na regressão logística o coeficiente $\beta_j$ representa a variação no **logaritmo da chance** para cada unidade adicional em $X_j$.

Para interpretar o impacto prático na escala de chances do mundo real, aplicamos a função exponencial:

$$\text{Impacto Multiplicativo nas Chances} = e^{\beta_j}$$

- Se $\beta_j > 0 \implies e^{\beta_j} > 1$: O aumento em $X_j$ **eleva as chances** de o evento positivo ocorrer.
- Se $\beta_j < 0 \implies e^{\beta_j} < 1$: O aumento em $X_j$ **reduz as chances** do evento positivo.
- Se $\beta_j = 0 \implies e^{\beta_j} = 1$: O atributo não exerce qualquer efeito multiplicativo sobre as chances.

---

## 5. Estimação por Máxima Verossimilhança (MLE)

Como a variável resposta segue uma distribuição de Bernoulli, a estimação dos parâmetros $\boldsymbol{\beta}$ não é realizada por Mínimos Quadrados, mas pelo método de **Máxima Verossimilhança** (*Maximum Likelihood Estimation* — MLE).

### 5.1. Função de Verossimilhança
A probabilidade conjunta de observar a amostra empírica independente de $n$ pontos é:

$$L(\boldsymbol{\beta}) = \prod_{i=1}^{n} [p(X_i)]^{y_i} \cdot [1 - p(X_i)]^{1 - y_i}$$

Onde $y_i \in \{0, 1\}$.

### 5.2. Log-Verossimilhança (*Log-Likelihood*)
Por conveniência matemática e estabilidade numérica, maximiza-se o logaritmo natural de $L$:

$$\ell(\boldsymbol{\beta}) = \ln L(\boldsymbol{\beta}) = \sum_{i=1}^{n} \left[ y_i \ln(p(X_i)) + (1 - y_i) \ln(1 - p(X_i)) \right]$$

Essa equação não possui solução analítica em forma fechada. Sua maximização é obtida por algoritmos numéricos iterativos, como o método de **Newton-Raphson** ou **Fisher Scoring**.

---

## 6. Tomada de Decisão e Ajuste do Limiar de Corte (*Cutoff*)

O modelo logístico emite uma probabilidade contínua $\hat{p} \in [0, 1]$. Para convertê-la em uma classificação binária discreta $\hat{Y} \in \{0, 1\}$, estabelece-se um **limiar de decisão** ($\theta$ ou *cutoff*):

$$\hat{Y} = \begin{cases} 1, & \text{se } \hat{p} \ge \theta \\ 0, & \text{se } \hat{p} < \theta \end{cases}$$

- **Limiar Padrão ($\theta = 0,5$)**: Utilizado quando os custos de cometer um Falso Positivo ($FP$) e um Falso Negativo ($FN$) são equivalentes.
- **Calibração de $\theta$ em Casos Críticos**:
  - Na detecção de fraudes ou diagnóstico de doenças graves, deixar passar um caso positivo ($FN$) é inaceitável. Reduz-se o limiar (ex: $\theta = 0,20$) para priorizar o [[Recall]].
  - Em campanhas caras de marketing direto ou concessão conservadora de crédito, prioriza-se a [[Precisão]], elevando o limiar (ex: $\theta = 0,70$).

A análise do comportamento do modelo em todos os cortes possíveis é formalizada pela [[Curva ROC]] e pelo valor de [[AUC]] em [[Métricas de Avaliação de Modelos]].

---

## 7. Estudo de Caso Prático 1: Concessão de Empréstimo Bancário

Nos materiais do curso (`reglog_1.pdf`), analisa-se um dataset de propostas de empréstimo financeiro (`emprestimo`: 1 = aprovado, 0 = recusado) baseado em `pont_credito` (escore de crédito) e `renda`:

```r
# Preparação do ambiente
rm(list = ls())
library(caret)
library(ROCR)

# Carga do dataset
load("Material/CAP 3 - Análise de dados/dados_emprestimo.RData")

# Treinamento do modelo logístico univariado com a pontuação de crédito
modlog <- glm(formula = emprestimo ~ pont_credito, data = emp, family = binomial(link = "logit"))
summary(modlog)
```

### Saída do Modelo no R
```text
Coefficients:
             Estimate Std. Error z value Pr(>|z|)  
(Intercept)  -79.3401    35.7382  -2.220   0.0264 *
pont_credito   0.1214     0.0549   2.212   0.0270 *
---
Null deviance: 70.204  on 60  degrees of freedom
Residual deviance: 13.412  on 59  degrees of freedom
AIC: 17.412
```

### Interpretação dos Resultados
- O coeficiente de `pont_credito` é $\hat{\beta}_1 = 0,1214$ ($p = 0,027 < 0,05$, estatisticamente significativo).
- Calculando o efeito multiplicativo nas chances:
  $$e^{0,1214} = 1,129$$
- **Conclusão de Negócio**: Para cada ponto adicional no escore de crédito do cliente, a chance de ter o empréstimo aprovado cresce em **$12,9\%$**!

### Matriz de Confusão e Indicadores

```r
# Predição de probabilidades
emp$prob_predita <- predict(modlog, type = "response")

# Classificação usando limiar padrão de 0.5
emp$classe_predita <- ifelse(emp$prob_predita >= 0.5, 1, 0)

# Avaliação com caret
matriz_confusao <- confusionMatrix(
  data = factor(emp$classe_predita),
  reference = factor(emp$emprestimo),
  positive = "1"
)
print(matriz_confusao)
```

No caderno do professor, o modelo alcançou:
- **[[Acurácia]]**: $95,08\%$
- **[[Recall|Sensibilidade (Recall)]]**: $95,56\%$
- **[[Especificidade]]**: $93,75\%$
- **[[Precisão]]**: $97,73\%$
- **[[AUC|Área sob a Curva ROC (AUC)]]**: $0,994$

---

## 8. Estudo de Caso Prático 2: Potabilidade da Água (*Water Quality*)

No caderno `Water_Quality_Reg_Logistica.ipynb`, o desafio consiste em classificar se amostras de água são seguras para consumo humano (`potavel`: 0 ou 1) com base em 20 propriedades químicas e biológicas (alumínio, arsênio, bário, cádmio, clorofórmio, chumbo, nitratos etc.):

```r
# Carga e particionamento dos dados
dados_agua <- read.csv("Material/CAP 3 - Análise de dados/waterQuality1.csv")

# Baseline: Modelo com todas as variáveis químicas
mod_agua_base <- glm(potavel ~ ., data = treino_agua, family = "binomial")

# Avaliação da Curva ROC no conjunto de teste
predicoes_teste <- predict(mod_agua_base, newdata = teste_agua, type = "response")
objeto_pred <- prediction(predicoes_teste, teste_agua$potavel)
performance_roc <- performance(objeto_pred, measure = "tpr", x.measure = "fpr")

# Cálculo da AUC
auc_valor <- performance(objeto_pred, measure = "auc")@y.values[[1]]
cat("AUC no conjunto de teste:", round(auc_valor, 4), "\n")
```

Essa modelagem probabilística fornece a base conceitual para compreender classificadores não lineares e não paramétricos, como as [[Árvores de Decisão]].
