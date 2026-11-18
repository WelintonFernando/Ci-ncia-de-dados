---
aliases:
  - Exercícios de Gráficos
  - Caderno de Exercícios de Interpretação
  - 45 Exercícios de Modelos
  - Simulado de Interpretação de Dados
tags:
  - exercicios
  - simulado
  - graficos
  - interpretacao
  - data-science
  - modelos
---

# Caderno de Exercícios: Interpretação de Gráficos e Tomada de Decisão em Modelos

Este simulado contém **45 exercícios práticos** elaborados especificamente para treinar a leitura de saídas visuais, o raciocínio estatístico e a justificativa técnica de intervenções em modelos de Ciência de Dados. 

Nenhuma questão exige a digitação de código na linguagem R; o foco é **100% interpretação visual, análise de trade-offs de desempenho e fundamentação de ações corretivas**.

As questões estão organizadas em três blocos de complexidade:
* **Nível Fundamental (Exercícios 01 a 15)**: Leitura anatômica direta, sinais, escalas e métricas básicas.
* **Nível Intermediário (Exercícios 16 a 30)**: Diagnóstico de premissas, trade-offs entre métricas e leitura conjunta de múltiplos atributos.
* **Nível Avançado (Exercícios 31 a 45)**: Justificativa de ações em cenários reais de negócio, casos críticos de resíduos e generalização de modelos.

> [!TIP]
> Tente resolver cada exercício individualmente antes de consultar a seção de orientações. No fim desta página, há uma **Seção de Dicas (Dicas 01 a 45)** que apontam o caminho de raciocínio sem entregar a resposta final. Para o gabarito completo e detalhado passo a passo, acesse: [[Resoluções e Gabarito Comentado - Exercícios de Gráficos]].

---

## 🟢 Bloco 1: Nível Fundamental (Exercícios 01 a 15)

### Exercício 01: Anatomia do Box-plot

```plotly
data:
  - y: [1800, 2500, 3200, 4000, 4800, 5500, 6500, 7500, 8800, 10000, 11500, 14000, 18500, 21000, 24500]
    type: box
    name: 'Distribuição Salarial'
    boxpoints: 'outliers'
    marker:
      color: '#1f77b4'
      size: 8
layout:
  title: 'Box-plot: Distribuição de Salários (R$)'
  yaxis:
    title: 'Salário Mensal (R$)'
```

Ao analisar o box-plot da distribuição de salários de uma empresa de tecnologia exibido acima, você observa que a linha central no interior da caixa está na marca de $R\$ 6.500$, a borda inferior da caixa marca $R\$ 4.000$ e a borda superior marca $R\$ 10.000$. 
1. Qual é o valor da mediana e qual é o valor do Intervalo Interquartil ($IQR$)?
2. O que representa, em termos percentuais de funcionários, o intervalo entre $R\$ 4.000$ e $R\$ 10.000$?

---

### Exercício 02: Detecção de Outliers pelo Critério de Tukey
Considerando os mesmos dados e o gráfico do Exercício 01 ($Q_1 = 4.000$ e $Q_3 = 10.000$):
* A partir de qual salário um colaborador será classificado formalmente como um *outlier* superior no diagrama de caixa? Mostre a fórmula de cálculo da cerca superior e verifique se os pontos de $R\$ 21.000$ e $R\$ 24.500$ no gráfico acima são de fato outliers.

---

### Exercício 03: Leitura de Reta de Regressão Linear Simples

```plotly
data:
  - x: [2, 3, 5, 6, 8, 10, 11, 13, 15, 16, 18, 20]
    y: [40, 42, 51, 50, 58, 63, 67, 72, 75, 82, 84, 92]
    type: scatter
    mode: markers
    name: 'Alunos Observados'
    marker:
      color: '#1f77b4'
      size: 9
  - x: [0, 22]
    y: [35, 96.6]
    type: scatter
    mode: lines
    name: 'Reta OLS: ŷ = 35 + 2.8*X'
    line:
      color: '#ff7f0e'
      width: 2.5
layout:
  title: 'Regressão Linear: Tempo de Estudo vs Nota Final'
  xaxis:
    title: 'Horas Semanais de Estudo (X)'
    range: [-1, 23]
  yaxis:
    title: 'Nota Final (0 a 100) (Y)'
    range: [25, 105]
  hovermode: 'closest'
```

No gráfico de dispersão acima, que correlaciona o tempo de estudo semanal ($X$, em horas) e a nota final em uma disciplina de exatas ($Y$, de 0 a 100), a reta ajustada possui a equação:
$$\hat{Y} = 35 + 2,8 \cdot X$$
1. Como se interpreta rigorosamente o valor $35$ nessa situação empírica?
2. Se um aluno aumentar sua dedicação semanal de estudo em $5$ horas, qual é o impacto esperado em sua nota final?

---

### Exercício 04: Resíduo Amostral em Ponto Específico

```plotly
data:
  - x: [2, 3, 5, 6, 8, 10, 11, 13, 15, 16, 18, 20]
    y: [40, 42, 51, 50, 58, 70, 67, 72, 75, 82, 84, 92]
    type: scatter
    mode: markers
    name: 'Alunos Observados'
    marker:
      color: '#1f77b4'
      size: 8
  - x: [0, 22]
    y: [35, 96.6]
    type: scatter
    mode: lines
    name: 'Reta OLS: ŷ = 35 + 2.8*X'
    line:
      color: '#ff7f0e'
      width: 2
  - x: [10]
    y: [70]
    type: scatter
    mode: markers
    name: 'Aluno Alvo (X=10, Y=70)'
    marker:
      color: '#2ca02c'
      size: 13
      symbol: 'diamond'
  - x: [10, 10]
    y: [63, 70]
    type: scatter
    mode: lines
    name: 'Resíduo e = +7'
    line:
      color: '#2ca02c'
      dash: dash
      width: 3
layout:
  title: 'Destaque de Resíduo Amostral: Aluno com X = 10 e Y = 70'
  xaxis:
    title: 'Horas Semanais de Estudo'
  yaxis:
    title: 'Nota Final'
```

Ainda com base no modelo dos Exercícios 03 e 04 ($\hat{Y} = 35 + 2,8 \cdot X$), o gráfico acima destaca um estudante específico que estudou $10$ horas semanais e obteve nota real $Y = 70$ (ponto em verde).
* Calcule o resíduo amostral ($e_i$) desse aluno e explique se o modelo superestimou ou subestimou o seu rendimento.

---

### Exercício 05: Interpretação de Gráfico de Correlação (Heatmap)

```plotly
data:
  - z:
      - [ 1.00,  0.74,  0.15]
      - [ 0.74,  1.00, -0.08]
      - [ 0.15, -0.08,  1.00]
    x: ['Idade', 'Pressão Sistólica', 'Horas de Sono']
    y: ['Idade', 'Pressão Sistólica', 'Horas de Sono']
    type: heatmap
    colorscale: 'Blues'
    showscale: true
    zmin: -1
    zmax: 1
layout:
  title: 'Matriz de Correlação: Indicadores Clínicos'
```

Ao inspecionar o mapa de calor de correlação de Pearson acima entre a variável *Pressão Arterial Sistólica* e *Idade*, o valor exibido na célula de cruzamento é $+0,74$.
* Explique a direção e a intensidade dessa relação linear. O que ocorre com a pressão arterial esperada à medida que a idade avança?

---

### Exercício 06: Correlação Nula versus Ausência de Relação

```plotly
data:
  - x: [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
    y: [25, 16, 9, 4, 1, 0, 1, 4, 9, 16, 25]
    type: scatter
    mode: markers
    name: 'Relação Quadrática Exata: Y = X²'
    marker:
      color: '#d62728'
      size: 10
  - x: [-5, 5]
    y: [10, 10]
    type: scatter
    mode: lines
    name: 'Reta Linear OLS (r = 0.00)'
    line:
      color: '#7f7f7f'
      dash: dash
      width: 2.5
layout:
  title: 'Relação Perfeita com Correlação de Pearson Nula (r = 0.00)'
  xaxis:
    title: 'Variável X'
  yaxis:
    title: 'Variável Y'
```

Observe o gráfico de dispersão acima. Se o coeficiente de correlação linear de Pearson entre duas variáveis $X$ e $Y$ em um gráfico de calor for rigorosamente $r = 0,00$, podemos afirmar categoricamente que **não existe nenhuma relação** entre $X$ e $Y$? Justifique sua resposta com base na dispersão exibida.

---

### Exercício 07: O Classificador Aleatório na Curva ROC

```plotly
data:
  - x: [0.0, 1.0]
    y: [0.0, 1.0]
    type: scatter
    mode: lines
    name: 'Classificador Avaliado (Diagonal: y = x)'
    line:
      color: '#7f7f7f'
      dash: dash
      width: 3
    fill: tozeroy
    fillcolor: 'rgba(127, 127, 127, 0.2)'
layout:
  title: 'Curva ROC: Modelo sobre a Diagonal de 45°'
  xaxis:
    title: 'Taxa de Falsos Positivos (FPR)'
    range: [-0.02, 1.02]
  yaxis:
    title: 'Taxa de Verdadeiros Positivos (TPR)'
    range: [-0.02, 1.05]
```

Em uma curva ROC gerada para um modelo de diagnóstico clínico exibida acima, a curva do modelo coincide perfeitamente com a diagonal que liga a origem $(0, 0)$ ao ponto $(1, 1)$.
1. Qual é o valor numérico da área sob a curva (AUC) desse modelo?
2. Em termos práticos de decisão clínica, qual é a utilidade desse classificador?

---

### Exercício 08: Ponto Ideal no Espaço ROC

```plotly
data:
  - x: [0.0, 1.0]
    y: [0.0, 1.0]
    type: scatter
    mode: lines
    name: 'Diagonal Aleatória (AUC = 0.5)'
    line:
      color: '#7f7f7f'
      dash: dash
  - x: [0.0]
    y: [1.0]
    type: scatter
    mode: markers
    name: 'Classificador Perfeito'
    marker:
      color: '#2ca02c'
      size: 14
      symbol: 'star'
layout:
  title: 'O Ponto Ideal no Espaço ROC'
  xaxis:
    title: 'Taxa de Falsos Positivos (FPR)'
    range: [-0.05, 1.05]
  yaxis:
    title: 'Taxa de Verdadeiros Positivos (TPR)'
    range: [-0.05, 1.1]
```

Quais são as coordenadas exatas $(X, Y)$ do classificador perfeito assinalado com a estrela verde no plano cartesiano da Curva ROC acima? O que significam essas coordenadas em termos de Sensibilidade ($\text{TPR}$) e Taxa de Alarmes Falsos ($\text{FPR}$)?

---

### Exercício 09: Leitura da Função Logística Sigmoide

