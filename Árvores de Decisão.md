---
aliases:
  - Árvores de Decisão
  - Árvore de Decisão
  - Decision Trees
  - CART
  - Gini
  - Entropia
  - Ganho de Informação
  - Poda de Árvores
tags:
  - machine-learning
  - classificacao
  - arvores-de-decisao
  - r
---

# Árvores de Decisão

As **Árvores de Decisão** (*Decision Trees*) constituem uma das famílias de algoritmos mais intuitivas, poderosas e interpretáveis do [[Aprendizado de Máquina]] supervisionado. Aplicáveis tanto para tarefas de classificação (árvores de classificação) quanto para estimação contínua (árvores de regressão), elas segmentam o espaço de atributos em regiões retangulares hiperplanares por meio de uma sequência hierárquica de testes condicionais do tipo *"se-então"* (*if-then-else*).

Ao contrário de modelos paramétricos como a [[Regressão Linear]] e a [[Regressão Logística]], as árvores de decisão são **não paramétricas**: elas não exigem suposições prévias sobre a distribuição probabilística dos dados, capturam interações de alta ordem nativamente e são completamente invariantes a transformações monotônicas de escala em [[Pré-Processamento e Engenharia de Atributos]].

---

## 1. Anatomia e Estrutura Hierárquica

Uma árvore de decisão é composta por quatro elementos estruturais fundamentais:

```
               [NÓ RAIZ (Root)]
              (Teste: Crédito > 7.5?)
                  /          \
            Sim  /            \  Não
                v              v
        [NÓ INTERNO]         [FOLHA (Leaf)]
     (Renda > R$ 5.000?)     --> Classe 0 (Recusado)
         /        \
   Sim  /          \  Não
       v            v
 [FOLHA (Leaf)]   [FOLHA (Leaf)]
 --> Classe 1     --> Classe 0
   (Aprovado)       (Recusado)
```

1. **Nó Raiz (*Root Node*)**: É o nó superior inicial que contém todas as observações do conjunto de treino antes de qualquer divisão. Ele aplica o primeiro teste sobre o atributo mais discriminante.
2. **Nós Internos (*Internal/Decision Nodes*)**: Nós intermediários que possuem exatamente um nó ancestral e dois (ou mais) nós sucessores. Cada nó interno define uma regra de partição sobre um atributo específico.
3. **Ramos (*Branches*)**: Conexões direcionadas que representam cada desfecho possível do teste condicional aplicado no nó ancestral.
4. **Nós Folha ou Terminais (*Leaf/Terminal Nodes*)**: Nós finais que não possuem sucessores. Uma vez atingida uma folha, é atribuída à observação uma classe categórica final (pela classe majoritária) ou um valor numérico predito (pela média amostral da folha).

---

## 2. Medidas Matemáticas de Impureza de Nós

O objetivo central dos algoritmos de indução de árvores (como o **CART** — *Classification and Regression Trees*) é encontrar divisões que maximizem a **homogeneidade** (pureza) dos nós filhos. 

Seja $c$ o número total de classes da variável resposta e $p_i(t)$ a frequência relativa das observações da classe $i$ presentes no nó $t$:

$$p_i(t) = \frac{n_i(t)}{n(t)}$$

Onde $\sum_{i=1}^{c} p_i(t) = 1$. A literatura do curso analisa três medidas clássicas de impureza:

---

### 2.1. Entropia de Shannon (Entropy)
Originada da Teoria da Informação de Claude Shannon, mede a incerteza média contida na distribuição de probabilidades:

$$\text{Entropia}(t) = - \sum_{i=1}^{c} p_i(t) \cdot \log_2[p_i(t)]$$

*Convenção matemática*: se $p_i(t) = 0$, define-se $0 \cdot \log_2(0) = 0$.

- **Nó Perfeitamente Puro** (100% de uma só classe, $p_1 = 1, p_2 = 0$):
  $$\text{Entropia} = -(1 \cdot \log_2 1 + 0) = 0$$
- **Nó com Impureza Máxima** (divisão 50%/50% em 2 classes):
  $$\text{Entropia} = - \left( \frac{1}{2} \log_2 \frac{1}{2} + \frac{1}{2} \log_2 \frac{1}{2} \right) = - \left( 0,5 \cdot (-1) + 0,5 \cdot (-1) \right) = 1,0$$

---

### 2.2. Índice de Gini (Gini Impurity)
É o critério padrão adotado pelo pacote `rpart` em [[Introdução ao R|R]]. Mede a probabilidade de um elemento selecionado aleatoriamente do nó ser rotulado incorretamente se fosse classificado de acordo com a distribuição das classes no nó:

