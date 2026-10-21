---
aliases:
  - Regressão Linear
  - Regressão Simples
  - Regressão Múltipla
  - Mínimos Quadrados Ordinários
  - OLS
tags:
  - machine-learning
  - regressao
  - estatistica
  - r
---

# Regressão Linear

A **Regressão Linear** é uma das técnicas seminais e mais amplamente utilizadas no [[Aprendizado de Máquina]] supervisionado e na econometria. Seu propósito central é modelar matematicamente a relação quantitativa entre uma **variável dependente contínua** (também denominada variável resposta, desfecho ou *target*, denotada por $Y$) e uma ou mais **variáveis independentes** (preditores, regressores ou *features*, denotadas por $X$).

No ambiente de [[Introdução ao R|R]], a regressão linear fornece não apenas estimativas numéricas de predição, mas também um arcabouço robusto de inferência estatística para testes de hipóteses, significância de parâmetros e intervalos de confiança.

---

## 1. Regressão Linear Simples

A Regressão Linear Simples analisa o impacto de um único preditor $X$ sobre a resposta $Y$.

### 1.1. Formulação Matemática Populacional
O modelo linear teórico da população é expresso por:

$$Y_i = \beta_0 + \beta_1 X_i + \epsilon_i$$

Onde:
- $Y_i$ é o $i$-ésimo valor observado da variável dependente;
- $X_i$ é o $i$-ésimo valor observado do preditor independente;
- $\beta_0$ é o **intercepto** (ou constante linear), representando o valor esperado de $Y$ quando $X = 0$;
- $\beta_1$ é o **coeficiente de inclinação** (ou coeficiente angular), medindo a variação esperada em $Y$ para cada acréscimo unitário em $X$;
- $\epsilon_i$ é o **erro estocástico** ou distúrbio aleatório (efeito de variáveis não observadas e ruídos de medição).

### 1.2. Equação Amostral Estimada
Como os parâmetros populacionais $\beta_0$ e $\beta_1$ são desconhecidos, calculamos suas estimativas amostrais $\hat{\beta}_0$ e $\hat{\beta}_1$:

$$\hat{Y}_i = \hat{\beta}_0 + \hat{\beta}_1 X_i$$

O **resíduo** $e_i$ de cada observação representa o desvio empírico entre o valor real e a reta predita:

$$e_i = Y_i - \hat{Y}_i = Y_i - (\hat{\beta}_0 + \hat{\beta}_1 X_i)$$

---

## 2. O Método dos Mínimos Quadrados Ordinários (OLS)

O método padrão para estimar os coeficientes da reta de regressão é o dos **Mínimos Quadrados Ordinários** (*Ordinary Least Squares* — OLS). Seu critério de otimização consiste em minimizar a **Soma dos Quadrados dos Resíduos** ($SSE$ — *Sum of Squared Errors*):

$$S(\beta_0, \beta_1) = \sum_{i=1}^{n} e_i^2 = \sum_{i=1}^{n} (Y_i - \beta_0 - \beta_1 X_i)^2$$

### Dedução Analítica dos Estimadores
Para encontrar o ponto de mínimo global, calculamos as derivadas parciais de $S$ em relação a $\beta_0$ e $\beta_1$ e as igualamos a zero:

1. **Derivada em relação a $\beta_0$**:
   $$\frac{\partial S}{\partial \beta_0} = -2 \sum_{i=1}^{n} (Y_i - \beta_0 - \beta_1 X_i) = 0 \implies \sum Y_i - n\beta_0 - \beta_1 \sum X_i = 0$$
   Dividindo por $n$, obtemos:
   $$\hat{\beta}_0 = \bar{Y} - \hat{\beta}_1 \bar{X}$$

2. **Derivada em relação a $\beta_1$**:
   $$\frac{\partial S}{\partial \beta_1} = -2 \sum_{i=1}^{n} X_i (Y_i - \beta_0 - \beta_1 X_i) = 0$$
   Substituindo $\hat{\beta}_0$:
   $$\sum X_i (Y_i - \bar{Y} + \hat{\beta}_1 \bar{X} - \hat{\beta}_1 X_i) = 0 \implies \sum (X_i - \bar{X})(Y_i - \bar{Y}) - \hat{\beta}_1 \sum (X_i - \bar{X})^2 = 0$$

Isolando $\hat{\beta}_1$:

$$\hat{\beta}_1 = \frac{\sum_{i=1}^{n} (X_i - \bar{X})(Y_i - \bar{Y})}{\sum_{i=1}^{n} (X_i - \bar{X})^2} = \frac{\text{Cov}(X, Y)}{\text{Var}(X)}$$

---

## 3. As Premissas Clássicas de Gauss-Markov

O Teorema de Gauss-Markov estabelece que, sob certas premissas, os estimadores de Mínimos Quadrados são **BLUE** (*Best Linear Unbiased Estimators* — Melhores Estimadores Lineares Não Viesados com variância mínima):