```plotly
data:
  - x: [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
    y: [0.007, 0.018, 0.047, 0.119, 0.269, 0.500, 0.731, 0.881, 0.953, 0.982, 0.993]
    type: scatter
    mode: lines
    name: 'Função Sigmoide p(z)'
    line:
      color: '#1f77b4'
      width: 3
  - x: [0]
    y: [0.5]
    type: scatter
    mode: markers
    name: 'Ponto Central (z = 0)'
    marker:
      color: '#d62728'
      size: 11
layout:
  title: 'Mapeamento Logístico: z = 0'
  xaxis:
    title: 'Índice Linear z'
  yaxis:
    title: 'Probabilidade p(z)'
```

Em um modelo de [[Regressão Logística]], para um determinado cliente, a combinação linear dos atributos resultou em um valor $z = 0,00$.
* Utilizando a função sigmoide $\sigma(z) = \frac{1}{1 + e^{-z}}$ e o gráfico acima, qual é a probabilidade predita exata $p(z)$ de o cliente pertencer à classe positiva?

---

### Exercício 10: O Limiar Padrão de Decisão

```plotly
data:
  - x: [-5, -2, -0.08, 0.08, 0, 2, 5]
    y: [0.007, 0.119, 0.48, 0.52, 0.50, 0.881, 0.993]
    type: scatter
    mode: lines
    name: 'Curva Sigmoide'
    line:
      color: '#1f77b4'
  - x: [-5, 5]
    y: [0.5, 0.5]
    type: scatter
    mode: lines
    name: 'Limiar Padrão θ = 0.50'
    line:
      color: '#d62728'
      dash: dash
      width: 2
  - x: [-0.08, 0.08, 0]
    y: [0.48, 0.52, 0.50]
    type: scatter
    mode: markers+text
    name: 'Instâncias A, B e C'
    text: ['A (0.48)', 'B (0.52)', 'C (0.50)']
    textposition: 'top left'
    marker:
      color: ['#1f77b4', '#2ca02c', '#ff7f0e']
      size: 10
layout:
  title: 'Classificação pelo Limiar θ = 0.50'
  xaxis:
    title: 'Combinação Linear z'
  yaxis:
    title: 'Probabilidade Predita p'
```

Se um modelo de Regressão Logística opera sob o limiar estático tradicional $\theta = 0,50$ indicado pela linha tracejada vermelha no gráfico acima, que classificação discreta ($\hat{Y} = 0$ ou $\hat{Y} = 1$) será atribuída a instâncias cujas probabilidades estimadas forem respectivamente: $p_A = 0,48$, $p_B = 0,52$ e $p_C = 0,50$?

---

### Exercício 11: Leitura de Matriz de Confusão

```plotly
data:
  - z:
      - [45, 10]
      - [5, 40]
    x: ['Predito Negativo (0)', 'Predito Positivo (1)']
    y: ['Real Negativo (0)', 'Real Positivo (1)']
    type: heatmap
    colorscale: 'Blues'
    showscale: true
layout:
  title: 'Matriz de Confusão (100 Pacientes)'
  xaxis:
    title: 'Previsão do Teste Clínico'
  yaxis:
    title: 'Condição Real do Paciente'
```

Analise a matriz de confusão gráfica acima, obtida em um teste com $100$ pacientes para detecção de uma patologia:
* Real Positivo: $40$ classificados como Positivo ($TP$) e $5$ classificados como Negativo ($FN$).
* Real Negativo: $10$ classificados como Positivo ($FP$) e $45$ classificados como Negativo ($TN$).
Calcule a **Acurácia global** e a taxa de **Recall** do modelo.

---

### Exercício 12: Identificação do Tipo de Erro
No cenário e na matriz do Exercício 11:
1. Qual é a contagem de **Erros do Tipo I** (Falsos Positivos)? Dê o significado prático para o paciente.
2. Qual é a contagem de **Erros do Tipo II** (Falsos Negativos)? Dê o significado prático para o paciente.

---

### Exercício 13: Escalares no Diagrama Viés-Variância

```plotly
data:
  - x: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    y: [10, 7.2, 5.0, 3.4, 2.2, 1.4, 0.8, 0.4, 0.2, 0.1]
    type: scatter
    mode: lines
    name: 'Viés² (Bias²)'
    line:
      color: '#1f77b4'
      dash: dash
      width: 2.5
  - x: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    y: [0.2, 0.4, 0.8, 1.4, 2.2, 3.4, 5.0, 7.2, 9.8, 13.0]
    type: scatter
    mode: lines
    name: 'Variância (Variance)'
    line:
      color: '#ff7f0e'
      dash: dot
      width: 2.5
  - x: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    y: [11.2, 8.6, 6.8, 5.8, 5.4, 5.8, 6.8, 8.6, 11.0, 14.1]
    type: scatter
    mode: lines
    name: 'Erro Total de Generalização'
    line:
      color: '#d62728'
      width: 3.5
layout:
  title: 'Dilema Viés versus Variância'
  xaxis:
    title: 'Complexidade do Algoritmo (Profundidade / Parâmetros)'
  yaxis:
    title: 'Erro Esperado'
```

No gráfico do *Bias-Variance Tradeoff* exibido acima, o que ocorre com o **Viés** e com a **Variância** à medida que a complexidade de um algoritmo (por exemplo, a profundidade máxima de uma árvore) aumenta da esquerda para a direita?

---

### Exercício 14: Interpretação de R² em Gráficos de Dispersão

```plotly
data:
  - x: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    y: [1.2, 3.8, 2.5, 6.2, 4.1, 7.9, 5.8, 9.5, 7.2, 11.0]
    type: scatter
    mode: markers
    name: 'Modelo 1: R² = 0.45 (Dispersão Aberta)'
    marker:
      color: '#1f77b4'
      size: 9
  - x: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    y: [1.1, 2.1, 2.9, 4.2, 5.0, 5.9, 7.1, 8.0, 8.9, 10.1]
    type: scatter
    mode: markers
    name: 'Modelo 2: R² = 0.92 (Dispersão Compacta)'
    marker:
      color: '#2ca02c'
      size: 9
      symbol: 'square'
  - x: [1, 10]
    y: [1, 10]
    type: scatter
    mode: lines
    name: 'Reta Teórica OLS'
    line:
      color: '#7f7f7f'
      dash: dash
layout:
  title: 'Comparativo Visual de R²: Modelo 1 (0.45) vs Modelo 2 (0.92)'
  xaxis:
    title: 'Variável Preditora X'
  yaxis:
    title: 'Variável Resposta Y'
```

Dois modelos lineares simples são ajustados para o mesmo conjunto de dados e exibidos no gráfico acima. O Modelo 1 apresenta $R^2 = 0,45$ e o Modelo 2 apresenta $R^2 = 0,92$.
* Visualmente, como se diferenciam as nuvens de pontos em relação à reta de regressão entre esses dois modelos?

---

### Exercício 15: Leitura de Gráfico Previsto versus Real

```plotly
data:
  - x: [100, 600]
    y: [100, 600]
    type: scatter
    mode: lines
    name: 'Previsão Perfeita (y = ŷ)'
    line:
      color: '#2ca02c'
      dash: dash
      width: 2
  - x: [150, 250, 300, 450, 200]
    y: [150, 250, 300, 450, 380]
    type: scatter
    mode: markers+text
    name: 'Amostras Avaliadas'
    text: ['', '', '', '', 'Ponto Acima (Real=380, Prev=200)']
    textposition: 'top center'
    marker:
      color: '#1f77b4'
      size: 9
layout:
  title: 'Gráfico Previsto versus Real'
  xaxis:
    title: 'Valor Previsto pelo Modelo (ŷ)'
  yaxis:
    title: 'Valor Real Observado (y)'
```

Em um gráfico de dispersão que plota no eixo horizontal o valor previsto $\hat{Y}$ e no eixo vertical o valor real $Y$, uma linha tracejada diagonal de 45° ($Y = \hat{Y}$) é desenhada.
* O que indica um ponto que se posiciona exatamente sobre essa linha diagonal? E um ponto situado consideravelmente acima da linha (como o ponto destacado com $Y = 380$ e $\hat{Y} = 200$)?

---

## 🟡 Bloco 2: Nível Intermediário (Exercícios 16 a 30)

### Exercício 16: Diagnóstico de Não Linearidade em Gráficos de Resíduos

```plotly
data:
  - x: [100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600]
    y: [-8.2, -3.1, 1.8, 5.2, 7.1, 6.8, 4.9, 1.2, -3.5, -9.1, -16.4]
    type: scatter
    mode: markers
    name: 'Resíduos Amostrais (e = y - ŷ)'
    marker:
      color: '#d62728'
      size: 9
  - x: [80, 620]
    y: [0, 0]
    type: scatter
    mode: lines
    name: 'Linha de Resíduo Nulo (e = 0)'
    line:
      color: '#7f7f7f'
      dash: dash
  - x: [100, 200, 325, 450, 600]
    y: [-8.2, 1.8, 7.1, 1.2, -16.4]
    type: scatter
    mode: lines
    name: 'Tendência Parabólica (U Invertido)'
    line:
      color: '#d62728'
      dash: dot
      width: 2
layout:
  title: 'Diagnóstico de Resíduos vs Ajustados: Curvatura Não Linear'
  xaxis:
    title: 'Valores Ajustados ŷ (Emissão Prevista)'
  yaxis:
    title: 'Resíduos (e)'
```

Ao inspecionar o gráfico de *Resíduos versus Valores Ajustados* ($e_i \times \hat{Y}_i$) exibido acima para um modelo linear simples estimando a emissão de poluentes a partir da rotação do motor, você observa que os pontos formam uma nítida curva parabólica em formato de "U" invertido (resíduos positivos no centro e resíduos negativos nas extremidades).
* Explique qual premissa clássica da regressão linear foi violada e justifique qual modificação estrutural deve ser feita na fórmula do modelo para corrigir o problema.

---

### Exercício 17: Diagnóstico de Heterocedasticidade

```plotly
data:
  - x: [50, 80, 100, 150, 200, 250, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200]
    y: [2, -3, 4, -8, 12, -15, 22, -35, 48, -62, 85, -110, 145, -190, 240, -310]
    type: scatter
    mode: markers
    name: 'Resíduos dos Erros'
    marker:
      color: '#9467bd'
      size: 8
  - x: [30, 1250]
    y: [0, 0]
    type: scatter
    mode: lines
    name: 'Referência e = 0'
    line:
      color: '#7f7f7f'
      dash: dash
  - x: [50, 1200]
    y: [5, 320]
    type: scatter
    mode: lines
    name: 'Envoltória Superior do Leque'
    line:
      color: '#9467bd'
      dash: dot
  - x: [50, 1200]
    y: [-5, -320]
    type: scatter
    mode: lines
    name: 'Envoltória Inferior do Leque'
    line:
      color: '#9467bd'
      dash: dot
layout:
  title: 'Resíduos vs Ajustados: Padrão em Megafone (Heterocedasticidade)'
  xaxis:
    title: 'Valores Ajustados (ŷ)'
  yaxis:
    title: 'Resíduos (e)'
```

