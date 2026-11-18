---
aliases:
  - Gabarito dos Exercícios de Gráficos
  - Resoluções Comentadas de Gráficos
  - Respostas dos 45 Exercícios
tags:
  - gabarito
  - resolucoes
  - graficos
  - interpretacao
  - data-science
---

# Resoluções e Gabarito Comentado: Exercícios de Interpretação de Gráficos e Modelos

Este documento apresenta a resolução analítica exaustiva e comentada de todos os **45 exercícios** do [[Exercícios de Interpretação de Gráficos e Modelos|Caderno de Exercícios de Interpretação]]. 

Cada resolução detalha não apenas a resposta correta, mas também a **fundamentação teórica exigida em provas acadêmicas**, as fórmulas aplicadas, os erros conceituais comuns e a justificativa para a tomada de decisão técnica.

---

## 🟢 Bloco 1: Nível Fundamental (Exercícios 01 a 15)

### Resolução 01
1. **Mediana e Intervalo Interquartil ($IQR$)**:
   * **Mediana ($Q_2$)**: É a linha divisória interna da caixa do box-plot: **$R\$ 6.500,00$**. Representa o valor central que divide a distribuição salarial rigorosamente ao meio: $50\%$ dos empregados ganham até esse valor e $50\%$ ganham mais que isso.
   * **Intervalo Interquartil ($IQR$)**: É a amplitude da caixa, calculada como a diferença entre o 3º quartil ($Q_3$) e o 1º quartil ($Q_1$):
     $$IQR = Q_3 - Q_1 = 10.000 - 4.000 = R\$ 6.000,00$$
2. **Significado do Intervalo $[R\$ 4.000, R\$ 10.000]$**:
   * Corresponde rigorosamente aos **$50\%$ centrais da distribuição de funcionários**. Por definição de quartis, $25\%$ dos funcionários ganham menos que $R\$ 4.000$ (abaixo de $Q_1$) e $25\%$ ganham mais que $R\$ 10.000$ (acima de $Q_3$).

---

### Resolução 02
* **Fórmula da Cerca Superior de Tukey**:
  $$\text{Cerca Superior} = Q_3 + 1,5 \times IQR$$
* **Cálculo Numérico**:
  $$\text{Cerca Superior} = 10.000 + 1,5 \times 6.000 = 10.000 + 9.000 = R\$ 19.000,00$$
* **Conclusão**: Qualquer funcionário que receba um salário estritamente superior a **$R\$ 19.000,00$** será assinalado no gráfico como um ponto isolado além do bigode superior (*outlier* univariado).

---

### Resolução 03
1. **Interpretação do Intercepto ($\hat{\beta}_0 = 35$)**:
   * É o valor esperado da nota final ($Y$) para um estudante que tenha dedicado **zero horas** semanais ao estudo formal da disciplina ($X = 0$). Reflete o conhecimento prévio basal ou o rendimento mínimo esperado sem esforço complementar.
2. **Impacto do Acréscimo de 5 Horas de Estudo**:
   * O coeficiente angular $\hat{\beta}_1 = 2,8$ representa a taxa marginal de variação: cada hora adicional de estudo eleva a nota prevista em $2,8$ pontos.
   * Para $\Delta X = +5$ horas:
     $$\Delta \hat{Y} = \hat{\beta}_1 \times \Delta X = 2,8 \times 5 = +14,0 \text{ pontos}$$
   * Espera-se que a nota final do aluno aumente em **$14$ pontos**.

---

### Resolução 04
1. **Previsão do Modelo para $X = 10$**:
   $$\hat{Y} = 35 + 2,8 \times 10 = 35 + 28 = 63,0$$
2. **Cálculo do Resíduo Amostral ($e_i$)**:
   $$e_i = Y_i - \hat{Y}_i = 70 - 63 = +7,0$$
3. **Interpretação de Super/Subestimação**:
   * Como o resíduo é **positivo** ($e_i > 0$), a realidade ($70$) foi superior à previsão ($63$). Logo, o modelo **subestimou** o rendimento desse aluno em $7$ pontos.

---

### Resolução 05
* **Direção**: Como o sinal é positivo ($+$), trata-se de uma relação linear **diretamente proporcional**. À medida que a idade do indivíduo avança, a sua pressão arterial sistólica esperada também aumenta de forma consistente.
* **Intensidade**: Um coeficiente de correlação de Pearson de $r = +0,74$ situa-se na faixa entre $0,70$ e $0,89$, o que é classificado na estatística como uma **associação linear forte**.

---

### Resolução 06
* **Não, não se pode afirmar categoricamente que não existe relação!**
* **Justificativa Rigorosa**: O coeficiente de Pearson avalia exclusivamente a força e a direção de relações estritamente **lineares** (em linha reta). Se duas variáveis tiverem uma relação não linear perfeita (por exemplo, uma relação quadrática simétrica $Y = X^2$ para $X \in [-10, 10]$ ou uma curva senoidal), os pontos estarão perfeitamente ligados por uma função matemática determinística, porém a correlação linear de Pearson resultará em exatamente $r = 0,00$. A inspeção do gráfico de dispersão é indispensável para descartar dependências não lineares.

---

### Resolução 07
1. **Valor da AUC**:
   * A linha diagonal divide a área do quadrado unitário de dimensões $[0, 1] \times [0, 1]$ (área total $= 1,0$) exatamente ao meio. Portanto, a área sob a curva é:
     $$\text{AUC} = 0,50$$
