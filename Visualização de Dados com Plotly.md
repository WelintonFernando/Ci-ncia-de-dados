---
aliases:
  - Visualização de Dados
  - Plotly
  - Visualização com Plotly
  - Gráficos Interativos
tags:
  - visualizacao
  - plotly
  - obsidian
  - data-science
---

# Visualização de Dados com Plotly

A **Visualização de Dados** é uma das competências centrais em [[Fundamentos de Ciência de Dados]] e [[Business Intelligence e Análise de Negócios]]. Trata-se da disciplina encarregada de converter dados numéricos tabulares em representações visuais intuitivas, aproveitando a capacidade perceptual do cérebro humano para discernir padrões, tendências temporais, agrupamentos (*clusters*) e anomalias (*outliers*) que seriam imperceptíveis em tabelas puras.

Tradicionalmente, a análise estatística em [[Introdução ao R|R]] utiliza saídas gráficas estáticas geradas pelos motores `base graphics` ou `ggplot2`. Embora excelentes para artigos impressos, gráficos estáticos são limitados na exploração analítica de dados de alta dimensionalidade. O **Plotly** revoluciona essa experiência ao renderizar gráficos dinâmicos e **totalmente interativos**, habilitando recursos nativos de zoom, deslocamento (*pan*), inspeção de detalhes ao passar o cursor (*hover tooltips*) e seleção de subconjuntos de dados.

No ambiente Obsidian, o plugin `obsidian-plotly` permite incorporar gráficos interativos diretamente nas notas de documentação por meio de blocos de código com sintaxe declarativa em YAML.

---

## 1. Princípios da Comunicação Visual de Dados

A construção de representações visuais eficazes fundamenta-se nos princípios teóricos da **Gramática dos Gráficos** (*The Grammar of Graphics*, Leland Wilkinson) e na relação tinta-dado (*Data-Ink Ratio*, Edward Tufte):

- **Foco no Sinal**: Maximizar a proporção de elementos visuais dedicados a transmitir informação genuína, eliminando decorações cosméticas desnecessárias (*chartjunk*).
- **Adequação Geométrica ao Tipo de Variável**:
  - Variáveis contínuas $\times$ contínuas $\implies$ Gráficos de dispersão (*Scatter plots*) e linhas de tendência;
  - Variáveis categóricas $\times$ contínuas $\implies$ Gráficos de barras agrupadas e diagramas de caixa (*Boxplots*);
  - Distribuição univariada contínua $\implies$ Histogramas e curvas de densidade;
  - Matrizes de contingência e correlação $\implies$ Mapas de calor (*Heatmaps*).
- **Interatividade como Instrumento de Descoberta**: Permitir ao cientista isolar categorias clicando na legenda e inspecionar coordenadas exatas sem poluir o gráfico com rótulos estáticos.

---

## 2. Como Funciona o Plotly no Obsidian

O plugin interpreta blocos de código delimitados pela tag `plotly`. O conteúdo é estruturado em formato **YAML** (ou JSON) e contém três chaves principais:

```yaml
```plotly
data:
  - x: [1, 2, 3]
    y: [10, 20, 15]
    type: scatter
    mode: lines+markers
    name: 'Série Exemplo'
layout:
  title: 'Título do Gráfico'
  xaxis:
    title: 'Eixo Horizontal'
  yaxis:
    title: 'Eixo Vertical'
```
```

- **`data`**: Uma lista de objetos (*traces*), onde cada elemento define uma série geométrica de dados (tipo de gráfico, coordenadas $x$ e $y$, cores, espessuras e marcadores).
- **`layout`**: Controla as propriedades visuais da moldura do gráfico (título principal, formatação e títulos dos eixos, tamanho das fontes, legendas, dimensões e anotações).
- **`config`** *(opcional)*: Controla o comportamento dos controles interativos da barra de ferramentas (modo responsivo, permissões de zoom e exportação como PNG).

---

## 3. Exemplos Práticos Interativos de Ciência de Dados

A seguir, apresentamos gráficos interativos completos que ilustram conceitos dos demais tópicos do curso:

---

### 3.1. Gráfico de Dispersão com Reta de Regressão Linear
Ilustra o ajuste dos Mínimos Quadrados Ordinários (OLS) de [[Regressão Linear]] simples para estimar o `peso` (kg) a partir da `altura` (m):

```plotly
data:
  - x: [1.47, 1.50, 1.52, 1.55, 1.57, 1.60, 1.63, 1.65, 1.68, 1.70, 1.73, 1.75, 1.78, 1.80, 1.83]
    y: [52.2, 53.1, 54.5, 55.8, 57.2, 58.7, 60.1, 61.5, 63.2, 64.6, 66.4, 67.9, 69.8, 71.5, 73.4]
    type: scatter
    mode: markers
    name: 'Observações Reais'
    marker:
      color: '#1f77b4'
      size: 9
  - x: [1.45, 1.85]
    y: [49.53, 74.07]
    type: scatter
    mode: lines
    name: 'Ajuste OLS: peso = -39.4 + 61.4*altura'
    line:
      color: '#ff7f0e'
      width: 2.5
layout:
  title: 'Regressão Linear Simples: Altura versus Peso'
  xaxis:
    title: 'Altura (metros)'
  yaxis:
    title: 'Peso (quilogramas)'
  hovermode: 'closest'
```