No gráfico de resíduos vs ajustados acima, a dispersão vertical dos resíduos é muito estreita quando $\hat{Y} < 100$, mas vai se alargando continuamente até formar um formato de leque ou megafone aberto quando $\hat{Y} > 1.000$.
1. Qual é o nome desse fenômeno estatístico?
2. Qual é o impacto disso sobre os testes de significância estatística ($p$-valores) dos coeficientes?
3. Que transformação matemática na variável dependente é classicamente recomendada para remediar essa patologia?

---

### Exercício 18: Comparação Visual de Dois Modelos na Curva ROC

```plotly
data:
  - x: [0.0, 0.05, 0.10, 0.20, 0.35, 0.50, 0.70, 0.85, 1.0]
    y: [0.0, 0.65, 0.85, 0.92, 0.95, 0.97, 0.99, 1.0, 1.0]
    type: scatter
    mode: lines+markers
    name: 'Modelo Alfa (Superior)'
    line:
      color: '#1f77b4'
      width: 3
  - x: [0.0, 0.05, 0.10, 0.20, 0.35, 0.50, 0.70, 0.85, 1.0]
    y: [0.0, 0.35, 0.60, 0.75, 0.82, 0.87, 0.92, 0.96, 1.0]
    type: scatter
    mode: lines+markers
    name: 'Modelo Beta (Inferior)'
    line:
      color: '#ff7f0e'
      width: 2.5
      dash: dot
  - x: [0.0, 1.0]
    y: [0.0, 1.0]
    type: scatter
    mode: lines
    name: 'Aleatório (AUC = 0.50)'
    line:
      color: '#7f7f7f'
      dash: dash
layout:
  title: 'Comparativo de Desempenho ROC: Modelo Alfa vs Beta'
  xaxis:
    title: 'Taxa de Falsos Positivos (FPR)'
  yaxis:
    title: 'Taxa de Verdadeiros Positivos (TPR)'
  hovermode: 'closest'
```

No plano cartesiano ROC acima, a curva do Modelo Alfa passa pelos pontos $(FPR=0,10; TPR=0,85)$ e $(FPR=0,20; TPR=0,92)$. A curva do Modelo Beta passa pelos pontos $(FPR=0,10; TPR=0,60)$ e $(FPR=0,20; TPR=0,75)$. Em todos os demais limiares, a curva Alfa mantém-se estritamente acima da curva Beta.
* Qual modelo possui maior AUC? Justifique tecnicamente por que o Modelo Alfa é estocasticamente superior para qualquer política de corte adotada pela empresa.

---

### Exercício 19: Mudança Estratégica de Limiar de Decisão

```plotly
data:
  - x: [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
    y: [0.007, 0.018, 0.047, 0.119, 0.269, 0.500, 0.731, 0.881, 0.953, 0.982, 0.993]
    type: scatter
    mode: lines
    name: 'Probabilidade de Fraude p(z)'
    line:
      color: '#1f77b4'
      width: 3
  - x: [-5, 5]
    y: [0.5, 0.5]
    type: scatter
    mode: lines
    name: 'Limiar Atual θ = 0.50'
    line:
      color: '#7f7f7f'
      dash: dash
  - x: [-5, 5]
    y: [0.15, 0.15]
    type: scatter
    mode: lines
    name: 'Limiar Proposto θ = 0.15 (Segurança Reforçada)'
    line:
      color: '#d62728'
      dash: dot
      width: 2.5
layout:
  title: 'Estratégia de Limiar para Detecção de Fraudes'
  xaxis:
    title: 'Escore de Risco Linear z'
  yaxis:
    title: 'Probabilidade Predita'
```

Um cientista de dados está calibrando um modelo de detecção de transações financeiras fraudulentas via cartão de crédito cujo gráfico de probabilidades é mostrado acima. Atualmente, o limiar de probabilidade está fixado em $\theta = 0,50$. A diretoria de segurança exige que "nenhuma fraude passe sem bloqueio imediato, mesmo que clientes inocentes recebam ligações de verificação".
* Para qual direção o cientista deve deslocar o limiar $\theta$ (aumentar para próximo de $0,85$ ou reduzir para próximo de $0,15$ como indicado pela linha vermelha)? Explique o impacto dessa decisão sobre o **Recall** e a **Precisão**.

---

### Exercício 20: O Paradoxo da Acurácia em Classes Raras

```plotly
data:
  - x: ['Saudáveis (Classe Negativa 0)', 'Doentes (Classe Rara Positiva 1)']
    y: [9950, 50]
    type: bar
    name: 'Contagem Real de Pacientes'
    marker:
      color: ['#1f77b4', '#d62728']
layout:
  title: 'Desbalanceamento Severo de Classes: 9.950 vs 50'
  yaxis:
    title: 'Número Absoluto de Pacientes'
```

Uma base de dados médica ilustrada no gráfico acima contém $10.000$ exames preventivos, dos quais $9.950$ são negativos (saudáveis) e apenas $50$ são positivos para uma condição rara ($0,5\%$). Um modelo baseline ingênuo classifica literalmente todas as $10.000$ pessoas como saudáveis.
1. Qual é a acurácia global desse modelo ingênuo?
2. Qual é o seu Recall para a detecção da doença?
3. Por que o gráfico de acurácia isolada é enganoso e qual métrica gráfica deve ser utilizada para avaliar adequadamente esse classificador?

---

### Exercício 21: Leitura de Box-plots Comparativos e Seleção de Atributos

```plotly
data:
  - y: [35, 38, 42, 45, 48, 52, 55, 60]
    type: box
    name: 'Idade: Fiel (0)'
    marker:
      color: '#1f77b4'
  - y: [34, 37, 41, 44, 49, 53, 56, 61]
    type: box
    name: 'Idade: Churn (1)'
    marker:
      color: '#aec7e8'
  - y: [1, 2, 3, 4, 5, 6, 8, 10]
    type: box
    name: 'Dias s/ Login: Fiel (0)'
    marker:
      color: '#2ca02c'
  - y: [25, 30, 35, 40, 45, 50, 60, 90]
    type: box
    name: 'Dias s/ Login: Churn (1)'
    marker:
      color: '#98df8a'
  - y: [50, 60, 70, 80, 90, 100]
    type: box
    name: 'Mensalidade: Fiel (0)'
    marker:
      color: '#ff7f0e'
  - y: [70, 85, 95, 110, 120, 140]
    type: box
    name: 'Mensalidade: Churn (1)'
    marker:
      color: '#ffbb78'
layout:
  title: 'Poder de Separação de Atributos por Status de Churn'
  yaxis:
    title: 'Valores dos Atributos'
```

Você precisa escolher os melhores preditores para alimentar um classificador de *churn*. Analise o gráfico comparativo acima:
* No Atributo A (*Idade*), as caixas dos clientes fiéis e dos que cancelaram possuem medianas idênticas e sobreposição quase total.
* No Atributo B (*Dias desde o último login*), a caixa dos que cancelaram está totalmente deslocada para o topo, com separação nítida em relação aos fiéis.
* No Atributo C (*Mensalidade*), há separação moderada.
Justifique tecnicamente a seleção do Atributo B e o descarte do Atributo A com base na separabilidade geométrica observada.

---

### Exercício 22: Detecção de Multicolinearidade em Matriz de Correlação

```plotly
data:
  - z:
      - [ 1.00,  0.91,  0.35]
      - [ 0.91,  1.00,  0.28]
      - [ 0.35,  0.28,  1.00]
    x: ['Área Útil (m²)', 'Total de Cômodos', 'Idade Imóvel']
    y: ['Área Útil (m²)', 'Total de Cômodos', 'Idade Imóvel']
    type: heatmap
    colorscale: 'Reds'
    showscale: true
    zmin: 0
    zmax: 1
layout:
  title: 'Matriz de Correlação: Diagnóstico de Multicolinearidade'
```

Ao examinar a matriz de correlação de Pearson acima para precificação de imóveis, você nota que a correlação entre *Área Útil em Metros Quadrados* e *Número Total de Cômodos* é de $r = +0,91$.
1. Que complicação estatística surge se você mantiver ambas as variáveis no modelo simultaneamente?
2. Como essa alta correlação afeta os erros-padrão dos coeficientes $\hat{\beta}$ e a interpretação individual de seus impactos?

---

### Exercício 23: Grade de Dispersão e Agrupamentos Naturais

```plotly
data:
  - x: [4.2, 4.4, 4.5, 4.7, 4.8, 5.0, 5.1, 5.2, 4.3, 4.6]
    y: [12, 14, 15, 13, 16, 14, 17, 18, 13, 15]
    type: scatter
    mode: markers
    name: 'Grupo A (Solos Ácidos / Baixo N)'
    marker:
      color: '#1f77b4'
      size: 9
  - x: [7.2, 7.4, 7.5, 7.6, 7.8, 8.0, 8.1, 8.3, 7.5, 7.9]
    y: [45, 48, 52, 50, 55, 58, 54, 60, 49, 53]
    type: scatter
    mode: markers
    name: 'Grupo B (Solos Alcalinos / Alto N)'
    marker:
      color: '#2ca02c'
      size: 9
layout:
  title: 'Dispersão Bivariada: Duas Nuvens com Vazio Intermediário'
  xaxis:
    title: 'pH do Solo'
    range: [3.5, 9.0]
  yaxis:
    title: 'Teor de Nitrogênio (mg/kg)'
    range: [5, 65]
```

Ao inspecionar o gráfico de dispersão acima contendo variáveis químicas de amostras de solo, você percebe que no cruzamento entre *pH* e *Teor de Nitrogênio* os pontos formam **duas nuvens densas e claramente separadas por um grande vazio intermediário**.
* O que essa visualização sugere sobre a natureza dos dados e que tipo de modelagem (não supervisionada ou segmentada) pode ser vantajosa antes de tentar uma regressão linear global?

---

### Exercício 24: Curva de Aprendizado: Diagnóstico de Overfitting

```plotly
data:
  - x: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    y: [0.40, 0.31, 0.23, 0.16, 0.10, 0.06, 0.03, 0.02, 0.015, 0.01]
    type: scatter
    mode: lines+markers
    name: 'Erro de Treino'
    line:
      color: '#1f77b4'
      width: 2.5
  - x: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    y: [0.42, 0.33, 0.25, 0.18, 0.22, 0.28, 0.35, 0.42, 0.49, 0.55]
    type: scatter
    mode: lines+markers
    name: 'Erro de Validação'
    line:
      color: '#d62728'
      width: 3
  - x: [4]
    y: [0.18]
    type: scatter
    mode: markers
    name: 'Mínimo de Validação (Profundidade 4)'
    marker:
      color: '#2ca02c'
      size: 12
      symbol: 'diamond'
layout:
  title: 'Curva de Erro vs Profundidade da Árvore'
  xaxis:
    title: 'Profundidade da Árvore de Decisão'
  yaxis:
    title: 'Erro Médio (MSE)'
```