2. **Utilidade Clínica**:
   * O classificador tem **utilidade nula**. Um modelo com $\text{AUC} = 0,50$ possui capacidade de discriminação idêntica ao lançamento de uma moeda não viciada (*chute puramente aleatório*). Ele é incapaz de separar pacientes doentes de saudáveis com acurácia superior ao acaso.

---

### Resolução 08
* **Coordenadas Exatas**:
  $$(X, Y) = (0, 1) \implies (\text{FPR} = 0,0; \text{TPR} = 1,0)$$
* **Significado Teórico**:
  * $\text{TPR} = 1,0$ (Taxa de Verdadeiros Positivos / Recall / Sensibilidade de $100\%$): O modelo detecta absolutamente todos os casos positivos reais da amostra, sem cometer nenhum Falso Negativo ($FN = 0$).
  * $\text{FPR} = 0,0$ (Taxa de Falsos Positivos de $0\%$): O modelo nunca classifica uma instância negativa como positiva, cometendo zero Falsos Positivos ($FP = 0$). É a perfeição preditiva absoluta.

---

### Resolução 09
* **Aplicação da Função Sigmoide**:
  $$p(z) = \sigma(z) = \frac{1}{1 + e^{-z}}$$
* **Para $z = 0,0$**:
  $$e^{-0} = e^0 = 1 \implies p(0) = \frac{1}{1 + 1} = \frac{1}{2} = 0,50 \text{ (ou } 50\%)$$
* **Conclusão**: O valor $z = 0$ representa o **ponto de inflexão central** da curva logística, mapeando exatamente a probabilidade de $50\%$.

---

### Resolução 10
Sob a regra de decisão padrão: $\hat{Y} = 1$ se $p \ge 0,50$ (ou $p > 0,50$ conforme convenção estrita) e $\hat{Y} = 0$ caso contrário:
* **Instância A ($p_A = 0,48$)**: Como $0,48 < 0,50$, recebe a classe **$\hat{Y} = 0$ (Negativo)**.
* **Instância B ($p_B = 0,52$)**: Como $0,52 \ge 0,50$, recebe a classe **$\hat{Y} = 1$ (Positivo)**.
* **Instância C ($p_C = 0,50$)**: Por convenção padrão em que o limiar $\theta = 0,50$ inclui a igualdade ($\ge 0,50$), é classificada como **$\hat{Y} = 1$ (Positivo)**.

---

### Resolução 11
* **Dados Extraídos da Matriz**:
  * $TP = 40$
  * $FN = 5$
  * $FP = 10$
  * $TN = 45$
  * Total de Observações $N = 40 + 5 + 10 + 45 = 100$
1. **Acurácia Global**:
   $$\text{Acurácia} = \frac{TP + TN}{N} = \frac{40 + 45}{100} = \frac{85}{100} = 0,85 \text{ (ou } 85\%)$$
2. **Recall (Sensibilidade)**:
   $$\text{Recall} = \frac{TP}{TP + FN} = \frac{40}{40 + 5} = \frac{40}{45} \approx 0,8889 \text{ (ou } 88,9\%)$$

---

### Resolução 12
1. **Erro do Tipo I (Falso Positivo — $FP$)**:
   * Contagem: **$10$ pacientes**.
   * Significado Prático: Pacientes clinicamente sadios que receberam erroneamente o diagnóstico de doentes ("falso alarme"). Serão submetidos a ansiedade psicológica desnecessária e novos exames confirmatórios invasivos.
2. **Erro do Tipo II (Falso Negativo — $FN$)**:
   * Contagem: **$5$ pacientes**.
   * Significado Prático: Pacientes portadores da patologia que foram incorretamente informados de que estavam sadios ("omissão perigosa"). Não receberão tratamento oportuno, gerando risco severo de agravamento ou óbito.

---

### Resolução 13
* **Viés ($Bias$)**: **Diminui continuamente**. À medida que a complexidade do modelo aumenta (mais níveis na árvore, mais graus polinomiais), o algoritmo ganha capacidade e flexibilidade para se moldar aos dados de treino, reduzindo a distância entre as previsões médias e a realidade empírica.
* **Variância ($Variance$)**: **Aumenta progressivamente**. Modelos excessivamente complexos tornam-se hipersensíveis a flutuações e ruídos amostrais específicos do conjunto de treino, variando bruscamente quando avaliados em conjuntos de dados ligeiramente distintos.

---

### Resolução 14
* **Modelo 1 ($R^2 = 0,45$)**: A nuvem de pontos no gráfico de dispersão apresenta-se bastante espalhada, dispersa e afastada da reta de regressão. Há grande variabilidade residual não explicada pelo modelo.
* **Modelo 2 ($R^2 = 0,92$)**: A nuvem de pontos encontra-se densamente concentrada e quase perfeitamente alinhada e compactada ao redor da reta de regressão, indicando excelente capacidade preditiva linear.

---

### Resolução 15
* **Ponto sobre a Linha Diagonal de 45° ($Y = \hat{Y}$)**: Representa uma **previsão perfeita**. Para aquela observação específica, o valor estimado pelo modelo coincidiu exatamente com a realidade empírica ($e_i = 0$).
* **Ponto consideravelmente acima da Linha ($Y > \hat{Y}$)**: Indica que a realidade foi substancialmente maior do que a previsão emitida pelo modelo. Logo, o modelo **subestimou severamente** o valor daquela observação.

---

## 🟡 Bloco 2: Nível Intermediário (Exercícios 16 a 30)

