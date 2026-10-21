---
aliases:
  - ETL
  - Limpeza de Dados
  - Tratamento de Dados
  - Data Wrangling
  - Extração de Dados
tags:
  - etl
  - dados
  - data-wrangling
  - engenharia-de-dados
  - r
---

# Extração e Tratamento de Dados (ETL)

O processo de **ETL** (**E**xtração, **T**ransformação e **C**arga — *Extract, Transform, Load*) é a espinha dorsal de qualquer iniciativa em [[Fundamentos de Ciência de Dados]]. Trata-se da sequência metodológica encarregada de coletar dados brutos de fontes heterogêneas, sanear inconsistências, converter formatos e disponibilizar estruturas prontas para modelagem estatística e [[Aprendizado de Máquina]].

Estudos consolidados da indústria apontam que os profissionais de dados dedicam entre **50% e 80% do tempo de projeto** exclusivamente às tarefas de tratamento e limpeza de dados (*data wrangling*). Dados mal formatados, corrompidos ou com valores sentinelas não identificados comprometem fatalmente o desempenho de modelos como [[Regressão Linear]], [[Regressão Logística]] e [[Árvores de Decisão]] — princípio conhecido como *Garbage In, Garbage Out* (GIGO).

---

## 1. O Fluxo de Trabalho do ETL

```
+------------------+      +-------------------------+      +--------------------+
|  1. EXTRAÇÃO     |      |    2. TRANSFORMAÇÃO     |      |     3. CARGA       |
|  (Extract)       | ---> |    (Transform)          | ---> |     (Load)         |
| Fontes Brutas,   |      | Saneamento, Tipagem,    |      | Armazenamento em   |
| CSV, Logs, ZIP   |      | Regex, NA, Outliers     |      | .RData, Data Lake  |
+------------------+      +-------------------------+      +--------------------+
```

---

## 2. Fase 1: Extração (Obtenção dos Dados)

No ambiente [[Introdução ao R|R]], a extração envolve a leitura de arquivos tabulares locais, descompactação de arquivos comprimidos e requisições a bancos de dados.

### 2.1. Leitura de Arquivos Tabulares com `read.table` e `read.csv`
A função `read.table()` é a função genérica mais versátil para arquivos delimitados por texto:

```r
# Parâmetros críticos de importação
df <- read.table(
  file = "dados_brutos.csv",
  header = FALSE,          # Se a primeira linha contém os nomes das colunas
  sep = ";",               # Caractere delimitador de campos (ex: ';', ',', '\t')
  dec = ".",               # Caractere separador decimal
  colClasses = c("character", "numeric", "numeric"), # Tipos forçados das colunas
  na.strings = c("NA", "", "[ERRO]", "null"),       # Textos interpretados como NA
  skip = 0,                # Número de linhas ignoradas no início do arquivo
  stringsAsFactors = FALSE # Previne conversão automática indevida de texto para fator
)
```

### 2.2. Leitura Direta de Arquivos Comprimidos (.zip)
É comum trabalhar com arquivos históricos compactados. O R permite descompactar e ler dinamicamente:

```r
# Descompactação em tempo de execução e leitura
arquivo_extraido <- unzip("cepagri_2017_2022.zip", "cepagri.csv")
dados <- read.csv(arquivo_extraido, sep = ";", header = FALSE)

# Limpeza do arquivo temporário do disco
file.remove(arquivo_extraido)
```

---

## 3. Fase 2: Transformação e Saneamento de Dados

A etapa de transformação resolve defeitos estruturais e adequa as variáveis ao padrão analítico.

### 3.1. Manipulação Temporal: Conversão de Datas e Horas
Frequentemente, carimbos de tempo (*timestamps*) são lidos como simples cadeias de texto (`character`). Para habilitar ordenação cronológica e cálculos temporais, utilizamos a família de funções `POSIXct`:

```r
# Exemplo de carimbo de data lido como texto: "01/01/2017-00:10"
df$horario <- as.POSIXct(
  df$data_texto,
  format = "%d/%m/%Y-%H:%M",
  tz = "America/Sao_Paulo"
)

# Engenharia de atributos temporais derivados:
df$ano    <- as.numeric(format(df$horario, "%Y"))
df$mes    <- as.numeric(format(df$horario, "%m"))
df$dia    <- as.numeric(format(df$horario, "%d"))
df$hora   <- as.numeric(format(df$horario, "%H"))
df$minuto <- as.numeric(format(df$horario, "%M"))
```

### 3.2. Tratamento Textual e Expressões Regulares (Regex)
Quando arquivos brutos contêm registros defeituosos (como linhas de erro geradas por interrupção de comunicação de sensores), funções baseadas em expressões regulares realizam a identificação e expurgo:

```r
# Identificar linhas contendo o padrão textual "[ERRO]"
linhas_com_erro <- grep("\\[ERRO\\]", df$temperatura)

# Remover as linhas defeituosas via indexação negativa
if (length(linhas_com_erro) > 0) {
  df <- df[-linhas_com_erro, ]
}

# Substituição de vírgula decimal brasileira por ponto antes da conversão
df$preco_texto <- gsub(",", ".", df$preco_texto)
df$preco <- as.numeric(df$preco_texto)
```

### 3.3. Tratamento de Dados Ausentes (*Missing Data* — `NA`)
O R possui um valor reservado específico para dados ausentes: `NA` (*Not Available*):

- **Verificação de Nulos**:
  ```r
  # Vetor booleano indicando presença de NA
  is.na(df$temperatura)

  # Contagem total de NAs por coluna
  colSums(is.na(df))
  ```
- **Remoção de Linhas Incompletas**:
  ```r
  # Remove qualquer linha que possua ao menos um NA
  df_limpo <- na.omit(df)
  ```
- **Imputação Estatística**:
  ```r
  # Substituição de NA pela mediana da variável (resistente a outliers)
  mediana_temp <- median(df$temperatura, na.rm = TRUE)
  df$temperatura[is.na(df$temperatura)] <- mediana_temp
  ```

---

## 4. Detecção de Anomalias Físicas e Valores Sentinelas

Muitos sistemas legados e sensores de hardware utilizam **valores sentinelas** para indicar panes temporárias. Por exemplo, em estações agrometeorológicas como as do CEPAGRI/UNICAMP, a leitura `99.9` ou `999` era registrada automaticamente quando a sonda perdia calibração.

Além disso, variáveis físicas possuem restrições matemáticas teóricas:
- **Umidade Relativa do Ar**: Deve obedecer estritamente a $0\% \le U \le 100\%$. Valores como $103\%$ ou negativos devem ser expurgados.
- **Velocidade do Vento**: Não pode ser negativa e leituras anômalas superiores a limites de furacão (ex: $> 120\text{ km/h}$) devem ser investigadas.

```r
# Substituição de sentinelas de erro por NA
df$umidade[df$umidade == 99.9] <- NA
df$umidade[df$umidade > 100.0] <- NA

# Remoção de inconsistências físicas de vento
df$vento[df$vento < 0] <- NA
```

---

## 5. Estudo de Caso Prático 1: Estação Meteorológica CEPAGRI

No estudo de caso desenvolvido nos cadernos do curso, analisou-se o histórico meteorológico de 2017 a 2022 coletado a cada 10 minutos pelo CEPAGRI (UNICAMP).

### Pipeline de Limpeza Passo a Passo em R