Ao plotar a curva de evolução do erro quadrático médio ($MSE$) ao longo do aumento da profundidade de uma Árvore de Decisão no gráfico acima:
* O erro no conjunto de **treino** cai monotonicamente de $0,40$ para $0,01$.
* O erro no conjunto de **validação** atinge seu mínimo ($0,18$) na profundidade $4$, mas a partir da profundidade $5$ passa a subir continuamente até $0,55$.
1. Em qual profundidade a árvore atinge seu ápice de generalização?
2. O que está acontecendo com o modelo entre as profundidades $5$ e $10$? Justifique a ação de poda (`prune`).

---

### Exercício 25: Diagnóstico de Underfitting

```plotly
data:
  - x: [500, 1000, 2000, 3000, 4000, 5000, 6000]
    y: [0.68, 0.66, 0.65, 0.65, 0.64, 0.64, 0.64]
    type: scatter
    mode: lines+markers
    name: 'Erro de Treino'
    line:
      color: '#1f77b4'
      width: 2.5
  - x: [500, 1000, 2000, 3000, 4000, 5000, 6000]
    y: [0.72, 0.69, 0.67, 0.66, 0.66, 0.65, 0.65]
    type: scatter
    mode: lines+markers
    name: 'Erro de Validação'
    line:
      color: '#d62728'
      width: 2.5
layout:
  title: 'Diagnóstico de Subajuste (Underfitting Crônico)'
  xaxis:
    title: 'Tamanho da Amostra de Treinamento (N)'
  yaxis:
    title: 'Erro Médio (MSE)'
    range: [0, 1.0]
```

Em outro experimento preditivo exibido no gráfico acima, tanto a curva de erro de treino quanto a de validação permanecem estagnadas em um patamar muito alto ($MSE \approx 0,65$), mesmo após alimentar o modelo com milhares de novas amostras de dados.
* Esse cenário caracteriza alto viés (*underfitting*) ou alta variância (*overfitting*)? Adicionar mais dados de treino resolverá o problema? Qual deve ser a ação técnica recomendada?

---

### Exercício 26: Impacto Visual de Outliers na Reta OLS

```plotly
data:
  - x: [10, 12, 14, 15, 18, 20, 22, 25, 28, 30, 32, 35]
    y: [12, 15, 17, 19, 21, 24, 26, 30, 34, 36, 38, 42]
    type: scatter
    mode: markers
    name: 'Dados Normais (r = 0.85)'
    marker:
      color: '#1f77b4'
      size: 8
  - x: [100]
    y: [0]
    type: scatter
    mode: markers+text
    name: 'Outlier de Alavancagem (100, 0)'
    text: ['Ponto de Alavancagem (100, 0)']
    textposition: 'top left'
    marker:
      color: '#d62728'
      size: 13
      symbol: 'x'
  - x: [8, 40]
    y: [10, 48]
    type: scatter
    mode: lines
    name: 'Reta OLS Sem Outlier (Inclinação Real)'
    line:
      color: '#2ca02c'
      width: 2.5
  - x: [8, 105]
    y: [28, 5]
    type: scatter
    mode: lines
    name: 'Reta OLS Com Outlier (Distorcida)'
    line:
      color: '#d62728'
      dash: dash
      width: 2.5
layout:
  title: 'Efeito de Ponto de Alta Alavancagem na Reta OLS'
  xaxis:
    title: 'Variável X'
  yaxis:
    title: 'Variável Y'
```

No gráfico de dispersão acima, a reta verde representa o ajuste OLS para as observações da massa principal. Quando um único ponto é adicionado nas coordenadas extremas $(X = 100, Y = 0)$, a reta de regressão sofre a distorção representada pela linha vermelha tracejada.
* O que acontecerá visualmente com a inclinação ($\hat{\beta}_1$) da reta de mínimos quadrados ordinários? Por que o método OLS é especialmente sensível a esse ponto de alavancagem?

---

### Exercício 27: Leitura de Gráfico de Barras Agrupadas de Métricas

```plotly
data:
  - x: ['Precisão', 'Recall', 'F1-Score']
    y: [0.95, 0.30, 0.456]
    type: bar
    name: 'Modelo 1 (Precisão Alta, Recall Baixo)'
    marker:
      color: '#1f77b4'
  - x: ['Precisão', 'Recall', 'F1-Score']
    y: [0.72, 0.70, 0.710]
    type: bar
    name: 'Modelo 2 (Equilibrado)'
    marker:
      color: '#2ca02c'
layout:
  title: 'Comparativo de Métricas: Modelo 1 vs Modelo 2'
  barmode: 'group'
  yaxis:
    title: 'Pontuação da Métrica'
    range: [0, 1.05]
```

Um painel apresenta o gráfico de barras agrupadas acima comparando dois modelos em Precisão, Recall e F1-Score:
* O Modelo 1 tem Precisão $= 0,95$ e Recall $= 0,30$.
* O Modelo 2 tem Precisão $= 0,72$ e Recall $= 0,70$.
Calcule mentalmente ou estime qual dos dois modelos terá a barra de **F1-Score** significativamente superior e justifique com base na fórmula da média harmônica.

---

### Exercício 28: A Armadilha da Variável Dummy em Gráficos
Em uma base de dados com uma variável categórica *Região* contendo quatro categorias mutuamente exclusivas: Norte, Sul, Leste e Oeste. Um analista cria quatro colunas binárias ($D_{\text{Norte}}, D_{\text{Sul}}, D_{\text{Leste}}, D_{\text{Oeste}}$) e insere as quatro simultaneamente em uma regressão linear múltipla com intercepto.
* Por que a matriz de dispersão ou o algoritmo computacional de inversão de matrizes $(\mathbf{X}^T \mathbf{X})^{-1}$ emitirá um erro de colinearidade perfeita? Qual é a regra fundamental para inclusão de variáveis dummy?

---

### Exercício 29: Inspeção de Normalidade dos Resíduos (Q-Q Plot)

```plotly
data:
  - x: [-3, 3]
    y: [-3, 3]
    type: scatter
    mode: lines
    name: 'Reta Normal Teórica'
    line:
      color: '#7f7f7f'
      dash: dash
  - x: [-2.5, -2.0, -1.5, -1.0, -0.5, 0.0, 0.5, 1.0, 1.5, 2.0, 2.5]
    y: [-4.2, -3.1, -1.6, -1.0, -0.4, 0.0, 0.4, 1.0, 1.7, 3.2, 4.5]
    type: scatter
    mode: markers
    name: 'Quantis Amostrais (Padrão S)'
    marker:
      color: '#d62728'
      size: 8
layout:
  title: 'Normal Q-Q Plot: Desvio em S nas Caudas'
  xaxis:
    title: 'Quantis Teóricos da Normal'
  yaxis:
    title: 'Resíduos Padronizados Amostrais'
```

Em um gráfico de probabilidade normal (Normal Q-Q Plot) exibido acima, os resíduos padronizados são plotados contra os quantis teóricos da distribuição Gaussiana padrão.
* Como os pontos se desviam fortemente da reta diagonal nas duas extremidades (formando um desenho em "S" com caudas pesadas para fora), o que isso revela sobre a premissa de normalidade dos resíduos do modelo linear?

---

### Exercício 30: Efeito da Padronização Z-Score em Gráficos

```plotly
data:
  - x: [-1.41, -0.71, 0.0, 0.71, 1.41]
    y: [-1.41, -0.71, 0.0, 0.71, 1.41]
    type: scatter
    mode: markers
    name: 'Dados Padronizados Z (Média=0, DP=1)'
    marker:
      color: '#1f77b4'
      size: 10
layout:
  title: 'Dispersão Centralizada na Origem (0, 0) via Z-Score'
  xaxis:
    title: 'Z(Altura)'
    range: [-3, 3]
  yaxis:
    title: 'Z(Peso)'
    range: [-3, 3]
```

Ao converter os atributos de uma base de dados para a escala $Z$-score ($z = \frac{x - \mu}{\sigma}$) como demonstrado no gráfico acima, o que acontece visualmente com o centro do gráfico de dispersão e com a dispersão relativa dos pontos em comparação com a variável original não padronizada? A forma geométrica da correlação é alterada?

---

## 🔴 Bloco 3: Nível Avançado e Decisão Estratégica (Exercícios 31 a 45)

### Exercício 31: Justificativa de Termo Polinomial em Dataset de Saúde

```plotly
data:
  - x: [51.2, 53.0, 54.2, 56.0, 57.2, 59.0, 60.8, 62.0, 63.7, 64.9, 66.7, 67.9, 69.7, 70.9, 72.7]
    y: [0.97, 0.08, 0.29, -0.20, 0.01, -0.28, -0.66, -0.45, -0.54, -0.33, -0.32, -0.01, 0.10, 0.61, 0.73]
    type: scatter
    mode: markers
    name: 'Resíduos Modelo Linear (women)'
    marker:
      color: '#d62728'
      size: 9
  - x: [50, 74]
    y: [0, 0]
    type: scatter
    mode: lines
    name: 'Resíduo Zero (e = 0)'
    line:
      color: '#7f7f7f'
      dash: dash
  - x: [51.2, 55, 61, 67, 72.7]
    y: [0.97, 0.0, -0.66, 0.0, 0.73]
    type: scatter
    mode: lines
    name: 'Curvatura Parabólica em U'
    line:
      color: '#d62728'
      dash: dot
      width: 2
layout:
  title: 'Diagnóstico de Resíduos: Dataset women (R² = 0.991)'
  xaxis:
    title: 'Valores Ajustados ŷ (Peso Estimado em kg)'
  yaxis:
    title: 'Resíduos Amostrais (e = y - ŷ)'
```

Considere o estudo com o dataset `women` visto no curso e ilustrado no gráfico de resíduos acima, onde foi ajustada inicialmente a regressão linear simples $\text{peso} = -39,4 + 61,4 \cdot \text{altura}$. O modelo obteve $R^2 = 0,9910$. Apesar desse $R^2$ aparentemente excelente, o professor afirma que o modelo está matematicamente inadequado e exige uma intervenção.
1. Que evidência visual no gráfico de resíduos sustenta rigorosamente a afirmação do professor?
2. Ao adicionar o termo quadrático $\text{altura}^2$, o $MSE$ caiu de $0,401$ para $0,024$ (redução de mais de $94\%$). Justifique por que um $R^2$ alto não é garantia de suficiência de um modelo linear.

---

### Exercício 32: Calibração de Corte em Custos Assimétricos (Fraude Bancária)