### Resolução 16
* **Premissa Violada**: **Linearidade nos Parâmetros e na Relação** (a premissa de que a média condicional dos erros é zero para qualquer nível de $X$: $E[\epsilon_i | X_i] = 0$). A presença de curvatura sistemática prova que os resíduos não são ruído branco puramente aleatório.
* **Modificação Estrutural na Fórmula**: O modelo deve incorporar um **termo de segundo grau (quadrático)** para acomodar a concavidade da relação física. Se a fórmula original era:
  $$\text{Poluentes} = \beta_0 + \beta_1 \cdot \text{Rotacao} + \epsilon$$
  Deve ser corrigida para:
  $$\text{Poluentes} = \beta_0 + \beta_1 \cdot \text{Rotacao} + \beta_2 \cdot \text{Rotacao}^2 + \epsilon$$

---

### Resolução 17
1. **Nome do Fenômeno**: **Heterocedasticidade** (violação da premissa de homocedasticidade, significando variância não constante dos termos de erro: $\text{Var}(\epsilon_i) \neq \sigma^2$).
2. **Impacto sobre Testes de Hipótese**: Embora os estimadores OLS continuem não viesados, eles **deixam de ser de variância mínima (perdem a propriedade BLUE)**. Os erros-padrão calculados convencionalmente tornam-se inconsistentes e viesados (geralmente subestimados), fazendo com que as estatísticas $t$ e $F$ fiquem artificialmente inflacionadas e os $p$-valores gerem conclusões falsamente significativas.
3. **Remédio Clássico**: Aplicar uma **transformação logarítmica** na variável dependente $Y$ (ou no modelo $\ln(Y) = \mathbf{X}\boldsymbol{\beta}$), pois o logaritmo comprime as magnitudes maiores com mais intensidade, estabilizando a dispersão residual.

---

### Resolução 18
* **Modelo com Maior AUC**: O **Modelo Alfa**.
* **Justificativa Técnica de Dominância**: 
  * Para uma mesma taxa de alarme falso de $10\%$ ($\text{FPR} = 0,10$), o Modelo Alfa captura $85\%$ dos positivos ($\text{TPR} = 0,85$), enquanto o Beta captura apenas $60\%$.
  * Para $\text{FPR} = 0,20$, o Modelo Alfa atinge $92\%$, enquanto o Beta atinge $75\%$.
  * Como a curva do Modelo Alfa posiciona-se estritamente **acima e à esquerda** da curva do Modelo Beta em todo o contínuo de limiares $\theta \in [0, 1]$, o Modelo Alfa apresenta **dominância estocástica**. Para qualquer nível de tolerância a alarmes falsos fixado pela empresa, o Modelo Alfa garantirá sempre um Recall superior, gerando uma integral de área sob a curva (AUC) inquestionavelmente maior.

---

### Resolução 19
* **Direção do Deslocamento**: O cientista deve **reduzir o limiar para próximo de $\theta = 0,15$**.
* **Impacto nas Métricas**:
  * **Recall**: **Aumentará expressivamente** (aproximando-se de $100\%$). Ao exigir apenas $15\%$ de probabilidade estimada para bloquear a transação, o modelo torna-se extremamente sensível, capturando praticamente todas as fraudes reais.
  * **Precisão**: **Cairá substancialmente**. A contrapartida inevitável da redução do limiar é o aumento acentuado de Falsos Positivos ($FP$ — clientes idôneos com compras legítimas bloqueadas preventivamente).

---

### Resolução 20
1. **Acurácia Global do Modelo Ingênuo**:
   $$\text{Acurácia} = \frac{9.950}{10.000} = 0,995 \text{ (ou } 99,5\%)$$
2. **Recall da Classe Rara (Doença)**:
   $$\text{Recall} = \frac{TP}{TP + FN} = \frac{0}{0 + 50} = 0,00 \text{ (ou } 0\%)$$
3. **Por que a Acurácia é Enganosa e Qual Gráfico Usar**:
   * Esse fenômeno é o **Paradoxo da Acurácia**: em bases desbalanceadas, prever exclusivamente a classe majoritária mascara a total inoperância do classificador para identificar o fenômeno de interesse.
   * Deve-se inspecionar o **Heatmap da Matriz de Confusão** e plotar a **Curva Precision-Recall (PR Curve)** ou a **Curva ROC**, avaliando especificamente o Recall e a Precisão da classe minoritária.

---

### Resolução 21
* **Seleção do Atributo B**: O Atributo B (*Dias desde o último login*) apresenta caixas quase totalmente disjuntas (sobreposição $< 10\%$) entre quem cancelou e quem permaneceu fiel. Isso comprova que os dois grupos ocupam regiões distintas e separáveis nessa dimensão contínua, conferindo a esse atributo um **alto poder preditivo discriminatório**.
* **Descarte do Atributo A**: O Atributo A (*Idade*) possui sobreposição de $95\%$ e medianas alinhadas. Isso significa que saber a idade de um cliente não fornece nenhuma informação estatística relevante para distinguir se ele vai ou não cancelar o serviço. Incluí-lo apenas adiciona ruído e graus de liberdade desnecessários.

---

### Resolução 22
1. **Complicação Estatística**: Trata-se de **Severa Multicolinearidade** entre preditores. Como $r = +0,91$, as duas variáveis contêm praticamente a mesma informação explicativa.
2. **Impacto sobre Erros-Padrão e Coeficientes**:
   * A matriz $(\mathbf{X}^T \mathbf{X})$ torna-se quase-singular (determinante muito próximo de zero).
   * Os **erros-padrão dos coeficientes $\hat{\beta}$ inflam enormemente**, fazendo com que as estatísticas $t$ caiam e variáveis individualmente relevantes pareçam estatisticamente não significativas ($p > 0,05$).
   * Os sinais dos coeficientes podem se tornar contra-intuitivos (por exemplo, um coeficiente de cômodos negativo mesmo em casas mais caras) devido à instabilidade numérica.