$$\text{Gini}(t) = 1 - \sum_{i=1}^{c} [p_i(t)]^2$$

- **Nó Perfeitamente Puro**:
  $$\text{Gini} = 1 - (1^2 + 0^2) = 0$$
- **Nó com Impureza Máxima** (divisão 50%/50% em 2 classes):
  $$\text{Gini} = 1 - \left( 0,5^2 + 0,5^2 \right) = 1 - (0,25 + 0,25) = 0,50$$

---

### 2.3. Erro de Classificação (Misclassification Error)
Mede a taxa de erro caso todas as observações do nó fossem atribuídas à sua classe majoritária:

$$\text{Erro}(t) = 1 - \max_{i} [p_i(t)]$$

- **Nó Puro**: $\text{Erro} = 1 - 1 = 0$;
- **Nó 50%/50%**: $\text{Erro} = 1 - 0,5 = 0,50$.

---

### Comparativo Numérico de Impureza (Exemplo dos Slides do Curso)

Considere quatro nós hipotéticos ($N_1, N_2, N_3, N_4$) contendo 6 observações de duas classes ($0$ e $1$):

| Nó | Contagem (Classe 0 : Classe 1) | Proporções ($p_0, p_1$) | Entropia | Índice Gini | Erro de Classificação |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **$N_1$** | $0 : 6$ (Puro) | $0,00$ ; $1,00$ | **$0,0000$** | **$0,0000$** | **$0,0000$** |
| **$N_2$** | $1 : 5$ (Quase puro) | $0,17$ ; $0,83$ | **$0,6500$** | **$0,2778$** | **$0,1667$** |
| **$N_3$** | $2 : 4$ | $0,33$ ; $0,67$ | **$0,9183$** | **$0,4444$** | **$0,3333$** |
| **$N_4$** | $3 : 3$ (Máxima impureza) | $0,50$ ; $0,50$ | **$1,0000$** | **$0,5000$** | **$0,5000$** |

---

## 3. Critério de Divisão: Impureza Coletiva e Ganho de Informação

Ao testar a partição de um nó ancestral $P$ (com $N$ observações) em $k$ nós filhos ($v_1, v_2, \dots, v_k$), onde cada filho $v_j$ recebe $N(v_j)$ observações, a **Impureza Coletiva da Divisão** ($I_{\text{split}}$) é a média ponderada das impurezas dos filhos:

$$I_{\text{split}} = \sum_{j=1}^{k} \frac{N(v_j)}{N} \cdot I(v_j)$$

O **Ganho de Informação** ($IG$ — *Information Gain*) gerado pela divisão é a redução líquida de impureza obtida:

$$IG = I(\text{nó pai}) - I_{\text{split}}$$

O algoritmo ganancioso (*greedy*) avalia exaustivamente todos os preditores e seleciona a divisão que **maximiza o Ganho de Informação** (ou equivalentemente, que minimiza $I_{\text{split}}$).

---

## 4. Partição de Diferentes Tipos de Atributos

### 4.1. Atributo Categórico Nominal Binário
Para variáveis com apenas dois níveis (ex: `sexo` $\in \{\text{"F"}, \text{"M"}\}$), o teste é direto:
- Ramo 1: $\text{sexo} = \text{"F"}$;
- Ramo 2: $\text{sexo} = \text{"M"}$.

### 4.2. Atributo Categórico com Múltiplos Níveis (Politômico)
Se o atributo possuir mais de duas categorias (ex: `educacao` $\in \{\text{"médio"}, \text{"superior"}, \text{"pós-graduação"}\}$), o algoritmo CART testa todas as combinações binárias possíveis de agrupamento (1 nível contra os demais):
- **Candidato A**: `educacao == "médio"` versus `{"superior", "pós"}`;
- **Candidato B**: `educacao == "superior"` versus `{"médio", "pós"}`;
- **Candidato C**: `educacao == "pós-graduação"` versus `{"médio", "superior"}`.

Calcula-se $I_{\text{split}}$ para cada candidato e seleciona-se a partição com menor impureza.

### 4.3. Atributo Numérico Contínuo
Para um atributo numérico contínuo $X$ (ex: `salario` ou `pont_credito`):
1. Ordenam-se as $N$ observações em ordem crescente: $x_{(1)} \le x_{(2)} \le \dots \le x_{(n)}$;
2. Identificam-se os pontos médios adjacentes entre observações com classes distintas como limiares de corte candidatos:
   $$c_m = \frac{x_{(m)} + x_{(m+1)}}{2}$$
3. Para cada limiar $c_m$, avalia-se o teste $X \le c_m$ versus $X > c_m$;
4. Escolhe-se o ponto de corte $c^*$ que gera a menor impureza coletiva dos filhos.