```plotly
data:
  - x: [0.0, 0.02, 0.08, 0.15, 0.25, 0.40, 0.60, 0.80, 1.0]
    y: [0.0, 0.80, 0.98, 0.99, 0.995, 0.998, 1.0, 1.0, 1.0]
    type: scatter
    mode: lines
    name: 'Curva ROC do Modelo de Fraude'
    line:
      color: '#1f77b4'
      width: 2.5
  - x: [0.02]
    y: [0.80]
    type: scatter
    mode: markers+text
    name: 'Ponto 1: θ = 0.50'
    text: ['θ = 0.50 (FPR=0.02, TPR=0.80)']
    textposition: 'bottom right'
    marker:
      color: '#ff7f0e'
      size: 11
  - x: [0.08]
    y: [0.98]
    type: scatter
    mode: markers+text
    name: 'Ponto 2: θ = 0.10'
    text: ['θ = 0.10 (FPR=0.08, TPR=0.98)']
    textposition: 'top left'
    marker:
      color: '#2ca02c'
      size: 13
      symbol: 'star'
layout:
  title: 'Curva ROC: Escolha de Ponto Operacional sob Custos Assimétricos'
  xaxis:
    title: 'Taxa de Falsos Positivos (FPR)'
    range: [-0.01, 0.35]
  yaxis:
    title: 'Taxa de Verdadeiros Positivos (TPR)'
    range: [0.65, 1.05]
```

Um banco digital processa $500.000$ pagamentos diários. A perda financeira média de uma transação fraudulenta não detectada ($FN$) é de $R\$ 3.200,00$. O custo operacional de checar um falso alarme ($FP$), enviando uma notificação por SMS para o cliente confirmar a compra, é de apenas $R\$ 0,50$.
* Analisando a curva ROC do modelo de fraude no gráfico acima, a gerência debate se deve escolher o ponto com limiar $\theta = 0,50$ ($\text{TPR}=0,80; \text{FPR}=0,02$) ou o ponto com limiar $\theta = 0,10$ ($\text{TPR}=0,98; \text{FPR}=0,08$).
Fundamente tecnicamente qual ponto operacional deve ser implementado, demonstrando a assimetria brutal entre os custos dos dois tipos de erro.

---

### Exercício 33: Escolha entre Normalização Min-Max e Padronização Z-score

```plotly
data:
  - y: [14.2, 16.5, 18.1, 19.4, 21.0, 22.5, 23.8, 25.1, 26.7, 28.3, 30.2, 32.0, 99.9, 99.9]
    type: box
    name: 'Série de Temperatura Bruta CEPAGRI'
    boxpoints: 'outliers'
    marker:
      color: '#d62728'
      size: 8
layout:
  title: 'Box-plot de Temperatura com Código Sentinela de Falha (99.9°C)'
  yaxis:
    title: 'Temperatura Registrada (°C)'
```

Um engenheiro de dados recebe a série temporal climática do CEPAGRI ilustrada no box-plot acima, contendo registros de temperatura do ar com alguns picos espúrios de $+99,9^\circ\text{C}$ decorrentes de falhas de hardware no sensor. Ele precisa escalar a variável antes de alimentar um algoritmo sensível à escala.
* O que acontecerá com todas as observações reais válidas (que variam tipicamente entre $10^\circ\text{C}$ e $35^\circ\text{C}$) se ele aplicar cegamente a **Normalização Min-Max** ($x_{\text{norm}} = \frac{x - x_{\min}}{x_{\max} - x_{\min}}$) antes de expurgar o valor $99,9$? Justifique por que o Z-score ou a limpeza prévia são mandatórios.

---

### Exercício 34: Trade-off na Poda de Árvores de Decisão (Custo-Complexidade)

```plotly
data:
  - x: [1, 2, 3, 4, 5, 6, 7, 8]
    y: [1.00, 0.65, 0.42, 0.31, 0.28, 0.27, 0.29, 0.33]
    type: scatter
    mode: lines+markers
    name: 'Erro de Validação Cruzada (x-error)'
    line:
      color: '#1f77b4'
      width: 2.5
  - x: [1, 8]
    y: [0.32, 0.32]
    type: scatter
    mode: lines
    name: 'Linha Limiar: 1-SE Rule'
    line:
      color: '#d62728'
      dash: dash
      width: 2
  - x: [4]
    y: [0.31]
    type: scatter
    mode: markers+text
    name: 'Árvore Mais Simples dentro de 1-SE'
    text: ['Árvore Ótima Podada (Tamanho 4)']
    textposition: 'bottom center'
    marker:
      color: '#2ca02c'
      size: 12
      symbol: 'star'
  - x: [6]
    y: [0.27]
    type: scatter
    mode: markers+text
    name: 'Mínimo Absoluto Pontual (Tamanho 6)'
    text: ['Mínimo Numérico (Tamanho 6)']
    textposition: 'bottom right'
    marker:
      color: '#ff7f0e'
      size: 10
layout:
  title: 'Gráfico de Complexidade de Custo e Regra de 1-SE'
  xaxis:
    title: 'Tamanho da Árvore / Número de Folhas'
  yaxis:
    title: 'Erro Relativo de Validação Cruzada'
```

No gráfico de complexidade de custo (`plotcp` em R) exibido acima, o eixo horizontal plota o tamanho da árvore e o eixo vertical plota o erro de validação cruzada (*x-error*), acompanhado da linha horizontal pontilhada vermelha que representa o limiar da **Regra de 1 Erro-Padrão (1-SE Rule)**.
1. Por que a literatura e as boas práticas de modelagem recomendam escolher a árvore mais simples cujo erro esteja abaixo da linha de 1-SE (tamanho 4), em vez de simplesmente escolher a árvore com o menor erro numérico absoluto (tamanho 6)?
2. O que essa decisão visa preservar no modelo final?

---

### Exercício 35: Análise Gráfica de Resíduos em Dados Temporais (Autocorrelação)

```plotly
data:
  - x: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    y: [4.2, 5.1, 4.8, 3.2, 1.1, -1.5, -3.8, -4.6, -4.9, -3.1, -0.8, 1.6, 3.9, 4.8, 5.2, 3.8, 1.2, -1.8, -3.9, -4.5]
    type: scatter
    mode: lines+markers
    name: 'Resíduos ao Longo do Tempo (Dias)'
    line:
      color: '#d62728'
      width: 2.5
  - x: [1, 20]
    y: [0, 0]
    type: scatter
    mode: lines
    name: 'Linha Zero'
    line:
      color: '#7f7f7f'
      dash: dash
layout:
  title: 'Diagnóstico Temporal: Resíduos com Autocorrelação Positiva'
  xaxis:
    title: 'Sequência Cronológica (Dias)'
  yaxis:
    title: 'Resíduo Amostral (e)'
```

Ao plotar os resíduos de um modelo de previsão de demanda ao longo do tempo no gráfico acima, você percebe que resíduos positivos tendem a ser seguidos por longas sequências de resíduos positivos, e resíduos negativos tendem a ser seguidos por longas sequências de resíduos negativos (padrão cíclico ondulatório).
1. Qual premissa do Teorema de Gauss-Markov está sendo violada?
2. Qual teste estatístico clássico diagnostica esse padrão e qual é o perigo de ignorá-lo ao calcular intervalos de confiança?

---

### Exercício 36: Interpretação de Odds Ratio na Regressão Logística

```plotly
data:
  - x: [0, 5, 10, 15, 20, 25]
    y: [1.0, 1.83, 3.37, 6.17, 11.3, 20.8]
    type: scatter
    mode: lines+markers
    name: 'Multiplicador das Chances: exp(0.1214 * ΔX)'
    line:
      color: '#1f77b4'
      width: 3
    marker:
      size: 9
  - x: [10]
    y: [3.37]
    type: scatter
    mode: markers+text
    name: 'ΔX = 10 (Chances x 3.37)'
    text: ['ΔX = 10 (Fator = 3.37)']
    textposition: 'top left'
    marker:
      color: '#d62728'
      size: 13
      symbol: 'diamond'
layout:
  title: 'Crescimento da Razão de Chances (Odds Ratio) com o Escore'
  xaxis:
    title: 'Acréscimo na Pontuação de Crédito (ΔX)'
  yaxis:
    title: 'Fator Multiplicativo nas Chances (Odds Ratio)'
```

Em um modelo de concessão de crédito univariado usando a pontuação de crédito (`pont_credito`), a saída do modelo indicou um coeficiente angular $\hat{\beta}_1 = 0,1214$, cujo comportamento multiplicativo nas chances é traçado no gráfico acima.
1. Como se converte esse coeficiente da escala linear (logit) para a escala multiplicativa de **Razão de Chances (*Odds Ratio*)**? Calcule $e^{0,1214}$.
2. Se um cliente aumentar seu escore em $10$ pontos (ponto destacado no gráfico), qual será o impacto percentual multiplicativo em suas chances relativas de ter o empréstimo aprovado?

---

### Exercício 37: Leitura de Gráfico de Sensibilidade vs Especificidade

```plotly
data:
  - x: [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.52, 0.6, 0.7, 0.8, 0.9, 1.0]
    y: [1.0, 0.98, 0.94, 0.88, 0.80, 0.73, 0.71, 0.62, 0.48, 0.32, 0.15, 0.0]
    type: scatter
    mode: lines
    name: 'Sensibilidade / Recall (TPR)'
    line:
      color: '#1f77b4'
      width: 3
  - x: [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.52, 0.6, 0.7, 0.8, 0.9, 1.0]
    y: [0.0, 0.20, 0.38, 0.52, 0.63, 0.70, 0.71, 0.78, 0.86, 0.93, 0.98, 1.0]
    type: scatter
    mode: lines
    name: 'Especificidade (TNR)'
    line:
      color: '#2ca02c'
      width: 3
  - x: [0.52]
    y: [0.71]
    type: scatter
    mode: markers+text
    name: 'Ponto de Equilíbrio (θ* = 0.52)'
    text: ['Interseção (θ* = 0.52, Sens = Espec = 71%)']
    textposition: 'top center'
    marker:
      color: '#d62728'
      size: 13
      symbol: 'x'
layout:
  title: 'Curvas Cruzadas de Sensibilidade versus Especificidade'
  xaxis:
    title: 'Limiar de Corte de Probabilidade (θ)'
  yaxis:
    title: 'Valor da Métrica (0 a 1)'
```

No gráfico de curvas cruzadas acima, que plota no eixo horizontal o limiar de probabilidade ($\theta \in [0, 1]$) e no eixo vertical o valor das métricas, a curva de **Sensibilidade (Recall)** e a de **Especificidade** cruzam-se no ponto assinalado em vermelho.
* O que representa o ponto geométrico de interseção exato entre as duas curvas? Em que contexto operacional esse limiar específico é considerado uma escolha equilibrada razoável?

---

### Exercício 38: Avaliação de Modelo em Potabilidade da Água (`Water Quality`)

```plotly
data:
  - z:
      - [54, 46]
      - [12, 88]
    x: ['Predito Não Potável (0)', 'Predito Potável (1)']
    y: ['Real Não Potável (0)', 'Real Potável (1)']
    type: heatmap
    colorscale: 'Reds'
    showscale: true
layout:
  title: 'Matriz de Confusão em %: Modelo de Potabilidade da Água'
  xaxis:
    title: 'Previsão do Algoritmo'
  yaxis:
    title: 'Condição Real da Amostra'
```