---

### Resolução 23
* **Interpretação da Visualização**: A presença de duas nuvens densas isoladas por um vazio indica a existência de **subpopulações multimodais heterogêneas** (por exemplo, dois tipos completamente distintos de biomas ou solos calcários versus arenosos misturados na mesma base).
* **Modelagem Vantajosa**: Aplicar inicialmente um algoritmo de agrupamento (*clustering*, como K-Means ou Gaussian Mixture Models) para rotular os segmentos, ou utilizar uma **Árvore de Decisão** (que é naturalmente capaz de segmentar o espaço com divisões locais ortogonais), em vez de impor uma única reta linear global que atravessará o vazio intermediário sem representar bem nenhum dos dois grupos.

---

### Resolução 24
1. **Profundidade Ótima**: **Profundidade 4**. É o ponto onde o erro no conjunto de validação atinge seu valor mínimo absoluto ($0,18$).
2. **Diagnóstico entre Profundidades 5 e 10**:
   * Ocorre o fenômeno do **Sobreajuste (*Overfitting*) / Alta Variância**. O algoritmo passa a memorizar ruídos e idiossincrasias amostrais dos dados de treino (onde o erro vai a $0,01$), perdendo totalmente a capacidade de generalização para novos dados (o erro de validação dispara para $0,55$).
   * **Justificativa de Poda**: A árvore deve sofrer poda (*pruning*) no parâmetro de custo-complexidade correspondente à profundidade 4 para maximizar a acurácia no mundo real.

---

### Resolução 25
* **Diagnóstico**: O cenário caracteriza **Alto Viés (*Underfitting*)**.
* **Adicionar Mais Dados Resolverá?**: **Não**. Quando um modelo sofre de subajuste, ele não possui capacidade e flexibilidade representacional para capturar o padrão gerador dos dados; alimentá-lo com mais exemplos apenas fará com que ele erre as novas amostras da mesma forma.
* **Ação Recomendada**: Aumentar a expressividade do modelo: adicionar novas variáveis preditoras, criar termos de interação e polinomiais, ou trocar o algoritmo linear por modelos mais flexíveis (como Árvores de Decisão, Random Forest ou Redes Neurais).

---

### Resolução 26
* **Comportamento Visual da Reta OLS**: A reta sofrerá uma rotação brusca em direção ao ponto extremo, tendo sua inclinação $\hat{\beta}_1$ **drasticamente puxada para baixo (tornando-se menos inclinada ou até negativa)**.
* **Por que o OLS é Sensível**: O critério de otimização de Mínimos Quadrados minimiza a **soma dos quadrados dos resíduos** ($\sum e_i^2$). Como um ponto afastado em $X = 100$ gera um braço de alavanca monumental (*high leverage*), qualquer distância vertical até a reta resulta em um erro quadrático astronômico. Para amortecer essa penalidade quadrática imensa daquele único ponto, a matemática do OLS distorce toda a inclinação da reta, sacrificando o ajuste das outras 50 observações.

---

### Resolução 27
* **Modelo com F1-Score Superior**: O **Modelo 2**.
* **Demonstração Numérica pela Média Harmônica**:
  $$F_1 = 2 \times \frac{\text{Precisão} \times \text{Recall}}{\text{Precisão} + \text{Recall}}$$
  * **Modelo 1**:
    $$F_{1\text{ (Mod 1)}} = 2 \times \frac{0,95 \times 0,30}{0,95 + 0,30} = 2 \times \frac{0,285}{1,25} = \frac{0,57}{1,25} \approx 0,456 \text{ (ou } 45,6\%)$$
  * **Modelo 2**:
    $$F_{1\text{ (Mod 2)}} = 2 \times \frac{0,72 \times 0,70}{0,72 + 0,70} = 2 \times \frac{0,504}{1,42} = \frac{1,008}{1,42} \approx 0,710 \text{ (ou } 71,0\%)$$
* **Justificativa**: A média harmônica penaliza severamente equilíbrios desproporcionais entre Precisão e Recall. O baixo recall do Modelo 1 ($0,30$) derrubou fatalmente seu F1-Score, fazendo com que a barra do Modelo 2 seja amplamente superior no gráfico.

---

### Resolução 28
* **Origem do Erro Matemático (Armadilha da Variável Dummy)**:
  * Como todo cliente pertence a uma das quatro regiões, a soma das variáveis binárias em cada linha da matriz é sempre constante e igual a 1:
    $$D_{\text{Norte}} + D_{\text{Sul}} + D_{\text{Leste}} + D_{\text{Oeste}} = 1$$
  * Como a regressão linear com intercepto já inclui uma coluna de $1\text{s}$ para estimar $\beta_0$, cria-se uma dependência linear exata entre as colunas da matriz $\mathbf{X}$. A matriz $(\mathbf{X}^T \mathbf{X})$ torna-se singular (determinante nulo), tornando impossível computar sua inversa matricial $(\mathbf{X}^T \mathbf{X})^{-1}$.
* **Regra Fundamental**: Para qualquer variável categórica com $k$ categorias distintas, devem ser inseridas **estritamente $k - 1$ variáveis dummy** no modelo com intercepto. A categoria omitida torna-se a **categoria de referência base**.

---

