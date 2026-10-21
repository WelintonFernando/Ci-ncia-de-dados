---
aliases:
  - Pré-Processamento
  - Engenharia de Atributos
  - Padronização
  - Normalização
  - One-Hot Encoding
  - Variáveis Dummy
tags:
  - pre-processamento
  - feature-engineering
  - machine-learning
  - r
---

# Pré-Processamento e Engenharia de Atributos

O **Pré-Processamento** e a **Engenharia de Atributos** (*Feature Engineering*) constituem o estágio intermediário em que os dados saneados pelo pipeline de [[Extração e Tratamento de Dados (ETL)]] são transformados matematicamente para maximizar a capacidade preditiva dos algoritmos de [[Aprendizado de Máquina]].

Muitos modelos clássicos — como a [[Regressão Linear]] e a [[Regressão Logística]] — operam sob rígidas premissas numéricas (linearidade, escalas compatíveis e independência linear). Aplicar dados brutos sem transformação prévia pode levar a problemas graves como matrizes singulares não invertíveis, dominância indevida de variáveis com grande magnitude numérica e convergência lenta de algoritmos de otimização.

---

## 1. Escala de Atributos: Normalização versus Padronização

Ao trabalhar com múltiplas variáveis contínuas em um mesmo conjunto de dados, é comum encontrar ordens de grandeza discrepantes. Por exemplo, no dataset `state.x77` (dados demográficos dos estados norte-americanos):
- A variável `populacao` varia de $365$ a $21.198$ (milhares de habitantes);
- A variável `renda` varia de $\$3.624$ a $\$6.315$;
- A taxa de `analfabetismo` varia de $0,5\%$ a $2,8\%$;
- A taxa de `assassinato` varia de $1,4$ a $15,1$ por $100.000$ habitantes.

Se alimentarmos um modelo preditivo com esses dados sem ajuste de escala, os coeficientes das variáveis de grande magnitude serão artificialmente achatados, enquanto variáveis de pequenas amplitudes numéricas (mas com alto poder preditivo) podem ser ignoradas.

```
       DADOS ORIGINAIS                             DADOS PADRONIZADOS
Populacao: [365 ...... 21.198]               Populacao: [ -1.02 ... +3.41 ]
Renda:     [3.624 .... 6.315]   === ESCALA ===> Renda:     [ -1.45 ... +2.18 ]
Analfab.:  [0.5 ...... 2.8]                  Analfab.:  [ -1.15 ... +2.34 ]
```

---

### 1.1. Normalização Min-Max (Min-Max Scaling)
A **Normalização Min-Max** reescala linearmente os dados de modo que todos os valores fiquem estritamente contidos no intervalo fechado $[0, 1]$ (ou $[-1, 1]$).

#### Formulação Matemática
Para uma observação $x$ pertencente a uma variável $X$:

$$x_{\text{norm}} = \frac{x - x_{\min}}{x_{\max} - x_{\min}}$$

Onde:
- $x_{\min}$ é o menor valor observado da variável;
- $x_{\max}$ é o maior valor observado da variável;
- $(x_{\max} - x_{\min})$ representa a amplitude amostral total.

#### Implementação Prática em R
```r
# Função personalizada para normalização Min-Max
minmax <- function(x) {
  xmin <- min(x, na.rm = TRUE)
  xmax <- max(x, na.rm = TRUE)
  return((x - xmin) / (xmax - xmin))
}

# Exemplo numérico
valores_brutos <- c(-10, 3, 55, 110, 150, 200)
valores_norm <- minmax(valores_brutos)
print(data.frame(Original = valores_brutos, Normalizado = valores_norm))
# Original Normalizado
#      -10  0.00000000
#        3  0.06190476
#       55  0.30952381
#      110  0.57142857
#      150  0.76190476
#      200  1.00000000
```

- **Vantagens**: Fácil interpretação e preservação exata da relação de distâncias lineares originais.
- **Desvantagens**: É **altamente sensível a *outliers***. A presença de um único ponto extremo colapsa as demais observações para um intervalo muito estreito próximo de zero.

---

### 1.2. Padronização Z-Score (Standardization)
A **Padronização Z-Score** desloca o centro da distribuição para a média zero ($\mu = 0$) e reescala a dispersão para variância unitária ($\sigma = 1$).