No conjunto de dados de qualidade da água do curso, o objetivo é prever a potabilidade ($Y=1$ para água segura, $Y=0$ para água contaminada). A matriz de confusão percentual do modelo logístico é apresentada acima:
* Acurácia: $73\%$
* Recall da classe 1 (Potável): $88\%$
* Especificidade (Recall da classe 0 - Não Potável): $54\%$ (ou seja, $46\%$ de Falsos Positivos)
Considere que um Falso Positivo significa classificar água contaminada como potável e liberá-la para consumo de uma comunidade carente, provocando surtos de cólera.
* Essa configuração de métricas é aceitável para a segurança em saúde pública? Que ajuste visual e de limiar você exigiria que fosse implementado imediatamente no modelo?

---

### Exercício 39: Diagnóstico Gráfico de Separação Perfeita (*Quasi-Complete Separation*)

```plotly
data:
  - x: [10, 20, 30, 40, 48, 50, 52, 60, 70, 80, 90]
    y: [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1]
    type: scatter
    mode: markers
    name: 'Classes Reais Observadas'
    marker:
      color: '#1f77b4'
      size: 10
  - x: [10, 49.5, 50.5, 90]
    y: [0.0, 0.0, 1.0, 1.0]
    type: scatter
    mode: lines
    name: 'Curva Sigmoide em Degrau Vertical (β₁ → ∞)'
    line:
      color: '#d62728'
      width: 3
layout:
  title: 'Separação Perfeita: Falha do Algoritmo MLE'
  xaxis:
    title: 'Variável Contínua X'
  yaxis:
    title: 'Probabilidade Estimada'
```

Ao plotar a probabilidade estimada da regressão logística contra uma variável explicativa contínua no gráfico acima, você observa que todas as observações com $X < 50$ possuem $Y = 0$ e todas as observações com $X \ge 50$ possuem $Y = 1$, sem nenhuma sobreposição na fronteira. A curva ajustada torna-se um degrau vertical reto quase infinito e o software emite avisos de que os coeficientes explodiram para valores astronômicos.
* Que patologia de regressão logística ocorreu? Por que o algoritmo de Máxima Verossimilhança (MLE) falha nessa situação e como resolver o problema?

---

### Exercício 40: Leitura de Importância de Atributos em Gráfico de Barras

```plotly
data:
  - y: ['Açúcar Residual', 'Sulfatos', 'Densidade', 'Acidez Volátil', 'Álcool']
    x: [2, 5, 18, 30, 45]
    type: bar
    orientation: 'h'
    marker:
      color: ['#aec7e8', '#aec7e8', '#aec7e8', '#1f77b4', '#1f77b4']
layout:
  title: 'Importância de Atributos: Redução Média de Gini (%)'
  xaxis:
    title: 'Importância Relativa (%)'
  yaxis:
    title: 'Atributos Químicos'
```

Um modelo de aprendizado supervisionado treinado gera o gráfico horizontal de importância de variáveis acima com base na redução média da impureza de Gini.
1. Como o cientista de dados deve interpretar essa figura para redução de dimensionalidade?
2. Em um processo de simplificação do modelo para implantação em sistemas embarcados com restrição de memória, quais variáveis seriam as primeiras candidatas ao expurgo?

---

### Exercício 41: Análise Comparativa entre Box-plot e Histograma

```plotly
data:
  - x: [2, 2.5, 3, 3.2, 3.5, 3.8, 4, 4.2, 4.5, 5, 5.2, 5.5, 6, 7, 8, 12, 18, 28, 45, 90, 180]
    type: histogram
    name: 'Distribuição Salarial'
    marker:
      color: '#1f77b4'
  - x: [5.2, 5.2]
    y: [0, 10]
    type: scatter
    mode: lines
    name: 'Mediana: R$ 5.200 (Posição Central)'
    line:
      color: '#2ca02c'
      width: 3
  - x: [18.5, 18.5]
    y: [0, 10]
    type: scatter
    mode: lines
    name: 'Média: R$ 18.500 (Puxada pelos Extremos)'
    line:
      color: '#d62728'
      dash: dash
      width: 3
layout:
  title: 'Assimetria Positiva Severa: Média versus Mediana'
  xaxis:
    title: 'Salário (R$ mil)'
  yaxis:
    title: 'Frequência de Funcionários'
```

Em uma análise exploratória, o histograma da variável salarial apresentado acima exibe uma cauda extremamente longa e esparsa que se arrasta para a direita por centenas de milhares de reais, afastando a Média da Mediana.
* Por que a **Média** amostral é substancialmente maior que a **Mediana** nessa variável? Qual dessas duas medidas representa com mais fidelidade o "salário típico" de um colaborador dessa organização?

---

### Exercício 42: Leitura de Gráfico de Contorno / Fronteira de Decisão

```plotly
data:
  - x: [2, 3, 4, 2.5, 3.5, 6, 7, 8, 6.5, 7.5]
    y: [2, 3, 2.5, 4, 3.8, 7, 8, 7.5, 6.5, 8.5]
    type: scatter
    mode: markers
    name: 'Classe 0 (Círculos)'
    marker:
      color: '#1f77b4'
      size: 9
  - x: [2, 3, 3.5, 7, 8, 7.5]
    y: [7, 8, 7.5, 2, 3, 2.5]
    type: scatter
    mode: markers
    name: 'Classe 1 (Cruzes)'
    marker:
      color: '#d62728'
      size: 11
      symbol: 'x'
  - x: [5, 5]
    y: [0, 10]
    type: scatter
    mode: lines
    name: 'Fronteira Ortogonal Árvore (X1 = 5)'
    line:
      color: '#2ca02c'
      width: 3
  - x: [0, 10]
    y: [5, 5]
    type: scatter
    mode: lines
    name: 'Fronteira Ortogonal Árvore (X2 = 5)'
    line:
      color: '#2ca02c'
      width: 3
layout:
  title: 'Fronteiras de Decisão Ortogonais das Árvores'
  xaxis:
    title: 'Atributo Contínuo X1'
    range: [0, 10]
  yaxis:
    title: 'Atributo Contínuo X2'
    range: [0, 10]
```

No gráfico cartesiano acima, a fronteira de decisão gerada por uma Árvore de Decisão consiste exclusivamente em segmentos de retas estritamente ortogonais (horizontais e verticais paralelas aos eixos), enquanto a fronteira da Regressão Logística é uma linha diagonal contínua.
* Explique a razão matemática pela qual as árvores de decisão produzem apenas divisões retangulares/ortogonais no espaço de atributos.

---

### Exercício 43: Trade-off na Curva Precision-Recall versus ROC

```plotly
data:
  - x: [0.0, 0.005, 0.01, 0.02, 0.05, 0.10, 0.20, 1.0]
    y: [0.0, 0.70, 0.80, 0.88, 0.94, 0.97, 0.99, 1.0]
    type: scatter
    mode: lines
    name: 'Curva ROC (Aparente Excelência: AUC = 0.98)'
    line:
      color: '#1f77b4'
      width: 3
  - x: [0.0, 0.20, 0.50, 0.70, 0.80, 0.90, 1.0]
    y: [0.90, 0.65, 0.35, 0.15, 0.08, 0.03, 0.001]
    type: scatter
    mode: lines
    name: 'Curva PR (Realidade Severa: Precisão Despenca)'
    line:
      color: '#d62728'
      width: 3
      dash: dash
layout:
  title: 'Comparativo: Curva ROC versus Curva PR em Classes Raras'
  xaxis:
    title: 'FPR (na ROC) ou Recall (na PR)'
  yaxis:
    title: 'TPR (na ROC) ou Precisão (na PR)'
```

Ao avaliar dois modelos em um cenário de busca jurídica onde a base contém $1.000.000$ de documentos irrelevantes e apenas $100$ contratos confidenciais pertinentes, analise o gráfico comparativo acima:
* O Modelo tem uma Curva ROC com $\text{AUC} = 0,98$. No entanto, quando plotada a **Curva Precisão-Recall (PR Curve)** em vermelho tracejado, a sua precisão para níveis razoáveis de recall cai para apenas $15\%$.
Por que a Curva ROC mascara o fraco desempenho do modelo nesse caso de desbalanceamento extremo de classes? Por que a curva PR é mais fidedigna?

---

### Exercício 44: Análise de Gráfico de Resíduos Padronizados versus Alavancagem (*Cook's Distance*)

```plotly
data:
  - x: [0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.10, 0.11]
    y: [-0.8, 0.5, -1.2, 1.4, -0.2, 0.9, -1.5, 0.8, -0.6, 0.3]
    type: scatter
    mode: markers
    name: 'Observações Normais'
    marker:
      color: '#1f77b4'
      size: 8
  - x: [0.45]
    y: [3.8]
    type: scatter
    mode: markers+text
    name: 'Ponto Influente Crítico'
    text: ['Ponto de Alta Alavancagem e Resíduo (D > 1.0)']
    textposition: 'bottom left'
    marker:
      color: '#d62728'
      size: 14
      symbol: 'x'
  - x: [0.01, 0.50]
    y: [1.8, 3.2]
    type: scatter
    mode: lines
    name: 'Contorno de Cook: D = 0.5'
    line:
      color: '#ff7f0e'
      dash: dash
  - x: [0.01, 0.50]
    y: [2.5, 3.6]
    type: scatter
    mode: lines
    name: 'Contorno de Cook: D = 1.0 (Crítico)'
    line:
      color: '#d62728'
      dash: dot
layout:
  title: 'Resíduos Padronizados vs Alavancagem (Distância de Cook)'
  xaxis:
    title: 'Alavancagem / Leverage (h)'
  yaxis:
    title: 'Resíduos Padronizados'
```

No gráfico de diagnóstico de regressão acima, as linhas pontilhadas representam os limites da **Distância de Cook ($D > 0,5$ e $D > 1,0$)**. O ponto assinalado com o "X" vermelho localiza-se muito além da curva de contorno crítico $D = 1,0$.
1. O que caracteriza esse ponto como um **ponto influente**?
2. Qual é a recomendação rigorosa de ação: remover imediatamente o ponto sem averiguar ou realizar uma investigação de causa-raiz para determinar se foi erro de digitação ou um evento de negócio genuíno e raro?

---

### Exercício 45: Síntese de Diagnóstico Executivo de Modelos