### Resolução 29
* **Interpretação do Q-Q Plot**: O desvio em formato de "S" com caudas pontilhadas saindo da diagonal indica **Cauda Pesada / Leptocurtose**.
* **Impacto Teórico**: Os resíduos empíricos apresentam valores extremos nas extremidades com frequência muito maior do que seria previsto por uma distribuição Gaussiana pura. Isso viola a premissa de normalidade dos resíduos ($\epsilon_i \sim \mathcal{N}(0, \sigma^2)$). Em amostras pequenas, invalida os testes de significância $t$ e $F$; em amostras grandes, sugere que modelos de regressão robusta ou transformações de potência (Box-Cox) devem ser avaliados.

---

### Resolução 30
* **Centro e Dispersão**:
  * O centro da nuvem de pontos é transladado de modo que a nova média de todas as variáveis padronizadas fique rigorosamente fixada na **origem cartesiana $(0, 0)$**.
  * A dispersão em ambos os eixos passa a ser medida estritamente em **unidades de desvio-padrão**, com a grande maioria dos pontos contida no intervalo $[-3, +3]$.
* **Forma Geométrica**: **A forma geométrica, a correlação e a disposição relativa entre os pontos permanecem absolutamente inalteradas**. Trata-se de uma transformação linear afim, que preserva a estrutura geométrica dos dados.

---

## 🔴 Bloco 3: Nível Avançado e Decisão Estratégica (Exercícios 31 a 45)

### Resolução 31
1. **Evidência Visual no Gráfico de Resíduos**:
   * O gráfico de Resíduos versus Valores Ajustados exibe uma **curvatura parabólica em U perfeita**: resíduos fortemente positivos nas pontas e negativos no centro. Isso prova que o erro não é puramente aleatório e existe um componente curvilíneo sistemático não capturado pelo modelo de 1º grau.
2. **Por que um $R^2$ Alto não Garante Suficiência**:
   * O coeficiente $R^2 = 0,9910$ mede apenas a proporção da variância total explicada pela reta em relação à média, mas é **cego quanto ao viés de especificação do modelo**.
   * Ao incluir o termo $\text{altura}^2$, o $MSE$ caiu de $0,401$ para $0,024$ (uma redução de erro de $94\%$). Um modelo pode ostentar um $R^2$ superior a $99\%$ e, ainda assim, cometer erros de previsão sistemáticos que seriam inaceitáveis em aplicações de alta precisão. O diagnóstico gráfico de resíduos é hierarquicamente superior a uma métrica escalar isolada de $R^2$.

---

### Resolução 32
* **Cenário de Volume Diário**: $500.000$ pagamentos. Supondo uma taxa de fraude de $1\%$ ($5.000$ fraudes e $495.000$ legítimas):
1. **Ponto Operacional 1 ($\theta = 0,50$ — $\text{TPR}=0,80; \text{FPR}=0,02$)**:
   * Fraudes não detectadas ($FN$): $20\%$ de $5.000 = 1.000$ fraudes $\implies$ Prejuízo: $1.000 \times R\$ 3.200 = \mathbf{R\$ 3.200.000,00}$.
   * Falsos Alarmes ($FP$): $2\%$ de $495.000 = 9.900$ SMSs $\implies$ Custo: $9.900 \times R\$ 0,50 = \mathbf{R\$ 4.950,00}$.
   * **Custo Total Diário**: **$R\$ 3.204.950,00$**.
2. **Ponto Operacional 2 ($\theta = 0,10$ — $\text{TPR}=0,98; \text{FPR}=0,08$)**:
   * Fraudes não detectadas ($FN$): $2\%$ de $5.000 = 100$ fraudes $\implies$ Prejuízo: $100 \times R\$ 3.200 = \mathbf{R\$ 320.000,00}$.
   * Falsos Alarmes ($FP$): $8\%$ de $495.000 = 39.600$ SMSs $\implies$ Custo: $39.600 \times R\$ 0,50 = \mathbf{R\$ 19.800,00}$.
   * **Custo Total Diário**: **$R\$ 339.800,00$**.
* **Fundamentação da Decisão**: O banco deve implementar o **limiar $\theta = 0,10$**. A economia diária de fraudes evitadas é de quase $R\$ 2,9$ milhões, enquanto o custo adicional de envio de SMS é de apenas $R\$ 15$ mil. Em problemas de custos altamente assimétricos, operar com limiares baixos para maximizar o Recall é a única decisão economicamente justificável.

---

### Resolução 33
* **Efeito da Normalização Min-Max com Outlier Sentinela**:
  * Pela fórmula: $x_{\text{norm}} = \frac{x - x_{\min}}{x_{\max} - x_{\min}}$. Se $x_{\max} = 99,9$ e $x_{\min} = 10,0$:
  * Para uma temperatura normal de $20^\circ\text{C}$: $x_{\text{norm}} = \frac{20 - 10}{99,9 - 10} = \frac{10}{89,9} \approx 0,11$.
  * Para uma temperatura de $35^\circ\text{C}$: $x_{\text{norm}} = \frac{35 - 10}{89,9} = \frac{25}{89,9} \approx 0,28$.
  * **Consequência Visual**: Todas as variações reais e legítimas da temperatura atmosférica (de $10$ a $35^\circ\text{C}$) ficarão **espremidas e colapsadas em uma faixa microscópica entre $0,0$ e $0,28$**, perdendo toda a resolução de variância porque o código de erro $99,9$ usurpou a posição do extremo $1,0$.
* **Justificativa**: A limpeza de dados em [[Extração e Tratamento de Dados (ETL)|ETL]] (conversão de valores sentinelas para `NA`) deve **obrigatoriamente anteceder** a normalização por escala.

---