#### Formulação Matemática
$$z = \frac{x - \mu}{\sigma}$$

Onde:
- $\mu$ é a média aritmética da amostra: $\mu = \frac{1}{n} \sum_{i=1}^{n} x_i$;
- $\sigma$ é o desvio padrão amostral: $\sigma = \sqrt{\frac{1}{n-1} \sum_{i=1}^{n} (x_i - \mu)^2}$.

#### Implementação Prática em R
O R possui a função nativa `scale()`:

```r
# Padronização de um vetor ou matriz
valores_z <- scale(valores_brutos)
print(mean(valores_z)) # 0 (aproximação numérica)
print(sd(valores_z))   # 1

# Padronizando colunas contínuas de um Data Frame
colunas_numericas <- c("populacao", "renda", "analfabetismo")
st_padronizado <- st
st_padronizado[colunas_numericas] <- scale(st[colunas_numericas])
```

- **Vantagens**: Muito mais robusta na presença de caudas longas; é o formato esperado por algoritmos baseados em descida de gradiente e métodos com penalização de norma (Ridge e Lasso).
- **Desvantagens**: Não delimita um intervalo rígido de mínimo e máximo.

---

### 1.3. Sensibilidade dos Modelos à Escala

| Algoritmo | Sensível à Escala? | Justificativa Teórica |
| :--- | :---: | :--- |
| **[[Regressão Linear]] Simples/Múltipla** | Não (em OLS puro) | Os coeficientes $\hat{\beta}_j$ se ajustam automaticamente às unidades de medida originais. |
| **Regressão com Regularização (Ridge/Lasso)** | **Sim** | A penalidade ($\lambda \sum \beta_j^2$) penaliza coeficientes maiores causados por escalas pequenas. |
| **[[Regressão Logística]]** | Parcialmente | Não altera a convergência teórica do MLE, mas melhora a estabilidade numérica do Fisher Scoring. |
| **[[Árvores de Decisão]]** | **Não** | Os critérios de divisão ([[Índice Gini|Gini]] e [[Entropia]]) dependem apenas da **ordenação** dos pontos. |
| **K-Means / KNN / PCA** | **Altamente Sim** | São baseados estritamente no cálculo de distâncias euclidianas geométricas. |

---

## 2. Codificação de Variáveis Categóricas (One-Hot Encoding)

Algoritmos estatísticos operam internamente sobre espaços vetoriais reais ($\mathbb{R}^n$). Portanto, atributos categóricos com rótulos textuais (ex: `sexo`: "M", "F"; `regiao`: "Sul", "Norte", "Nordeste") precisam ser codificados numericamente.

### 2.1. O Conceito de Variáveis Fictícias (*Dummy Variables*)
A abordagem padrão é o **One-Hot Encoding**, onde cada categoria única é convertida em uma coluna indicadora binária que assume o valor $1$ caso a observação pertença àquela classe e $0$ caso contrário:

$$\text{Dummy}(k) = \begin{cases} 1, & \text{se a categoria for } k \\ 0, & \text{caso contrário} \end{cases}$$

---

### 2.2. A Armadilha da Variável Dummy (*Dummy Variable Trap*)

> [!WARNING]
> Ao converter uma variável categórica com $k$ níveis distintos, **NUNCA** inclua todas as $k$ colunas dummy em uma [[Regressão Linear]] ou [[Regressão Logística]] que contenha constante de intercepto ($\beta_0$).

#### O Problema Matemático da Singularidade
Considere a variável `sexo` com níveis `"F"` e `"M"`. Se criarmos duas colunas dummy $D_F$ e $D_M$:

$$D_F + D_M = 1 \quad (\text{para toda e qualquer observação})$$

Como o modelo de regressão linear já inclui o termo independente $\beta_0 \cdot \mathbf{1}$:

$$\mathbf{x}_{\text{intercepto}} = D_F + D_M$$

Isso cria uma **relação de dependência linear exata** entre as colunas da matriz de planejamento $\mathbf{X}$ (multicolinearidade perfeita). Consequentemente, o determinante da matriz de produto cruzado torna-se nulo:

$$\det(\mathbf{X}^T \mathbf{X}) = 0 \implies (\mathbf{X}^T \mathbf{X})^{-1} \text{ não existe!}$$

Quando isso ocorre em R, a função `lm()` emite o aviso:
```text
Coefficients: (1 not defined because of singularities)
```

#### A Solução Canônica: $k - 1$ Dummies
Para $k$ categorias, deve-se incluir exatamente **$k - 1$** variáveis no modelo. A categoria excluída torna-se a **categoria de referência** (*baseline*):
- O intercepto $\beta_0$ representará o valor esperado médio da categoria de referência;
- Os coeficientes $\beta_j$ das dummies incluídas mensuram a diferença marginal em relação à referência.

```r
# Exemplo em R: Tratamento com 3 níveis (A, B, C)
# Criando dummies manuais
df$trat_A <- ifelse(df$tratamento == "A", 1, 0)
df$trat_B <- ifelse(df$tratamento == "B", 1, 0)
# A categoria "C" é omitida de propósito para servir de referência!

# Ajuste da regressão sem singularidade
modelo_ohe <- lm(resultado ~ dose + trat_A + trat_B, data = df)
summary(modelo_ohe)
```

---

## 3. Engenharia de Interações e Termos Polinomiais

Frequentemente, a resposta $Y$ não é explicada puramente pela soma linear aditiva de atributos isolados, mas pela sinergia conjunta entre variáveis:

### 3.1. Termos de Interação Multiplicativa ($X_1 \cdot X_2$)
Permitem modelar se o efeito de um atributo sobre $Y$ depende da intensidade de outro:

$$Y = \beta_0 + \beta_1 X_1 + \beta_2 X_2 + \beta_3 (X_1 \cdot X_2) + \epsilon$$

No R, o operador `*` inclui as variáveis individuais e a interação (`Y ~ X1 * X2`), enquanto `:` especifica apenas o produto isolado. A sintaxe `(.)^2` gera automaticamente todas as combinações lineares e interações par a par de segundo nível:

```r
# Modelo com todas as interações de até 2º nível entre preditores
modelo_interacao <- lm(resultado ~ (.)^2, data = df_treino)
```

### 3.2. Termos Quadráticos e Polinomiais ($X^2$)
Quando a relação física é curvilínea (parabólica), utiliza-se o operador de proteção `I()` em R:

$$Y = \beta_0 + \beta_1 X + \beta_2 X^2 + \epsilon$$

```r
# Regressão com componente parabólico
modelo_curvo <- lm(peso ~ altura + I(altura^2), data = dados_mulheres)
```

---

## 4. Particionamento Estratificado de Dados

Para validar a capacidade de generalização dos modelos e prevenir o sobreajuste (*overfitting*), o conjunto de dados deve ser dividido em conjuntos disjuntos antes de qualquer treinamento:

```
[CONJUNTO TOTAL DE DADOS (100%)]
       |
       +---> TREINO (60% - 70%): Utilizado para estimar os parâmetros beta / podas
       |
       +---> VALIDAÇÃO (15% - 20%): Utilizado para calibrar hiperparâmetros e corte
       |
       +---> TESTE (15% - 20%): Blindado; utilizado para apuração final das métricas
```

### Implementação Reprodutível em R

```r
# Fixar semente para reprodutibilidade científica exata
set.seed(42)

n_total <- nrow(dados)
tx_teste <- 0.20
tx_valid <- 0.20

n_teste <- trunc(n_total * tx_teste)
n_valid <- trunc(n_total * tx_valid)
n_trein <- n_total - n_teste - n_valid

# Amostragem sem reposição
idx_todos <- 1:n_total
idx_teste <- sample(idx_todos, size = n_teste, replace = FALSE)

resto <- setdiff(idx_todos, idx_teste)
idx_valid <- sample(resto, size = n_valid, replace = FALSE)

idx_trein <- setdiff(resto, idx_valid)

# Partições finais
dados_treino <- dados[idx_trein, ]
dados_valid  <- dados[idx_valid, ]
dados_teste  <- dados[idx_teste, ]
```

Esse preparo rigoroso assegura estimativas confiáveis das [[Métricas de Avaliação de Modelos]] em tarefas de [[Regressão Linear]], [[Regressão Logística]] e [[Árvores de Decisão]].