```plotly
data:
  - x: [100, 200, 300, 400, 500, 600, 700]
    y: [18, 5, -8, -12, -9, 4, 19]
    type: scatter
    mode: markers
    name: 'Resíduos do Modelo de Vendas'
    marker:
      color: '#d62728'
      size: 9
  - x: [80, 720]
    y: [0, 0]
    type: scatter
    mode: lines
    name: 'Referência Zero'
    line:
      color: '#7f7f7f'
      dash: dash
  - x: [100, 250, 400, 550, 700]
    y: [18, -2, -12, -2, 19]
    type: scatter
    mode: lines
    name: 'Padrão Parabólico Sistemático'
    line:
      color: '#d62728'
      dash: dot
layout:
  title: 'Relatório Executivo: Diagnóstico de Resíduos vs Ajustados'
  xaxis:
    title: 'Vendas Previstas (ŷ)'
  yaxis:
    title: 'Resíduos Amostrais (e)'
```

Você recebe um relatório executivo de um modelo de regressão para prever vendas corporativas cujo diagnóstico gráfico de resíduos é exibido acima. O relatório ostenta as seguintes informações gráficas e numéricas:
* $R^2$ no conjunto de treino: $0,985$
* $R^2$ no conjunto de teste: $0,520$
* O gráfico de Resíduos vs Ajustados exibe uma parábola nítida.
* Dois preditores possuem correlação linear entre si de $r = 0,94$.
Redija um diagnóstico técnico sintetizado apontando os **três problemas estruturais graves** que esse modelo possui e especifique as três ações corretivas correspondentes que devem ser executadas antes de colocar o modelo em produção.

---

## 🟣 Bloco 4: Seção Especial — Complexidade Polinomial, Erro Absoluto Médio e One-Hot Encoding (Exercícios 46 a 51)

### Exercício 46: Leitura das Curvas de Erro (EAM) por Potência Polinomial (2 Linhas)

```plotly
data:
  - x: [1, 2, 3, 4, 5, 6, 7, 8, 9]
    y: [50.612, 49.258, 46.730, 46.060, 45.307, 45.141, 44.868, 44.597, 44.570]
    type: scatter
    mode: lines+markers
    name: 'Treino (Features Contínuas)'
    line:
      color: '#1f77b4'
      width: 2.5
    marker:
      symbol: 'triangle-up'
      size: 9
  - x: [1, 2, 3, 4, 5, 6, 7, 8, 9]
    y: [50.747, 49.457, 46.942, 46.155, 45.466, 45.412, 45.732, 45.735, 50.999]
    type: scatter
    mode: lines+markers
    name: 'Validação (Features Contínuas)'
    line:
      color: '#2ca02c'
      width: 2.5
    marker:
      symbol: 'square'
      size: 9
  - x: [1, 9]
    y: [50.747, 50.747]
    type: scatter
    mode: lines
    name: 'Linha Baseline (50.747)'
    line:
      color: '#d62728'
      dash: dash
  - x: [6]
    y: [45.412]
    type: scatter
    mode: markers+text
    name: 'Mínimo de Validação (Potência 6)'
    text: ['Mínimo de Validação (Potência 6)']
    textposition: 'bottom center'
    marker:
      color: '#2ca02c'
      size: 12
      symbol: 'diamond'
layout:
  title: 'Erro Absoluto Médio vs Potência Polinomial (Features Contínuas)'
  xaxis:
    title: 'Potência das Variáveis do Modelo (Grau Polinomial)'
    tickvals: [1, 2, 3, 4, 5, 6, 7, 8, 9]
  yaxis:
    title: 'Erro Absoluto Médio (× 1000)'
  hovermode: 'closest'
```

Considere o gráfico acima exibindo o Erro Absoluto Médio ($EAM$) em função da potência das variáveis contínuas ($1$ a $9$) em dados de preços de imóveis:
1. O que representa o comportamento das duas curvas na **Potência 1** (onde ambas estão altas e coladas próximas a $50.700$)?
2. Em qual potência o erro de validação atinge seu ponto ótimo de mínimo sem variáveis categóricas?
3. O que acontece entre o erro de treino e o de validação a partir da **Potência 7 até a 9**? Qual fenômeno estatístico clássico isso caracteriza?

---

### Exercício 47: Leitura Comparativa das 4 Linhas com One-Hot Encoding

```plotly
data:
  - x: [1, 2, 3, 4, 5, 6, 7, 8, 9]
    y: [50.612, 49.258, 46.730, 46.060, 45.307, 45.141, 44.868, 44.597, 44.570]
    type: scatter
    mode: lines+markers
    name: 'Treino (sem OHE)'
    line:
      color: '#1f77b4'
      width: 2
    marker:
      symbol: 'triangle-up'
      size: 7
  - x: [1, 2, 3, 4, 5, 6, 7, 8, 9]
    y: [50.747, 49.457, 46.942, 46.155, 45.466, 45.412, 45.732, 45.735, 50.999]
    type: scatter
    mode: lines+markers
    name: 'Validação (sem OHE)'
    line:
      color: '#2ca02c'
      width: 2
    marker:
      symbol: 'square'
      size: 7
  - x: [1, 2, 3, 4, 5, 6, 7, 8, 9]
    y: [49.646, 48.652, 46.104, 45.292, 44.620, 44.477, 44.204, 44.008, 43.962]
    type: scatter
    mode: lines+markers
    name: 'Treino (com One-Hot OHE)'
    line:
      color: '#1f77b4'
      dash: dash
      width: 2.5
    marker:
      symbol: 'triangle-up'
      size: 8
  - x: [1, 2, 3, 4, 5, 6, 7, 8, 9]
    y: [49.503, 48.697, 45.905, 45.091, 44.591, 44.559, 44.747, 45.337, 50.452]
    type: scatter
    mode: lines+markers
    name: 'Validação (com One-Hot OHE)'
    line:
      color: '#2ca02c'
      dash: dash
      width: 3
    marker:
      symbol: 'square'
      size: 9
  - x: [1, 9]
    y: [50.747, 50.747]
    type: scatter
    mode: lines
    name: 'Baseline'
    line:
      color: '#d62728'
      dash: dot
layout:
  title: 'Comparativo de 4 Linhas: EAM vs Potência com e sem One-Hot Encoding'
  xaxis:
    title: 'Potência das Variáveis do Modelo'
    tickvals: [1, 2, 3, 4, 5, 6, 7, 8, 9]
  yaxis:
    title: 'Erro Absoluto Médio (× 1000)'
  hovermode: 'closest'
```

Ao analisar o gráfico completo de 4 linhas acima (comparando modelos sem OHE com linhas sólidas versus modelos com OHE em linhas tracejadas):
* Por que as duas curvas tracejadas (com One-Hot Encoding) posicionam-se **sistematicamente abaixo** das respectivas curvas sólidas em praticamente todas as potências? O que essa separação vertical comprova sobre a relevância das variáveis categóricas de localização?

---

### Exercício 48: Diagnóstico de Underfitting versus Overfitting pelas Potências

```plotly
data:
  - x: [1, 5, 9]
    y: [50.612, 45.307, 44.570]
    type: scatter
    mode: markers+lines
    name: 'Treino'
    line:
      color: '#1f77b4'
      width: 2
    marker:
      size: 10
  - x: [1, 5, 9]
    y: [50.747, 45.466, 50.999]
    type: scatter
    mode: markers+lines
    name: 'Validação'
    line:
      color: '#2ca02c'
      width: 2
    marker:
      size: 10
  - x: [1, 9]
    y: [50.747, 50.747]
    type: scatter
    mode: lines
    name: 'Baseline'
    line:
      color: '#d62728'
      dash: dash
layout:
  title: 'Foco nos Três Estados Críticos: Potência 1 vs 5 vs 9'
  xaxis:
    title: 'Grau de Potência do Modelo'
    tickvals: [1, 5, 9]
    ticktext: ['Potência 1 (Underfitting)', 'Potência 5 (Ótimo)', 'Potência 9 (Overfitting)']
  yaxis:
    title: 'Erro Absoluto Médio (× 1000)'
```

Com base no gráfico simplificado acima, que isola as potências $1$, $5$ e $9$:
1. Explique por que a **Potência 1** é diagnosticada tecnicamente como **Subajuste (*Underfitting*)**.
2. Explique por que a **Potência 9** é diagnosticada tecnicamente como **Sobreajuste (*Overfitting*)**, analisando a distância vertical de afastamento entre a linha de treino e a de validação.

---

### Exercício 49: Seleção Justificada do Modelo para Implantação em Produção

```plotly
data:
  - x: [1, 2, 3, 4, 5, 6, 7, 8, 9]
    y: [49.503, 48.697, 45.905, 45.091, 44.591, 44.559, 44.747, 45.337, 50.452]
    type: scatter
    mode: lines+markers
    name: 'Erro de Validação (com OHE)'
    line:
      color: '#2ca02c'
      width: 3
  - x: [5]
    y: [44.559]
    type: scatter
    mode: markers+text
    name: 'Ponto Ótimo: Potência 5'
    text: ['MELHOR MODELO (Potência 5: EAM = 44.559)']
    textposition: 'bottom center'
    marker:
      color: '#d62728'
      size: 14
      symbol: 'star'
layout:
  title: 'Curva de Validação com OHE: Localização do Mínimo Global'
  xaxis:
    title: 'Potência Polinomial'
    tickvals: [1, 2, 3, 4, 5, 6, 7, 8, 9]
  yaxis:
    title: 'EAM de Validação (× 1000)'
```

Um analista júnior de precificação imobiliária observa que na 9ª potência com One-Hot Encoding o erro de **treinamento** é o menor de toda a tabela ($EAM_{\text{treino}} = 43.962$). Por isso, ele propõe colocar o modelo de 9ª potência em produção.
* Utilizando o gráfico de validação acima, redija a justificativa técnica para rejeitar a proposta do analista e comprovar por que o **modelo com 5ª potência e One-Hot Encoding** deve ser o escolhido.

---

### Exercício 50: Engenharia de Atributos: Por que Dummies não são Elevadas a Potências?
No script do professor, a variável categórica de localização `prox_oceano` possui 5 categorias: `[1H OCEANO, BAÍA, INTERIOR, LITORAL, ILHA]`.
1. Quantas colunas binárias (*dummies*) foram criadas para entrar no modelo de regressão com intercepto? Cite a regra que fundamenta essa decisão.
2. No código, as variáveis contínuas numéricas foram elevadas às potências de 1 a 9 (`I(latitude^2)`, `I(latitude^3)`, etc.), mas as variáveis de One-Hot Encoding foram mantidas na sua forma linear fixa de 1º grau. Explique a razão matemática rigorosa pela qual **variáveis dummy não devem ser elevadas a potências quadráticas ou cúbicas**.

---

### Exercício 51: A Linha de Linha de Base (*Baseline*) e o Ponto de Ruptura
Nos gráficos de potência polinomial da aula, uma linha horizontal vermelha contínua corta o gráfico na altura de $EAM \approx 50.747$.
1. O que representa conceitualmente a **linha de baseline** em uma modelagem preditiva supervisionada?
2. O que significa, em termos de generalização e confiabilidade, quando a curva de validação na **Potência 9** ultrapassa a linha de baseline para cima ($EAM_{\text{valid}} = 50.999$)?