### Resolução 34
1. **Regra de 1 Erro-Padrão (1-SE Rule)**:
   * A regra estabelece que, devido à variabilidade inerente da validação cruzada, a árvore com o menor erro numérico pontual pode estar superajustando ligeiramente a amostra de validação. Portanto, busca-se a árvore mais à esquerda (menor número de nós, mais simples e restrita) cujo erro ainda esteja dentro do intervalo de tolerância estatística de $1$ desvio-padrão em relação ao erro mínimo.
2. **O que Visa Preservar**:
   * Preserva a **Parcimônia do Modelo (Navalha de Occam)** e a sua **capacidade de generalização**, além de produzir árvores com menos regras de decisão, tornando o modelo dramaticamente mais interpretável e auditável para os tomadores de decisão de negócio.

---

### Resolução 35
1. **Premissa Violada**: **Ausência de Autocorrelação nos Erros** (independência estatística dos resíduos: $\text{Cov}(\epsilon_i, \epsilon_j) = 0$ para $i \neq j$).
2. **Teste Diagnóstico e Perigos**:
   * O teste clássico é o **Teste de Durbin-Watson** (valores próximos de $2$ indicam independência; valores próximos de $0$ indicam forte autocorrelação positiva).
   * O perigo é que a autocorrelação positiva gera erros-padrão gravemente subestimados, fazendo com que os intervalos de confiança sejam artificialmente estreitos, dando uma falsa sensação de certeza matemática a previsões de demanda voláteis.

---

### Resolução 36
1. **Conversão para Razão de Chances (*Odds Ratio*)**:
   $$\text{Odds Ratio} = e^{\hat{\beta}_1} = e^{0,1214} \approx 1,129$$
   * Isso significa que para cada ponto adicional na pontuação de crédito, as chances relativas de ter o empréstimo aprovado aumentam em approximately **$12,9\%$**.
2. **Impacto para um Acréscimo de 10 Pontos ($\Delta X = 10$)**:
   $$\text{Novo Fator} = e^{\hat{\beta}_1 \times \Delta X} = e^{0,1214 \times 10} = e^{1,214} \approx 3,367$$
   * Um aumento de $10$ pontos na pontuação multiplica as chances de aprovação por **$3,37$ vezes** (um aumento de **$+237\%$** nas chances).

---

### Resolução 37
* **O que Representa a Interseção**: Representa o limiar de corte $\theta^*$ onde a **Sensibilidade (Recall) é exatamente igual à Especificidade** ($\text{TPR} = \text{TNR}$).
* **Contexto Operacional**: É a escolha ideal em situações onde:
  1. As duas classes estão razoavelmente equilibradas na população;
  2. Os **custos econômicos de cometer um Erro do Tipo I ($FP$) ou um Erro do Tipo II ($FN$) são aproximadamente equivalentes**. Nenhum dos dois lados possui gravidade desproporcional.

---

### Resolução 38
* **Aceitabilidade em Saúde Pública**: **Totalmente inaceitável!**
* **Justificativa do Risco**: Em vigilância sanitária, um falso positivo significa classificar água contaminada ($0$) como segura/potável ($1$). A especificidade atual de apenas $54\%$ significa que quase a metade ($46\%$) de todas as fontes de água impróprias serão distribuídas à população como se fossem limpas, desencadeando epidemias de transmissão hídrica.
* **Ajuste Exigido no Modelo**: Deve-se **elevar severamente o limiar de decisão $\theta$** (por exemplo, para $\theta = 0,85$ ou $0,90$). Dessa forma, o algoritmo só liberará uma fonte para consumo se tiver quase certeza matemática absoluta de potabilidade, empurrando a Especificidade para próximo de $98\%$ e minimizando os falsos positivos a níveis residuais seguros.

---

### Resolução 39
* **Patologia Ocorrida**: **Separação Completa / Quase-Completa (*Complete Separation*)**.
* **Por que o MLE Falha**: O estimador de Máxima Verossimilhança tenta encontrar coeficientes $\boldsymbol{\beta}$ que maximizem a probabilidade dos dados observados. Como há uma linha divisória perfeita no ponto $X = 50$, o algoritmo busca produzir uma probabilidade de $0,0$ para $X < 50$ e $1,0$ para $X \ge 50$. Para a função logística se transformar em um degrau perfeitamente vertical, a inclinação $\beta_1$ precisa convergir para **$+\infty$**. O algoritmo não converge (*divergência numérica*), emitindo erros de variância infinita.
* **Solução Técnica**: Aplicar **Regularização $L_2$ (Regressão de Ridge)**, regularização elástica, ou utilizar a correção de viés de penalização de Firth (`logistf` no R).

---

### Resolução 40
1. **Interpretação da Importância de Variáveis**:
   * O teor de `Álcool` e a `Acidez Volátil` respondem conjuntamente por **$75\%$ de toda a capacidade discriminatória** do modelo na redução de impureza. São os pilares fundamentais da modelagem.
2. **Candidatos ao Expurgo**:
   * `Açúcar Residual` ($2\%$) e `Sulfatos` ($5\%$) possuem contribuição preditiva marginal desprezível. Podem ser eliminados sem qualquer perda perceptível na acurácia do modelo, reduzindo o custo de sensores, o tempo de inferência e a memória necessária no dispositivo embarcado.

---

### Resolução 41
* **Por que a Média é Maior que a Mediana**: A média aritmética incorpora o valor numérico de todos os pontos da amostra ($\bar{X} = \frac{1}{n} \sum X_i$). A presença de executivos com salários de centenas de milhares ou milhões de reais distorce e "puxa" a média fortemente para a direita na cauda longa. A mediana, por sua vez, depende estritamente da **ordem posicional**, mantendo-se imutável frente à magnitude dos extremos.
* **Medida Mais Fidedigna**: A **Mediana**. Ela reflete o salário do indivíduo que ocupa exatamente a posição de $50\%$ da hierarquia da empresa, sendo a medida de tendência central estatisticamente recomendada para distribuições com forte assimetria positiva.