1. **Linearidade nos Parâmetros**: A relação entre as variáveis deve ser descrita por uma função linear dos coeficientes $\beta$.
2. **Média Condicional dos Erros Nula**: $E[\epsilon_i | X_i] = 0$. Em média, o modelo não subestima nem superestima o resultado.
3. **Homocedasticidade**: A variância dos resíduos é constante para qualquer valor de $X$: $\text{Var}(\epsilon_i) = \sigma^2$. A violação dessa premissa gera *heterocedasticidade*.
4. **Ausência de Autocorrelação**: Os erros de observações distintas são estatisticamente independentes: $\text{Cov}(\epsilon_i, \epsilon_j) = 0$ para $i \neq j$.
5. **Exogeneidade Estrita**: As variáveis preditoras não são correlacionadas com os termos de erro.
6. **Normalidade dos Resíduos**: $\epsilon_i \sim \mathcal{N}(0, \sigma^2)$. Premissa necessária para que os testes de significância estatística ($t$-test e $F$-test) sejam rigorosamente válidos.

---

## 4. Regressão Linear Múltipla

Na Regressão Múltipla, o modelo incorpora $k$ preditores simultaneamente:

$$Y_i = \beta_0 + \beta_1 X_{i1} + \beta_2 X_{i2} + \dots + \beta_k X_{ik} + \epsilon_i$$

### 4.1. Formulação Matricial Compacta
Para $n$ observações amostrais:

$$\mathbf{Y} = \mathbf{X}\boldsymbol{\beta} + \boldsymbol{\epsilon}$$

Onde:
$$\mathbf{Y} = \begin{bmatrix} Y_1 \\ Y_2 \\ \vdots \\ Y_n \end{bmatrix}, \quad
\mathbf{X} = \begin{bmatrix} 1 & X_{11} & X_{12} & \dots & X_{1k} \\ 1 & X_{21} & X_{22} & \dots & X_{2k} \\ \vdots & \vdots & \vdots & \ddots & \vdots \\ 1 & X_{n1} & X_{n2} & \dots & X_{nk} \end{bmatrix}, \quad
\boldsymbol{\beta} = \begin{bmatrix} \beta_0 \\ \beta_1 \\ \vdots \\ \beta_k \end{bmatrix}, \quad
\boldsymbol{\epsilon} = \begin{bmatrix} \epsilon_1 \\ \epsilon_2 \\ \vdots \\ \epsilon_n \end{bmatrix}$$

A solução analítica matricial dos Mínimos Quadrados é dada por:

$$\hat{\boldsymbol{\beta}} = (\mathbf{X}^T \mathbf{X})^{-1} \mathbf{X}^T \mathbf{Y}$$

Essa equação exige que a matriz de produto cruzado $(\mathbf{X}^T \mathbf{X})$ seja invertível, justificando a regra estrita de evitar a multicolinearidade explicada em [[Pré-Processamento e Engenharia de Atributos]].

### 4.2. Interpretação dos Coeficientes Parciais
Cada coeficiente $\hat{\beta}_j$ mensura o efeito marginal esperado na variável resposta $Y$ correspondente ao aumento de uma unidade no preditor $X_j$, **mantendo constantes todos os demais preditores do modelo** (*ceteris paribus*).

---

## 5. Métricas de Avaliação e Diagnóstico

As fórmulas matemáticas das métricas de regressão em [[Métricas de Avaliação de Modelos]] incluem:

### 5.1. Coeficiente de Determinação ($R^2$)
O $R^2$ expressa a proporção da variabilidade total de $Y$ que é explicada linearmente pelo conjunto de preditores:

$$R^2 = 1 - \frac{SS_{\text{res}}}{SS_{\text{tot}}} = 1 - \frac{\sum_{i=1}^{n} (Y_i - \hat{Y}_i)^2}{\sum_{i=1}^{n} (Y_i - \bar{Y})^2}$$

Onde $0 \le R^2 \le 1$.

### 5.2. Coeficiente de Determinação Ajustado ($R^2_{\text{adj}}$)
Na regressão múltipla, a inclusão de qualquer nova variável (mesmo ruído aleatório puro) nunca diminui o valor de $R^2$. Para penalizar o excesso de variáveis irrelevantes, utiliza-se o $R^2$ ajustado pelos graus de liberdade:

$$R^2_{\text{adj}} = 1 - \left[ \frac{(1 - R^2)(n - 1)}{n - k - 1} \right]$$

Onde $n$ é o tamanho da amostra e $k$ é a quantidade de preditores.

### 5.3. Métricas de Erro Absoluto e Quadrático
- **Erro Absoluto Médio ($MAE$)**:
  $$\text{MAE} = \frac{1}{n} \sum_{i=1}^{n} |Y_i - \hat{Y}_i|$$
- **Erro Quadrático Médio ($MSE$)**:
  $$\text{MSE} = \frac{1}{n} \sum_{i=1}^{n} (Y_i - \hat{Y}_i)^2$$
- **Raiz do Erro Quadrático Médio ($RMSE$)**:
  $$\text{RMSE} = \sqrt{\text{MSE}}$$

---

## 6. Diagnóstico de Resíduos e Modelagem Não Linear