---

## 💡 Seção de Dicas (Dicas 01 a 51)

Use estas orientações para desbloquear seu raciocínio sem recorrer diretamente ao gabarito:

* **Dica 01**: Lembre-se de que a mediana é a linha que divide a caixa exatamente ao meio e o $IQR$ é simplesmente a largura da caixa ($Q_3 - Q_1$). Entre $Q_1$ e $Q_3$ está exatamente a metade central de qualquer amostra.
* **Dica 02**: A cerca superior de Tukey é dada pela fórmula $Q_3 + 1,5 \times IQR$. Aplique os valores numéricos encontrados no exercício anterior.
* **Dica 03**: O intercepto $\beta_0$ ocorre quando a variável preditora é nula ($X = 0$). A inclinação $\beta_1$ multiplica o acréscimo de $X$.
* **Dica 04**: A fórmula universal do resíduo é sempre o valor observado real menos o valor predito pelo modelo: $e_i = Y_i - \hat{Y}_i$. Se o resíduo for positivo, o modelo previu abaixo da realidade.
* **Dica 05**: O sinal do coeficiente de Pearson indica a direção (positivo = sobem juntos; negativo = um sobe e o outro desce) e a magnitude próxima de $1$ reflete força linear.
* **Dica 06**: Pearson mede apenas associações estritamente **lineares**. Pense em uma parábola simétrica perfeita $Y = X^2$ centrada em zero: a relação é determinística e exata, mas $r = 0$.
* **Dica 07**: A diagonal de 45° divide um quadrado unitário de área $1 \times 1$ exatamente em dois triângulos idênticos.
* **Dica 08**: No classificador perfeito, você detecta todos os positivos sem cometer nenhum alarme falso. Qual é a taxa de acerto e qual é a taxa de erro?
* **Dica 09**: Lembre-se de que qualquer número elevado a zero resulta em $1$ ($e^0 = 1$). Calcule $\frac{1}{1 + 1}$.
* **Dica 10**: Compare cada probabilidade calculada com o limiar $\theta = 0,50$. Em empates exatos ($0,50$), a regra padrão estrita exige que seja maior que o limiar ou segue a convenção de classe majoritária.
* **Dica 11**: Acurácia é o total de acertos dividido pelo total de pacientes ($TP + TN / N$). Recall avalia apenas os doentes reais: quantos dos positivos reais foram capturados?
* **Dica 12**: Tipo I é o alarme falso (saudável rotulado como doente); Tipo II é a omissão (doente que volta para casa sem diagnóstico).
* **Dica 13**: Quanto mais flexível e complexo for o modelo, mais ele se molda aos dados de treino (reduzindo o viés), mas maior se torna sua volatilidade diante de novas amostras (aumentando a variância).
* **Dica 14**: O $R^2$ reflete o quão compacta e aderente está a nuvem de pontos ao redor da linha reta.
* **Dica 15**: A linha diagonal é o espelho exato onde o previsto bate $100\%$ com a realidade. Estar acima da linha significa que a realidade ($Y$) foi maior do que a previsão do modelo ($\hat{Y}$).
* **Dica 16**: Se os erros têm formato de arco/parábola, a reta de primeiro grau é insuficiente. Falta um expoente de ordem superior para descrever a curvatura.
* **Dica 17**: Pense na palavra "hetero" (diferente) e "cedasticidade" (dispersão). Quando a variância cresce com a escala da variável, a transformação logarítmica contrai valores grandes com muito mais força que valores pequenos.
* **Dica 18**: Quanto mais a curva se aproxima do canto superior esquerdo (afastando-se da diagonal neutra), maior é a área sob a curva. Se uma curva nunca cruza a outra e fica sempre por cima, ela ganha em qualquer cenário.
* **Dica 19**: Para não deixar nenhuma fraude escapar, você deve tornar o modelo mais desconfiado ou mais tolerante? Se o modelo disparar alerta mesmo com pouca probabilidade (ex: $20\%$), ele deixará menos fraudes passarem.
* **Dica 20**: Se 99,5% da base pertence a uma única classe, um classificador cego que sempre chuta a classe majoritária acerta 99,5% das vezes, mas tem utilidade zero para achar os casos raros.
* **Dica 21**: Um bom preditor deve separar as classes no espaço. Se as distribuições dos dois grupos se sobrepõem totalmente, o atributo não adiciona poder discriminatório.
* **Dica 22**: Quando dois preditores medem praticamente a mesma coisa ($r = 0,91$), a matriz de dados se aproxima da redundância matemática (quase-singularidade), inflando a incerteza dos coeficientes.
* **Dica 23**: Nuvens separadas por vazios denunciam subpopulações distintas (misturas de distribuições). Modelos de clusterização (como K-Means) ou árvores segmentadas são ideais.
* **Dica 24**: O erro de validação aponta o ponto de generalização ótima no seu ponto de mínimo. Quando ele volta a subir enquanto o treino cai, o modelo começou a decorar ruído amostral.
* **Dica 25**: Se o modelo não aprende bem nem os dados de treino nem os de teste, ele sofre de falta crônica de complexidade (alto viés). Mais dados não corrigem um modelo simplista demais; precisa-se de mais variáveis ou algoritmos mais expressivos.
* **Dica 26**: Mínimos Quadrados minimizam o quadrado dos desvios verticais. Um ponto distante com erro grande exerce uma alavanca desproporcional sobre a reta, puxando-a em sua direção.
* **Dica 27**: A média harmônica é severamente puxada para baixo se uma das duas métricas for muito pequena. Ela pune equilíbrios discrepantes entre Precisão e Recall.
* **Dica 28**: Pense na soma das dummies: $D_1 + D_2 + D_3 + D_4 = 1$. Como o modelo já possui a constante (intercepto $\beta_0 \times 1$), cria-se uma combinação linear perfeita ($1 = 1$), inviabilizando a inversão da matriz.
* **Dica 29**: Se os pontos do Q-Q Plot fogem da diagonal nas pontas formando caudas em "S", a distribuição empírica dos resíduos tem valores extremos muito mais frequentes do que uma Gaussiana perfeita prevê.
* **Dica 30**: A fórmula do $Z$-score subtrai a média e divide pelo desvio-padrão. Isso desloca a média para zero e fixa a escala em unidades de desvio-padrão, sem distorcer as distâncias relativas entre os pontos.
* **Dica 31**: Lembre-se de que $R^2$ mede apenas a variância explicada pela reta, mas não verifica se o modelo é tendencioso. O gráfico de resíduos revela se há erros sistemáticos na estimativa.
* **Dica 32**: Compare a multiplicação dos custos: perder R$ 3.200 a cada fraude não capturada é 6.400 vezes mais grave do que gastar R$ 0,50 para verificar um alarme falso.
* **Dica 33**: Na Normalização Min-Max, o valor máximo ($x_{\max} = 99,9$) se torna $1,0$ e o mínimo se torna $0,0$. O que acontece com os dados que ficam entre 10 e 35 quando espremidos contra uma escala que vai até 100?
* **Dica 34**: O princípio da Navalha de Occam: entre dois modelos com capacidade preditiva estatisticamente indistinguível (dentro de 1 erro-padrão), o modelo mais parcimonioso e simples é sempre o preferido.
* **Dica 35**: Pense na dependência serial temporal e no teste de Durbin-Watson. Se os erros de hoje dependem dos erros de ontem, as observações não são estatisticamente independentes.
* **Dica 36**: Para calcular o efeito de um acréscimo de $\Delta X = 10$, a razão de chances é multiplicada por $e^{\beta_1 \times 10} = (e^{\beta_1})^{10}$.
* **Dica 37**: No ponto onde Recall e Especificidade se cruzam, o modelo equilibra perfeitamente a taxa de captura de positivos com a taxa de captura de negativos.
* **Dica 38**: Em saúde pública, permitir que água contaminada seja rotulada como potável ($FP$) causa mortes. A prioridade absoluta deve ser maximizar a Especificidade (reduzir Falsos Positivos a quase zero).
* **Dica 39**: Quando uma variável separa perfeitamente as duas classes sem nenhuma sobreposição, o coeficiente da regressão logística tende ao infinito teórico para alcançar probabilidades absolutas de $0$ e $1$.
* **Dica 40**: Variáveis com contribuição ínfima para a redução da impureza das divisões adicionam ruído e custo computacional sem trazer ganho expressivo de informação preditiva.
* **Dica 41**: A média aritmética é sensível e é puxada para a cauda longa pelos milionários; a mediana olha apenas para a posição central dos indivíduos ordenados.
* **Dica 42**: Árvores de decisão realizam cortes univariados consecutivos do tipo $X_j \le c$, que representam hiperplanos perpendiculares aos eixos cartesianos.
* **Dica 43**: A taxa FPR do gráfico ROC tem no denominador o total de negativos reais ($FP + TN$). Quando $TN$ é gigantesco (um milhão), um aumento expressivo em $FP$ mal altera o FPR, enquanto a Precisão ($TP / (TP + FP)$) desaba.
* **Dica 44**: Um ponto isolado com alta alavancagem pode ser um erro de entrada de dados ou uma observação vital do mundo real. Ele nunca deve ser deletado sem uma investigação qualitativa do contexto.
* **Dica 45**: Conecte os quatro sintomas diagnosticados: discrepância gigante de $R^2$ entre treino e teste (overfitting), parábola nos resíduos (não linearidade) e correlação $0,94$ entre preditores (multicolinearidade).
* **Dica 46**: Na potência 1, o modelo só traça uma reta linear hiper-rígida, errando feio tanto no treino quanto na validação. Observe em qual potência o erro de validação para de cair e começa a subir.
* **Dica 47**: As variáveis contínuas medem dimensões métricas (área, cômodos), mas ignoram a localização espacial. A proximidade com o oceano explica uma fatia enorme da variância do preço imobiliário, empurrando as curvas de erro para baixo.
* **Dica 48**: O subajuste peca por falta de flexibilidade (ambos os erros altos). O sobreajuste é denunciado pelo "efeito tesoura": o treino continua caindo enquanto a validação explode para cima, abrindo um grande vão entre as linhas.
* **Dica 49**: Em modelos preditivos, o critério de escolha NUNCA é o menor erro de treino (que apenas mede memorização), mas sim o ponto onde o erro na amostra de validação atinge seu ponto mais baixo antes de começar a sobreajustar.
* **Dica 50**: Para $k$ categorias, precisamos de $k - 1$ colunas dummy para que a categoria omitida seja o referencial base. Lembre-se de que $0^2=0$ e $1^2=1$: elevar uma dummy a qualquer potência resulta exatamente nela mesma!
* **Dica 51**: A linha de baseline é o chute ingênuo da média/mediana sem modelo nenhum. Se um modelo complexo de 9ª potência fica pior do que o baseline, ele se tornou tão instável e ruidoso que chutar a média é mais seguro.