---

### 3.2. Heatmap Interativo: Matriz de Confusão
Visualização bidimensional com gradiente térmico da **Matriz de Confusão** do modelo de concessão de crédito discutido em [[Regressão Logística]] e [[Métricas de Avaliação de Modelos]]:

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
  title: 'Matriz de Confusão: Modelo de Concessão de Empréstimo'
  xaxis:
    title: 'Classificação do Modelo'
  yaxis:
    title: 'Situação Real do Cliente'
```

- **Célula $[0, 0]$**: $15$ Verdadeiros Negativos ($TN$);
- **Célula $[0, 1]$**: $1$ Falso Positivo ($FP$ — Erro Tipo I);
- **Célula $[1, 0]$**: $2$ Falsos Negativos ($FN$ — Erro Tipo II);
- **Célula $[1, 1]$**: $43$ Verdadeiros Positivos ($TP$).

---

### 3.3. Boxplot Comparativo de Classes
O diagrama de caixa (*boxplot*) é ideal para analisar a separação de variáveis entre classes antes de treinar classificadores como [[Regressão Logística]] e [[Árvores de Decisão]]. O exemplo abaixo compara a distribuição de escore de crédito (`pont_credito`) entre tomadores com empréstimo aprovado versus rejeitado:

```plotly
data:
  - y: [580, 590, 610, 620, 630, 640, 645, 650, 655, 660, 670, 680]
    type: box
    name: 'Empréstimo Recusado (Classe 0)'
    marker:
      color: '#d62728'
  - y: [680, 700, 710, 715, 720, 730, 740, 750, 760, 780, 790, 810, 830, 850]
    type: box
    name: 'Empréstimo Aprovado (Classe 1)'
    marker:
      color: '#2ca02c'
layout:
  title: 'Distribuição do Escore de Crédito por Status do Empréstimo'
  yaxis:
    title: 'Pontuação de Crédito'
```

Passe o cursor sobre os diagramas para inspecionar os valores exatos de mínimo, 1º quartil ($Q_1$), mediana ($Q_2$), 3º quartil ($Q_3$) e máximo de cada classe!

---

### 3.4. Gráfico de Barras Agrupadas: Comparação de Modelos Preditivos
Compara simultaneamente as métricas de [[Acurácia]], [[Precisão]], [[Recall]] e [[F1-Score]] apuradas entre três algoritmos distintos aplicados sobre o mesmo conjunto de validação:

```plotly
data:
  - x: ['Acurácia', 'Precisão', 'Recall', 'F1-Score']
    y: [0.74, 0.65, 0.70, 0.67]
    type: bar
    name: 'Modelo Baseline'
    marker:
      color: '#7f7f7f'
  - x: ['Acurácia', 'Precisão', 'Recall', 'F1-Score']
    y: [0.95, 0.98, 0.96, 0.97]
    type: bar
    name: 'Regressão Logística'
    marker:
      color: '#1f77b4'
  - x: ['Acurácia', 'Precisão', 'Recall', 'F1-Score']
    y: [0.93, 0.94, 0.95, 0.94]
    type: bar
    name: 'Árvore de Decisão Podada'
    marker:
      color: '#2ca02c'
layout:
  title: 'Comparativo de Desempenho entre Modelos Preditivos'
  barmode: 'group'
  yaxis:
    title: 'Pontuação da Métrica (0 a 1)'
    range: [0, 1.05]
```

---

## 4. Integração do R com o Plotly

No ambiente de script em [[Introdução ao R|R]] ou no [[Ambiente de Desenvolvimento Jupyter]], é possível criar gráficos interativos diretamente via biblioteca oficial `plotly` ou convertendo gráficos construídos em `ggplot2`:

```r
# Instalação e carga
install.packages("plotly")
library(plotly)
library(ggplot2)

# Abordagem 1: Sintaxe nativa do plot_ly
p1 <- plot_ly(data = iris, x = ~Sepal.Length, y = ~Petal.Length, 
              color = ~Species, type = 'scatter', mode = 'markers')
p1

# Abordagem 2: Conversão automática de ggplot2 para Plotly interativo
g <- ggplot(dados_cepagri, aes(x = horario, y = temperatura)) +
  geom_line(color = "steelblue") +
  labs(title = "Série Temporal de Temperatura", x = "Tempo", y = "Temperatura (°C)")

# Transforma em widget interativo com zoom e hover tooltips
ggplotly(g)
```

Essa versatilidade fecha o ciclo entre a exploração interativa de modelos no laboratório e a entrega de painéis executivos em [[Business Intelligence e Análise de Negócios]].