---

## 5. O Problema do Sobreajuste (*Overfitting*) e Mecanismos de Poda

Árvores de decisão não restringidas continuam crescendo até que cada folha contenha apenas uma observação (impureza zero). Esse comportamento gera um sobreajuste extremo: a árvore memoriza o ruído amostral do treino, obtendo $100\%$ de acurácia no treino, mas falha catastrófica ao prever dados inéditos de teste.

Para controlar a complexidade da árvore, utilizam-se duas estratégias:

```
        COMPLEXIDADE DA ÁRVORE (Número de Folhas / Profundidade)
Baixa (Underfitting) <-------------------------> Alta (Overfitting)
   Erro Alto no Treino                             Erro Zero no Treino
   Erro Alto no Teste                              Erro Enorme no Teste
                          [PONTO ÓTIMO DE PODA]
                       Menor Erro de Validação Cruzada
```

---

### 5.1. Pré-Poda (*Early Stopping*)
Interrompe o crescimento da árvore antes que ela se torne excessivamente complexa. No R, configura-se via função `rpart.control`:

```r
controle_prepoda <- rpart.control(
  minsplit = 20,   # Número mínimo de observações em um nó para tentar uma divisão
  minbucket = 7,   # Número mínimo obrigatório de observações em qualquer nó folha
  maxdepth = 5,    # Profundidade máxima permitida da árvore
  cp = 0.01        # Limiar de melhoria mínima no erro para justificar uma nova divisão
)
```

---

### 5.2. Pós-Poda por Complexidade de Custo (*Cost-Complexity Pruning*)
É a abordagem metodologicamente recomendada: permite-se que a árvore cresça completamente e, em seguida, removem-se os ramos inferiores que contribuem pouco para a acurácia geral.

A função de custo penalizada minimizada pelo algoritmo é:

$$R_\alpha(T) = R(T) + \alpha \cdot |T|$$

Onde:
- $R(T)$ é a taxa de erro da árvore nos dados;
- $|T|$ é o número de nós folha da árvore (complexidade);
- $\alpha \ge 0$ (denotado por `cp` — *Complexity Parameter* no R) é o fator de penalização: se $\alpha = 0$, a árvore completa é mantida; conforme $\alpha$ cresce, a árvore é progressivamente podada.

#### Seleção do Melhor Parâmetro de Complexidade em R
O R calcula o erro de validação cruzada para diferentes valores de `cp`:

```r
library(rpart)
library(rpart.plot)

# 1. Ajuste da árvore inicial completa
arvore_completa <- rpart(
  classe ~ ., 
  data = treino, 
  method = "class", 
  control = rpart.control(cp = 0.001)
)

# 2. Exibição da tabela e gráfico de validação cruzada
printcp(arvore_completa)
plotcp(arvore_completa)

# 3. Identificação automática do cp que minimizou o erro de validação cruzada (xerror)
cp_otimo <- arvore_completa$cptable[which.min(arvore_completa$cptable[, "xerror"]), "CP"]

# 4. Poda da árvore no ponto ótimo
arvore_podada <- prune(arvore_completa, cp = cp_otimo)

# 5. Visualização elegante da árvore podada
rpart.plot(arvore_podada, type = 2, extra = 104, under = TRUE, main = "Árvore de Decisão Otimizada")
```

---

## 6. Árvores com Ponderação e Matriz de Perda (*Loss Matrix*)

Em problemas com classes desbalanceadas ou onde erros possuem custos financeiros e humanos assimétricos (ex: fraude em seguros ou diagnóstico clínico), deixar passar uma fraude (Falso Negativo) custa muito mais caro do que investigar um cliente legítimo (Falso Positivo).

O pacote `rpart` permite definir uma **Matriz de Custo/Perda** (*Loss Matrix*):

```r
# Matriz de Perda: Linhas = Classe Real, Colunas = Classe Predita
# Formato: [Perda Real 0 -> Pred 0,  Perda Real 0 -> Pred 1 (FP)]
#          [Perda Real 1 -> Pred 0 (FN),  Perda Real 1 -> Pred 1]
matriz_perda <- matrix(c(0, 1, 10, 0), nrow = 2, byrow = TRUE)

# Treinamento com penalidade 10x maior para Falsos Negativos
arvore_ponderada <- rpart(
  fraude ~ ., 
  data = dados_seguro, 
  method = "class",
  parms = list(loss = matriz_perda)
)
```

Essa matriz força o algoritmo a selecionar pontos de corte mais conservadores que maximizam o [[Recall]] de fraudes, cujas métricas completas são avaliadas em [[Métricas de Avaliação de Modelos]].
