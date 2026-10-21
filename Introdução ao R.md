---
aliases:
  - R
  - Linguagem R
  - Programação em R
  - Data Frames em R
tags:
  - programacao
  - r
  - data-science
  - fundamentos
---

# Introdução ao R

A linguagem **R** é um ambiente computacional e de programação interpretado, amplamente adotado no meio acadêmico e na indústria para análise estatística, mineração de dados, visualização gráfica e [[Aprendizado de Máquina]]. Desenvolvida inicialmente por Ross Ihaka e Robert Gentleman na Universidade de Auckland, a linguagem deriva do clássico **S** e é distribuída como software livre sob a licença GNU GPL pelo projeto CRAN (Comprehensive R Archive Network).

No contexto de [[Fundamentos de Ciência de Dados]], o R se destaca pelo ecossistema nativo orientado a matrizes, vetores e [[Data Frames]], permitindo que analistas realizem manipulações complexas de dados com sintaxe concisa e operações altamente vetorizadas.

---

## 1. Características Fundamentais da Linguagem

Para compreender o funcionamento do R e evitar erros comuns durante a manipulação de dados, é crucial conhecer suas premissas arquiteturais:

- **Linguagem Interpretada**: As instruções são executadas linha a linha por um interpretador interativo, sem necessidade de etapa prévia de compilação.
- **Tipagem Dinâmica e Fraca**: As variáveis não exigem declaração explícita de tipos. O tipo de uma variável é determinado dinamicamente pelo valor atribuído a ela. Se necessário, o interpretador realiza coerção automática de tipos.
- **Sensibilidade a Caixa (*Case Sensitive*)**: Nomes de variáveis e funções diferenciam maiúsculas de minúsculas. Ou seja, `variavel != Variavel` e `a != A`.
- **Indexação Baseada em 1 (*1-based indexing*)**: Diferente de linguagens como Python e C, onde o primeiro índice de uma coleção é `0`, em R a contagem de elementos inicia sempre no índice **1** (`vetor[1]`).
- **Inexistência de Escalares Primitivos**: Em R, mesmo um número isolado como `x <- 10` é, na realidade, um **vetor** de comprimento unitário (`length(x) == 1`).
- **Operador Ponto (`.`) versus Cifrão (`$`):**
  - O ponto `.` em R **não** representa acesso a métodos (como na orientação a objetos de Java ou Python), sendo apenas um caractere válido para compor nomes de variáveis (exemplo: `dados.treino` ou `media.altura`).
  - O operador cifrão `$` é o operador reservado para acessar colunas específicas dentro de uma lista ou de um [[Data Frames]] (exemplo: `paciente$idade`).

---

## 2. Sintaxe Básica, Atribuição e Comentários

### Atribuição de Variáveis
A convenção recomendada e idiomática em R para atribuição de valores é o operador seta `<-`. Embora o operador de igualdade `=` também funcione na maioria dos casos, ele possui sobrecarga sintática em argumentos de funções, tornando o `<-` a prática preferencial e livre de ambiguidades.

```r
# Atribuição recomendada
largura <- 10.0
profundidade <- 20.5
altura <- 2.0

# Cálculo derivado
volume <- largura * profundidade * altura
print(volume)
```

### Comentários e Boas Práticas
Linhas de comentário iniciam com o caractere cerquilha `#`. Recomenda-se utilizar nomes descritivos em minúsculas separados por sublinhado `_` (snake_case) para variáveis complexas (exemplo: `dados_limpos_2026`).

### Sistema de Ajuda Integrado
O R disponibiliza uma documentação interna rica e acessível diretamente pelo console:

```r
# Consulta a documentação de uma função específica
?plot
help(lm)

# Pesquisa textual por termos na documentação completa
??regression
help.search("logistic")

# Demonstrações práticas e exemplos executáveis
demo(graphics)
example(matrix)
```

---

## 3. Tipos Básicos de Dados (Atômicos)

O R trabalha com quatro tipos atômicos principais:

| Tipo | Descrição | Exemplo | Verificação de Tipo |
| :--- | :--- | :--- | :--- |
| **Numeric (Double)** | Números reais de ponto flutuante (padrão numérico) | `x <- 3.1415` | `class(x)` $\to$ `"numeric"` |
| **Integer** | Números inteiros estritos (declarados com sufixo `L` ou convertidos) | `n <- 42L` ou `as.integer(42)` | `is.integer(n)` $\to$ `TRUE` |
| **Character** | Cadeias de caracteres (textos delimitados por aspas simples ou duplas) | `nome <- "Ciência de Dados"` | `class(nome)` $\to$ `"character"` |
| **Logical** | Valores booleanos (`TRUE` ou `FALSE`, abreviados como `T` ou `F`) | `ativo <- TRUE` | `is.logical(ativo)` $\to$ `TRUE` |

### Coerção Automática de Tipos
Quando elementos de tipos diferentes são agrupados na mesma estrutura atômica, o R aplica uma hierarquia rígida de coerção para preservar a integridade:

$$\text{logical} \longrightarrow \text{integer} \longrightarrow \text{numeric} \longrightarrow \text{character}$$

