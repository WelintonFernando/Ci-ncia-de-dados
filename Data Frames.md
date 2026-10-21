---
aliases:
  - Data Frame
  - DataFrame
  - Data Frames em R
tags:
  - programacao
  - r
  - estruturas-de-dados
  - data-science
---

# Data Frames

O **Data Frame** é a estrutura de dados bidimensional mais proeminente e indispensável na linguagem [[Introdução ao R|R]] e na Ciência de Dados contemporânea. Trata-se de uma tabela heterogênea organizada em linhas e colunas, na qual cada coluna representa uma variável (que pode possuir seu próprio tipo de dado: numérico, texto, lógico ou fator) e cada linha corresponde a uma observação empírica ou registro do mundo real.

Ao contrário de uma **matriz** — que exige que todos os elementos pertençam estritamente ao mesmo tipo atômico —, o Data Frame espelha fielmente a natureza de tabelas relacionais de bancos SQL e planilhas de dados, servindo de base para todos os algoritmos de [[Aprendizado de Máquina]].

---

## 1. Criação e Inspeção de um Data Frame

A construção de um Data Frame no R é feita a partir de vetores alinhados de mesmo comprimento:

```r
# Vetores individuais representando atributos
nomes      <- c("Ana", "Bruno", "Carlos", "Diana", "Eduardo")
idades     <- c(25, 34, 28, 42, 31)
salarios   <- c(4500.50, 7200.00, 5100.80, 9800.00, 6300.20)
aprovado   <- c(TRUE, FALSE, TRUE, TRUE, FALSE)
setor      <- factor(c("TI", "Vendas", "TI", "Diretoria", "Vendas"))

# Instanciação do Data Frame
funcionarios <- data.frame(
  nome = nomes,
  idade = idades,
  salario = salarios,
  aprovado = aprovado,
  setor = setor,
  stringsAsFactors = FALSE
)

# Funções essenciais de diagnóstico
str(funcionarios)     # Estrutura interna detalhada e tipos de cada coluna
summary(funcionarios) # Medidas descritivas de resumo estatístico
dim(funcionarios)     # Dimensão da tabela (retorna: 5 linhas e 5 colunas)
head(funcionarios, 3) # Exibe as 3 primeiras linhas
tail(funcionarios, 2) # Exibe as 2 últimas linhas
names(funcionarios)   # Lista os nomes de todos os atributos
```

---

## 2. Acesso, Fatiamento e Indexação

O fatiamento de dados em Data Frames no R combina flexibilidade e poder expressivo:

### 2.1. Acesso a Colunas via Operador Cifrão (`$`)
O operador `$` extrai diretamente a coluna como um vetor atômico nativo:

```r
vetor_salarios <- funcionarios$salario
media_salarial <- mean(funcionarios$salario)
```

### 2.2. Acesso Bidimensional por Coordenadas `[linhas, colunas]`
```r
# Elemento específico (linha 2, coluna 3)
funcionarios[2, 3] # 7200

# Selecionar as linhas 1 a 3 de todas as colunas
funcionarios[1:3, ]

# Selecionar todas as linhas apenas de colunas específicas
funcionarios[, c("nome", "salario")]
```

### 2.3. Filtragem Condicional Lógica (Subsetting)
A filtragem de registros é realizada inserindo vetores booleanos na coordenada de linhas:

```r
# Filtrar apenas funcionários com salário superior a R$ 5.000
filtro_salario <- funcionarios$salario > 5000
altos_salarios <- funcionarios[filtro_salario, ]

# Múltiplas condições lógicas combinadas (& para E, | para OU)
selecao_ti <- funcionarios[funcionarios$setor == "TI" & funcionarios$idade < 30, ]
```

---

## 3. Manipulação, Adição e Exclusão de Variáveis

A engenharia de atributos tabulares é direta e intuitiva:

```r
# Adicionando uma nova coluna calculada
funcionarios$salario_anual <- funcionarios$salario * 12

# Modificando condicionalmente com ifelse()
funcionarios$categoria_salario <- ifelse(
  funcionarios$salario >= 7000, 
  "Executivo", 
  "Operacional"
)

# Removendo uma coluna atribuindo NULL
funcionarios$categoria_salario <- NULL
```

---

## 4. O Papel do Data Frame no Ciclo de Dados

O Data Frame é a entidade transversal sobre a qual operam todas as etapas analíticas do vault:
1. **[[Extração e Tratamento de Dados (ETL)]]**: A função `read.csv()` ou `read.table()` carrega arquivos tabulares diretamente na forma de Data Frames, sobre os quais aplicam-se remoção de nulos (`na.omit`) e filtros com expressões regulares;
2. **[[Pré-Processamento e Engenharia de Atributos]]**: Aplica-se padronização com `scale()` e codificação binária em colunas do Data Frame;
3. **Modelagem Preditiva**: O argumento `data = ...` nas funções `lm()` em [[Regressão Linear]], `glm()` em [[Regressão Logística]] e `rpart()` em [[Árvores de Decisão]] recebe obrigatoriamente um Data Frame como entrada de treino;
4. **[[Visualização de Dados com Plotly]]**: Colunas de Data Frames são mapeadas diretamente nos eixos $x$ e $y$ dos gráficos interativos.