```r
# 1. Preparação do ambiente
rm(list = ls())
library(repr)

# 2. Extração dos dados brutos
caminho <- "Material/CAP 2 - Mineração de dados/cepagri_2017_2022.zip"
arq <- unzip(caminho, "cepagri.csv")
df_bruto <- read.table(arq, sep = ";", header = FALSE, stringsAsFactors = FALSE)
file.remove(arq)

# Nomeando colunas
names(df_bruto) <- c("horario_txt", "temperatura_txt", "vento_txt", "umidade_txt", "sensacao_txt")

# 3. Filtragem de linhas com marcação [ERRO]
linhas_erro <- grep("\\[ERRO\\]", df_bruto$temperatura_txt)
if (length(linhas_erro) > 0) {
  df <- df_bruto[-linhas_erro, ]
} else {
  df <- df_bruto
}

# 4. Conversão de tipos
df$horario     <- as.POSIXct(df$horario_txt, format = "%d/%m/%Y-%H:%M", tz = "America/Sao_Paulo")
df$temperatura <- as.numeric(df$temperatura_txt)
df$vento       <- as.numeric(df$vento_txt)
df$umidade     <- as.numeric(df$umidade_txt)
df$sensacao    <- as.numeric(df$sensacao_txt)

# 5. Tratamento de limites físicos e sentinelas
df$umidade[df$umidade > 100] <- NA
df$sensacao[df$sensacao == 99.9] <- NA

# 6. Engenharia de Variável Física: Sensação Térmica (Wind Chill)
# Fórmula padronizada pelo National Weather Service dos EUA:
# T_wc = 13.12 + 0.6215*T - 11.37*(V^0.16) + 0.3965*T*(V^0.16)
calcular_sensacao <- function(temp, vento_kmh) {
  v_exp <- vento_kmh^0.16
  sens <- 13.12 + 0.6215 * temp - 11.37 * v_exp + 0.3965 * temp * v_exp
  return(sens)
}

# Aplicando para condições válidas de vento
df$sensacao_calculada <- ifelse(
  df$vento > 4.8 & df$temperatura <= 10.0,
  calcular_sensacao(df$temperatura, df$vento),
  df$temperatura
)
```

---

## 6. Estudo de Caso Prático 2: Vendas de Imóveis (King County)

No dataset `kc_house_data.csv`, a coluna `date` apresentava uma formatação composta: `"20141013T000000"`. Além disso, valores zerados em atributos como `bedrooms` e `bathrooms` em residências de grande área construída (`sqft_living`) configuravam anomalias cadastrais:

```r
# Carga dos dados de imóveis
kc <- read.csv("Material/Datasets/kc_house_data.csv", stringsAsFactors = FALSE)

# Extração de ano e mês a partir da string de data
kc$ano_venda <- as.numeric(substr(kc$date, 1, 4))
kc$mes_venda <- as.numeric(substr(kc$date, 5, 6))

# Filtragem de registros absurdos (ex: casas com 0 quartos e preço > R$ 1.000.000)
casas_anomalas <- which(kc$bedrooms == 0 & kc$price > 1000000)
if (length(casas_anomalas) > 0) {
  kc <- kc[-casas_anomalas, ]
}

# Cálculo do preço por metro quadrado construído (1 sqft ≈ 0.092903 m²)
kc$area_m2 <- kc$sqft_living * 0.092903
kc$preco_m2 <- kc$price / kc$area_m2
```

---

## 7. Fase 3: Carga e Persistência de Checkpoints

Em fluxos extensos de manipulação, recomenda-se salvar marcos intermediários (*checkpoints*) em arquivos binários `.RData`. Isso garante que, se um passo posterior falhar, não seja necessário reprocessar gigabytes de dados crus:

```r
# Salvando marcos do processo
save(df_bruto, file = "cepagri_00_captura.RData")
save(df, file = "cepagri_01_saneado.RData")

# Restaurando o ambiente limpo
rm(list = ls())
load("cepagri_01_saneado.RData")
```

Essa disciplina de engenharia de dados prepara adequadamente o conjunto de observações para as etapas de [[Pré-Processamento e Engenharia de Atributos]], viabilizando o treinamento eficiente de modelos em [[Regressão Linear]] e [[Regressão Logística]].