```r
# Coerção lógica para numérica
casado <- TRUE
resultado <- casado + 4  # TRUE é convertido para 1
print(resultado)         # Retorna 5

# Coerção mista em vetor atômico
v1 <- c(5, 1.7, TRUE)
print(v1) # [1] 5.0 1.7 1.0 (todos convertidos para numeric)

v2 <- c(5, 1.7, TRUE, "IFSP")
print(v2) # [1] "5" "1.7" "TRUE" "IFSP" (todos convertidos para character)
```

---

## 4. Estruturas de Dados Essenciais

### 4.1. Vetores (*Vectors*)
O vetor é a estrutura elementar do R. Todos os seus elementos devem obrigatoriamente possuir o **mesmo tipo de dado**.

#### Criação de Vetores
Utiliza-se a função concatenadora `c()`:

```r
# Vetor numérico
idades <- c(18, 22, 25, 40, 33)

# Vetor de caracteres
cidades <- c("São Paulo", "Presidente Epitácio", "Campinas", "Santos")

# Geração de sequências numéricas
seq1 <- 1:10                       # Inteiros de 1 a 10
seq2 <- seq(from = 0, to = 1, by = 0.2)     # [0.0, 0.2, 0.4, 0.6, 0.8, 1.0]
seq3 <- seq(from = 0, to = 10, length.out = 5) # 5 elementos linearmente espaçados
repeticao <- rep(c(1, 2), times = 3)         # [1, 2, 1, 2, 1, 2]
```

#### Indexação e Fatiamento de Vetores
A indexação em R é altamente flexível e suporta números positivos, negativos e expressões booleanas:

```r
frutas <- c("Maçã", "Banana", "Laranja", "Uva", "Manga")

# Acesso por posição (1-based)
frutas[1]       # "Maçã"
frutas[c(2, 4)] # "Banana", "Uva"

# Indexação negativa: remove os elementos indicados
frutas[-2]      # "Maçã", "Laranja", "Uva", "Manga" (exclui o índice 2)
frutas[-c(1, 5)]# "Banana", "Laranja", "Uva"

# Indexação condicional lógica (Filtragem booleana)
valores <- c(10, 45, 22, 89, 15, 60)
filtro <- valores > 30
valores[filtro] # 45, 89, 60
```

#### Operações Vetorizadas
No R, funções matemáticas e operadores aritméticos operam nativamente sobre vetores inteiros sem a necessidade de loops `for` explícitos:

```r
renda <- c(1500, 2800, 4200, 8900)
gasto <- c(1200, 3100, 3900, 6500)

# Operação elemento a elemento
razao_comprometimento <- gasto / renda
inadimplente <- razao_comprometimento > 1.0

print(razao_comprometimento)
print(inadimplente) # FALSE, TRUE, FALSE, FALSE
```

---

### 4.2. Fatores (*Factors*)
Fatores são estruturas especializadas para armazenar **variáveis categóricas** (nominais ou ordinais), fundamentais na construção de modelos de [[Regressão Linear]], [[Regressão Logística]] e [[Árvores de Decisão]]:

```r
# Criação de fator nominal
escolaridade <- factor(c("médio", "superior", "médio", "pós-graduação"))
print(levels(escolaridade))

# Fator ordinal com hierarquia explícita
nivel <- factor(c("baixo", "alto", "médio", "alto"),
                levels = c("baixo", "médio", "alto"),
                ordered = TRUE)
print(nivel[1] < nivel[2]) # Retorna TRUE
```

---

### 4.3. Matrizes (*Matrices*)
Matrizes são coleções bidimensionais homogêneas (linhas $\times$ colunas), muito utilizadas no cálculo numérico e em formulações algébricas como os Mínimos Quadrados Ordinários em [[Regressão Linear]]:

```r
# Criação de matriz por coluna (padrão)
m1 <- matrix(1:6, nrow = 2, ncol = 3)
#      [,1] [,2] [,3]
# [1,]    1    3    5
# [2,]    2    4    6

# Criação de matriz por linha
m2 <- matrix(1:6, nrow = 2, ncol = 3, byrow = TRUE)
#      [,1] [,2] [,3]
# [1,]    1    2    3
# [2,]    4    5    6

# Operações matriciais
soma_m <- m1 + m2              # Soma elemento a elemento
prod_elem <- m1 * m2           # Multiplicação elemento a elemento

# Multiplicação matricial algébrica (%*%)
m_a <- matrix(c(1, 2, 3, 4), nrow = 2, ncol = 2)
m_b <- matrix(c(5, 6, 7, 8), nrow = 2, ncol = 2)
prod_matricial <- m_a %*% m_b  # Produto de matrizes

# Transposta de uma matriz
m_transposta <- t(m_a)
```

---

### 4.4. Data Frames (Estrutura Principal de Dados)
O **Data Frame** é a estrutura bidimensional heterogênea fundamental em R. Cada coluna representa uma variável (que pode ser de tipo diferente: numérico, texto, fator) e cada linha representa uma observação ou registro.

#### Construção de um Data Frame