---

### Resolução 42
* **Razão Matemática**:
  * As Árvores de Decisão constroem suas regras avaliando **uma única variável por vez** em cada nó divisor (critério univariado), na forma $X_j \le c$.
  * No espaço cartesiano, a equação $X_1 = c$ representa uma reta estritamente vertical, e $X_2 = c$ representa uma reta estritamente horizontal. Como resultado, todas as regiões de decisão formadas por árvores univariadas são necessariamente **retângulos e hiperblocos com bordas paralelas aos eixos cartesianos**, sem capacidade nativa de gerar diagonais suaves a menos que sejam combinadas em dezenas de cortes em escadaria.

---

### Resolução 43
* **Por que a Curva ROC Mascara o Fraco Desempenho**:
  * O eixo horizontal da curva ROC é a Taxa de Falsos Positivos: $\text{FPR} = \frac{FP}{FP + TN}$.
  * Em uma base onde há $1.000.000$ de negativos reais ($TN$), se o modelo emitir $10.000$ alarmes falsos ($FP$), o cálculo resultará em:
    $$\text{FPR} = \frac{10.000}{10.000 + 1.000.000} \approx 0,0099 \text{ (menos de } 1\%)$$
  * O gráfico ROC mostrará um ponto muito próximo de zero no eixo $X$, fazendo o modelo parecer excelente ($\text{AUC} = 0,98$).
* **Por que a Curva Precision-Recall é Mais Fidedigna**:
  * A Precisão avalia diretamente a experiência do usuário que lê os resultados: $\text{Precisão} = \frac{TP}{TP + FP}$.
  * Se o modelo capturou $80$ dos $100$ contratos ($TP = 80$) gerando os mesmos $10.000$ alarmes falsos:
    $$\text{Precisão} = \frac{80}{80 + 10.000} \approx 0,0079 \text{ (menos de } 1\%)$$
  * O advogado terá que ler mais de cem documentos inúteis para cada contrato relevante que encontrar. A curva PR expõe esse colapso imediatamente.

---

### Resolução 44
1. **O que Caracteriza o Ponto Influente**:
   * O ponto possui simultaneamente **alto resíduo padronizado** (desvio vertical grande em relação à previsão do modelo) e **alta alavancagem / leverage** (valores de preditores $X$ muito distantes do centro da massa de dados). A Distância de Cook ($D > 1,0$) comprova matematicamente que a remoção desse único ponto provocará uma alteração drástica nas estimativas de todos os coeficientes $\boldsymbol{\beta}$ do modelo.
2. **Recomendação Rigorosa de Ação**:
   * **Nunca deletar sumariamente o ponto sem investigação prévia!**
   * Deve-se conduzir uma apuração de causa-raiz: se for um erro material de digitação (ex: digitar 1.000 em vez de 10), corrige-se o valor. Se for uma fraude genuína ou um cliente real excepcional, o ponto deve ser mantido, justificando-se a modelagem separada ou o uso de técnicas de regressão robusta que minimizem a influência de pontos extremos.

---

### Resolução 45
* **Diagnóstico Técnico Executivo dos 3 Problemas Estruturais**:
  1. **Sobreajuste Severo (*Overfitting*)**: A discrepância massiva entre o desempenho no conjunto de treino ($R^2 = 0,985$) e no conjunto de teste ($R^2 = 0,520$) prova que o modelo memorizou ruídos amostrais e não possui capacidade de generalização no mundo real.
  2. **Violação da Premissa de Linearidade**: O padrão em parábola nítida no gráfico de Resíduos vs Ajustados comprova erro sistemático de especificação funcional.
  3. **Multicolinearidade Crítica entre Preditores**: A correlação bivariada de $r = 0,94$ entre dois preditores gera instabilidade numérica, infla os erros-padrão e prejudica a inferência causal.

* **As 3 Ações Corretivas Mandatórias**:
  1. **Simplificar e Regularizar o Modelo**: Aplicar penalização (Lasso ou Ridge) ou podar a complexidade do algoritmo para fechar a lacuna de erro entre treino e teste.
  2. **Inserir Termos Não Lineares**: Adicionar termos polinomiais de 2º grau ($X^2$) ou transformar variáveis com $\ln(X)$ para eliminar o padrão parabólico dos resíduos.
  3. **Expurgar Preditores Redundantes**: Remover uma das duas variáveis altamente correlacionadas ($r = 0,94$) ou combiná-las via Análise de Componentes Principais (PCA) antes do ajuste final.

---

## 🟣 Bloco 4: Seção Especial — Complexidade Polinomial, Erro Absoluto Médio e One-Hot Encoding (Exercícios 46 a 51)

### Resolução 46
1. **Comportamento na Potência 1 (Subajuste / Underfitting)**:
   * Ambas as curvas (treino e validação) iniciam em patamares muito elevados de erro ($EAM \approx 50.600$ a $50.750$), posicionadas lado a lado. Isso diagnostica o **Subajuste (*Underfitting*)**. Um modelo puramente linear de 1º grau impõe um hiperplano hiper-rígido que não tem flexibilidade para modelar a topografia geográfica e a curvatura real dos preços imobiliários.
2. **Ponto Ótimo sem Variáveis Categóricas**:
   * O erro de validação atinge seu ponto mais baixo absoluto na **Potência 6**, registrando $EAM_{\text{valid}} = 45.412$.