Um modelo com $R^2$ alto pode mascarar violações severas de linearidade. O exame gráfico dos resíduos ($e_i$) em função dos valores ajustados ($\hat{Y}_i$) é indispensável.

### 6.1. O Caso do Dataset `women` (Altura versus Peso)
No caderno de Regressão Simples do curso, ajustou-se um modelo de regressão para estimar o `peso` a partir da `altura`:

```r
# Carga e modelo linear simples
data(women)
names(women) <- c("altura_pol", "peso_lb")
# Convertendo para unidades do Sistema Internacional (m e kg)
mlh <- data.frame(
  altura = women$altura_pol * 0.0254,
  peso   = women$peso_lb * 0.453592
)

# Ajuste linear simples
reg1 <- lm(peso ~ altura, data = mlh)
summary(reg1)
```

#### Identificação da Não Linearidade
Embora o modelo linear simples tenha apresentado um $R^2 = 0,991$, a inspeção dos resíduos revelou um formato claro de **parábola** (resíduos negativos no centro e fortemente positivos nos extremos):

```r
# Gráfico de resíduos
plot(fitted(reg1), residuals(reg1), main = "Resíduos vs Ajustados (Modelo Linear)")
abline(h = 0, col = "red", lty = 2)
```

```plotly
data:
  - x: [51.2, 53.0, 54.2, 56.0, 57.2, 59.0, 60.8, 62.0, 63.7, 64.9, 66.7, 67.9, 69.7, 70.9, 72.7]
    y: [0.97, 0.08, 0.29, -0.20, 0.01, -0.28, -0.66, -0.45, -0.54, -0.33, -0.32, -0.01, 0.10, 0.61, 0.73]
    type: scatter
    mode: markers
    name: 'Resíduos: Modelo Linear (Padrão Parabólico U)'
    marker:
      color: '#d62728'
      size: 9
  - x: [50, 74]
    y: [0, 0]
    type: scatter
    mode: lines
    name: 'Resíduo Nulo (Referência e = 0)'
    line:
      color: '#7f7f7f'
      dash: dash
      width: 2
  - x: [51.2, 53.0, 56.0, 60.8, 64.9, 69.7, 72.7]
    y: [0.97, 0.10, -0.20, -0.66, -0.33, 0.10, 0.73]
    type: scatter
    mode: lines
    name: 'Tendência Parabólica do Erro'
    line:
      color: '#d62728'
      dash: dot
      width: 2
layout:
  title: 'Diagnóstico de Resíduos: Padrão Não Linear Detectado'
  xaxis:
    title: 'Valores Ajustados (ŷ - Peso Estimado)'
  yaxis:
    title: 'Resíduos (e = y - ŷ)'
  hovermode: 'closest'
```

Essa curvatura nos resíduos é o diagnóstico definitivo de que a relação subjacente possui componente quadrático.

#### Correção com Termo Polinomial
Incorporando o termo quadrático $\text{altura}^2$ com a função `I()`:

```r
# Modelo Polinomial Quadrático
reg2 <- lm(peso ~ altura + I(altura^2), data = mlh)
summary(reg2)
```

#### Tabela Comparativa de Desempenho

| Modelo | Equação Estimada | $MAE$ | $MSE$ | $R^2$ | $R^2_{\text{adj}}$ |
| :--- | :--- | :---: | :---: | :---: | :---: |
| **Linear Simples** | $\text{peso} = -39,44 + 61,36 \cdot \text{altura}$ | $0,520$ | $0,401$ | $0,9910$ | $0,9903$ |
| **Quadrático ($X^2$)** | $\text{peso} = 111,28 - 124,53 \cdot \text{altura} + 56,58 \cdot \text{altura}^2$ | **$0,137$** | **$0,024$** | **$0,9995$** | **$0,9994$** |

A inclusão do termo de 2º grau reduziu o erro quadrático ($MSE$) em mais de **$94\%$** e eliminou o padrão sistemático dos resíduos!

---

## 7. Estudo de Caso Prático: Regressão Múltipla com `state.x77`

O dataset `state.x77` contém indicadores socioeconômicos dos 50 estados dos EUA em 1977. O objetivo é modelar a taxa de criminalidade violenta (`assassinato`):

```r
# Preparação do dataset
df_estados <- as.data.frame(state.x77)
names(df_estados) <- c("populacao", "renda", "analfabetismo", "expectativa_vida", 
                       "assassinato", "formacao_superior", "dias_geada", "area")

# Modelo Base (Baseline) com todas as variáveis
mod_base <- lm(assassinato ~ ., data = df_estados)
summary(mod_base)

# Refinamento: Selecionando apenas preditores estatisticamente significativos (p < 0.05)
mod_refinado <- lm(assassinato ~ populacao + analfabetismo + dias_geada, data = df_estados)
summary(mod_refinado)

# Comparação de critérios de informação (AIC e BIC: quanto menor, melhor)
AIC(mod_base, mod_refinado)
BIC(mod_base, mod_refinado)
```

Modelos refinados com menor complexidade e parcimônia evitam o sobreajuste e generalizam com superioridade nos dados de teste, servindo de ponte direta para os problemas de classificação binária abordados em [[Regressão Logística]].