```r
# Vetores individuais
nomes <- c("Alice", "Bernardo", "Carla", "Daniel", "Eduarda")
idades <- c(24, 30, 22, 28, 35)
nota_final <- c(8.5, 5.0, 7.2, 9.1, 6.0)
frequencia <- c(0.85, 0.70, 0.90, 0.95, 0.78)

# Criação do Data Frame
alunos <- data.frame(
  nome = nomes,
  idade = idades,
  nota = nota_final,
  freq = frequencia,
  stringsAsFactors = FALSE
)

# Inspeção inicial dos dados
str(alunos)     # Estrutura interna e tipos de cada coluna
summary(alunos) # Estatísticas descritivas básicas
dim(alunos)     # Dimensões (linhas x colunas)
head(alunos, 3) # Exibe as 3 primeiras linhas
```

#### Seleção e Filtragem em Data Frames

```r
# Acesso a coluna por nome via operador $
notas <- alunos$nota

# Acesso por coordenadas [linha, coluna]
alunos[1, 2]         # Idade da primeira linha
alunos[1:3, ]        # Linhas de 1 a 3, todas as colunas
alunos[, c("nome", "nota")] # Colunas específicas

# Criação de nova variável derivada
alunos$aprovado <- (alunos$nota >= 6.0) & (alunos$freq >= 0.75)

# Filtragem de observações condicionais
aprovados <- alunos[alunos$aprovado == TRUE, ]
print(aprovados[, c("nome", "nota", "freq")])
```

---

## 5. Gerenciamento de Memória e Workspace

O R mantém todos os objetos criados na memória RAM da sessão ativa. O controle eficiente desse espaço de trabalho (*workspace*) é essencial durante rotinas pesadas de [[Extração e Tratamento de Dados (ETL)]]:

```r
# Listar todas as variáveis presentes na memória
ls()

# Remover objetos específicos
rm(largura, profundidade, altura)

# Limpar completamente a memória RAM da sessão de trabalho
rm(list = ls())

# Salvar variáveis específicas em arquivo binário comprimido (.RData)
save(alunos, file = "dados_alunos.RData")

# Salvar toda a sessão ativa de trabalho
save.image(file = "workspace_completo.RData")

# Restaurar dados salvos previamente
load("dados_alunos.RData")
```

---

## 6. Integração com o Ecossistema de Ciência de Dados

O R se integra perfeitamente com ferramentas modernas de documentação e modelagem:
1. **Ambiente Interativo**: Executável via console interativo ou em cadernos no [[Ambiente de Desenvolvimento Jupyter]] por meio do kernel `IRkernel`.
2. **Engenharia e Limpeza**: Aplicação de expressões regulares e tratamento de valores ausentes em [[Extração e Tratamento de Dados (ETL)]].
3. **Modelagem Preditiva**: Funções estatísticas robustas como `lm()` para [[Regressão Linear]] e `glm()` para [[Regressão Logística]].
4. **Algoritmos Não Paramétricos**: Bibliotecas como `rpart` para construção de [[Árvores de Decisão]].
5. **Diagnóstico de Performance**: Avaliação de resultados por meio de métricas como [[Acurácia]], [[Recall]], [[Precisão]], [[F1-Score]] e [[Curva ROC]] em [[Métricas de Avaliação de Modelos]].
6. **Apresentação de Resultados**: Geração de relatórios estáticos e painéis visuais interativos documentados em [[Visualização de Dados com Plotly]].

---

## 7. Exercícios Práticos Resolvidos

### Exercício 1: Vetorização e Coerção
**Enunciado**: Crie um vetor com as receitas mensais de 5 filiais: `c(12000, 15500, 9800, 22000, 18400)` e os custos associados: `c(10000, 16000, 8500, 19000, 17000)`. Calcule o lucro de cada filial, identifique quais filiais deram prejuízo e calcule o lucro total acumulado.

```r
# Resolução
receitas <- c(12000, 15500, 9800, 22000, 18400)
custos   <- c(10000, 16000, 8500, 19000, 17000)

# Vetorização do lucro
lucro <- receitas - custos
prejuizo <- lucro < 0

cat("Lucro por filial:", lucro, "\n")
cat("Filiais com prejuízo (índices):", which(prejuizo), "\n")
cat("Lucro total da rede: R$", sum(lucro), "\n")
```

### Exercício 2: Manipulação de Data Frame e Agregação
**Enunciado**: Dado um conjunto com 4 funcionários contendo `departamento` e `salario`, adicione um bônus de 10% para funcionários de "Vendas" e 5% para os demais, calculando o novo salário líquido.

```r
# Resolução
funcionarios <- data.frame(
  id = 1:4,
  departamento = c("Vendas", "TI", "Vendas", "RH"),
  salario = c(4500, 7200, 5100, 3800),
  stringsAsFactors = FALSE
)

# Adicionando bônus condicional via ifelse
funcionarios$taxa_bonus <- ifelse(funcionarios$departamento == "Vendas", 0.10, 0.05)
funcionarios$bonus <- funcionarios$salario * funcionarios$taxa_bonus
funcionarios$salario_final <- funcionarios$salario + funcionarios$bonus

print(funcionarios)
```