3. **Comportamento a partir da Potência 7 até a 9**:
   * Observa-se a manifestação clássica do **Sobreajuste (*Overfitting*) / Efeito Tesoura**: o erro no conjunto de treinamento continua caindo lentamente (de $44.868$ até $44.570$ na 9ª potência), mas o erro no conjunto de validação **passa a subir e descola bruscamente**, atingindo quase $51.000$ ($50.999$) na potência 9. O modelo passou a memorizar ruídos amostrais específicos do treino, perdendo a capacidade de generalizar para dados novos.

---

### Resolução 47
* **Por que as Linhas com One-Hot Encoding estão Sistematicamente Abaixo**:
  * As curvas tracejadas (com OHE) operam em patamares de erro substancialmente inferiores em todas as potências porque a inclusão das variáveis dummy indicadoras de localização (`prox_oceano`: `oc_1hora`, `oc_baia`, `oc_interior`, `oc_litoral`) injetou **informação discriminatória espacial qualitativa indispensável**.
  * Variáveis contínuas métricas isoladas (como área construída ou número de cômodos) são incapazes de capturar o valor de localização: um imóvel idêntico situado de frente para a praia (*litoral*) vale dramaticamente mais do que no *interior*. Ao incorporar as dummies de localização via One-Hot Encoding, o modelo reduz o erro absoluto médio de ponta a ponta em todos os graus polinomiais.

---

### Resolução 48
1. **Diagnóstico da Potência 1 (Alto Viés / Underfitting)**:
   * O modelo de 1ª potência peca por excesso de rigidez matemática (alto viés). O indicador visual é que **tanto o erro de treino quanto o erro de validação são muito altos e colados**, demonstrando que o algoritmo não conseguiu capturar nem mesmo a estrutura interna do conjunto de treino.
2. **Diagnóstico da Potência 9 (Alta Variância / Overfitting)**:
   * O modelo de 9ª potência possui excesso desmedido de flexibilidade e graus de liberdade devido à inclusão de dezenas de termos elevados a potências astronômicas ($X^9$). O indicador visual no gráfico é o **afastamento divergente entre as linhas**: o erro de treino atinge o menor patamar de toda a análise ($44.570$), enquanto o erro de validação explode para o pior patamar ($50.999$), abrindo um hiato de mais de $6.400$ pontos de erro entre treino e teste.

---

### Resolução 49
* **Fundamentação Técnica para Rejeitar a 9ª Potência e Escolher a 5ª Potência com OHE**:
  * A premissa norteadora da Ciência de Dados dita que **a seleção de modelos JAMAIS deve ser baseada no menor erro no conjunto de treinamento**. O erro de treino mede apenas a capacidade do algoritmo de "decorar" os dados já vistos.
  * A verdadeira capacidade preditiva no mundo real é apurada exclusivamente sobre o **conjunto de validação/teste**.
  * No gráfico de validação com OHE, o erro atinge seu **mínimo global na 5ª Potência ($EAM = 44.559$)**. A partir da 6ª potência, o erro de validação passa a subir ($44.747 \to 45.337 \to 50.452$). Se a empresa escolhesse o modelo de 9ª potência, teria previsões financeiras muito piores na prática. Portanto, o modelo da **5ª Potência com One-Hot Encoding** é a única escolha técnica e estatisticamente correta.

---

### Resolução 50
1. **Quantidade de Dummies e Regra Fundamental ($k - 1$)**:
   * Para uma variável categórica contendo $k = 5$ classes, são criadas exatamente **$k - 1 = 4$ colunas binárias** no modelo com intercepto (`oc_1hora`, `oc_baia`, `oc_interior`, `oc_litoral`). A quinta categoria (`ILHA`) é omitida intencionalmente para servir como a **categoria base de referência**, evitando a redundância matemática e a singularidade da matriz de dados (a **Armadilha da Dummy**).
2. **Por que Variáveis Dummy NÃO são Elevadas a Potências**:
   * Uma variável dummy binária só pode assumir os valores discretos $0$ ou $1$.
   * Pela álgebra elementar:
     $$0^p = 0 \quad \text{e} \quad 1^p = 1, \quad \forall p \in \mathbb{N}$$
   * Elevar uma dummy ao quadrado ($D^2$), ao cubo ($D^3$) ou à 9ª potência ($D^9$) gera uma coluna idêntica à coluna original $D$. Tentar incluir $D$ e $D^2$ no mesmo modelo geraria **colinearidade perfeita instantânea ($r = 1,00$)**, inviabilizando a inversão da matriz $(\mathbf{X}^T \mathbf{X})^{-1}$. Por isso, as dummies entram no modelo exclusivamente na sua forma linear fixa de 1º grau.

---

### Resolução 51
1. **Conceito de Linha de Base (*Baseline*)**:
   * Representa o erro de um **modelo ingênuo de referência**, que não utiliza preditores nem esforço de aprendizado de máquina — por exemplo, prever simplesmente a mediana ou média geral de preços para todos os distritos da Califórnia ($EAM \approx 50.747$). Todo modelo supervisionado precisa obrigatoriamente operar bem abaixo da linha de baseline para comprovar que adiciona valor analítico real.
2. **Significado do Ponto de Ruptura na Potência 9**:
   * Quando o erro de validação da 9ª potência ($50.999$) cruza a linha de baseline para cima, ocorre o colapso total do modelo: a modelagem com termos polinomiais de grau 9 tornou-se **tão ruidosa, instável e distorcida que utilizá-la em novos dados é pior do que simplesmente chutar a média de olhos fechados**! O modelo perdeu completamente qualquer utilidade prática.
