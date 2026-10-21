---
aliases:
  - Big Data
  - MapReduce
  - Sistemas Distribuídos
  - 5 Vs do Big Data
tags:
  - big-data
  - sistemas-distribuidos
  - computacao
  - arquitetura
---

# Big Data e Computação Distribuída

O termo **Big Data** designa o conjunto de tecnologias, arquiteturas e práticas analíticas desenvolvidas para capturar, armazenar, gerenciar e processar volumes massivos de dados que excedem a capacidade operacional dos sistemas de bancos de dados relacionais tradicionais. 

No contexto de [[Fundamentos de Ciência de Dados]], o surgimento do Big Data transformou radicalmente a indústria, exigindo uma transição de servidores centralizados de grande porte para arquiteturas de **computação distribuída** baseadas em aglomerados de servidores comerciais (*clusters*).

---

## 1. Evolução Histórica das Tecnologias de Dados

A gestão computacional de informações percorreu três grandes marcos históricos:

1. **Sistemas de Arquivos Planos (Décadas de 1950 a 1960)**: Armazenamento em arquivos sequenciais e fitas magnéticas, com alto acoplamento entre os programas e a estrutura física dos dados.
2. **Consolidação dos Bancos de Dados Relacionais (1970 a 2000)**: Introdução da álgebra relacional por Edgar F. Codd e criação da linguagem SQL. O modelo relacional impôs esquemas rígidos e integridade transacional ACID (Atomicidade, Consistência, Isolamento e Durabilidade), tornando-se o padrão da indústria por décadas.
3. **A Era do Big Data e da Web Social (2005 em diante)**: A explosão da Web 2.0 (YouTube, Facebook, Twitter), dispositivos móveis, sensores de IoT e a proliferação de dados não estruturados tornaram os bancos relacionais monolíticos financeiramente inviáveis para certas escalas. Surgiram o ecossistema **Apache Hadoop**, bancos de dados **NoSQL**, plataformas de computação em nuvem e bibliotecas de processamento distribuído.

---

## 2. Os 5 Vs do Big Data

O paradigma do Big Data é classicamente categorizado por cinco atributos fundamentais:

```
                          [VALOR]
                     Retorno de Negócio
                            ^
                            |
   [VOLUME]  <------- [VERACIDADE] -------> [VELOCIDADE]
  Escala Petabyte      Qualidade do Dado      Fluxos em Tempo Real
                            |
                            v
                      [VARIEDADE]
                Estruturado e Não Estruturado
```

### 2.1. Volume
- **Escala**: Os dados são mensurados em terabytes ($10^{12}$ bytes), petabytes ($10^{15}$ bytes) ou zetabytes ($10^{21}$ bytes).
- **Fato Marcante**: Estima-se que mais de 90% de todos os dados existentes no mundo foram gerados nos últimos dois anos, impulsionados por bilhões de interações sociais diárias, transmissões contínuas de vídeo e telemetria industrial.

### 2.2. Velocidade
- **Escala Temporal**: A velocidade em que novos dados são gerados, transmitidos e exigidos para tomada de decisão.
- **Processamento**: Transição do processamento tradicional em lote (*batch processing*) noturno para fluxos contínuos de dados em tempo real (*streaming processing* via Apache Kafka e Spark Streaming).

### 2.3. Variedade
- **Estruturados**: Dados tabulares com tipos e esquemas estritos pré-definidos (tabelas SQL, planilhas eletrônicas).
- **Semiestruturados**: Dados que possuem marcadores internos e hierarquias flexíveis, mas sem esquema relacional fixo (arquivos JSON, XML).
- **Não Estruturados**: Maior fatia dos dados corporativos (estimada em 80%), incluindo imagens, áudios, vídeos, postagens de texto livre em redes sociais, mensagens de chat e sinais de sensores brutos.

### 2.4. Veracidade
- **Confiabilidade**: Avalia a precisão, ruído, consistência e confiabilidade da fonte de dados. Dados poluídos, com anomalias ou originados de sensores defeituosos demandam rigorosas rotinas de saneamento descritas em [[Extração e Tratamento de Dados (ETL)]].

### 2.5. Valor
- **Impacto de Negócio**: O volume massivo de dados é inútil sem a capacidade de convertê-lo em vantagem competitiva, respostas preditivas de alta acurácia e redução de custos operacionais, articulados em [[Business Intelligence e Análise de Negócios]].

---

## 3. Comparativo Arquitetural: Centralizado, Replicado e Distribuído

Para contornar os limites físicos de escalabilidade vertical de um único servidor (*scale-up*), a computação moderna adota a escalabilidade horizontal (*scale-out*). A tabela a seguir sintetiza as diferenças estruturais entre os três modelos de arquitetura:

| Critério Analítico | Modelo Centralizado | Modelo Replicado | Modelo Distribuído |
| :--- | :--- | :--- | :--- |
| **Características** | Um repositório central único; processa requisições de todos os clientes. | Servidores espelhos contendo cópias idênticas integrais dos dados. | Múltiplos nós em cluster; cada servidor armazena e processa uma fração particionada dos dados. |
| **Capacidade de Armazenamento** | Limitada estritamente à capacidade de disco do servidor único. | Limitada à capacidade máxima de um único servidor (por guardar réplicas completas). | **Escalabilidade linear**: limitada apenas ao somatório de nós adicionados ao cluster. |
| **Fila de Requisições** | Fila única com gargalo na CPU e I/O do servidor central. | Distribuída entre o número de réplicas disponíveis. | Distribuída e balanceada dinamicamente entre todos os nós. |
| **Tempo de Atendimento** | Depende linearmente do volume concorrente de clientes conectados. | Depende da relação balanceada de clientes por réplica. | Otimizado via processamento paralelo local aos dados. |
| **Busca Indexada** | Simples e direta (árvores B-Tree locais). | Simples em cada réplica individual. | Complexa; exige catálogos distribuídos e roteamento de partição. |
| **Falhas Temporárias** | Interrompe o atendimento para **todos** os clientes da rede. | Atrasam resposta apenas para clientes conectados àquela réplica. | Toleradas automaticamente pelo remanejamento transparente de tarefas. |
| **Falhas Permanentes** | Perda catastrófica de dados, salvo se houver substituição de hardware e restauração de backup frio. | Tolerada com alta disponibilidade se houver ao menos uma réplica ativa. | Tolerada nativamente via fator de replicação interna de blocos (ex: HDFS replica cada bloco 3 vezes). |
| **Síntese de Escalabilidade** | **Não escala em armazenamento**; escala pouco em clientes. | **Não escala em armazenamento**; escala bem em número de leituras de clientes. | **Totalmente escalável em armazenamento e processamento**. |

---

## 4. O Paradigma MapReduce

Proposto pela Google e popularizado pelo ecossistema **Apache Hadoop**, o **MapReduce** é um modelo de programação distribuída inspirado nas funções de alta ordem `map` e `reduce` das linguagens de programação funcionais. O modelo abstrai a complexidade do particionamento de dados, tolerância a falhas, balanceamento de carga e comunicação entre nós de rede.

### 4.1. Filosofia de Operação
Em vez de trafegar petabytes de dados pela rede até o programa central (o que saturaria a infraestrutura de comunicação), o MapReduce envia o código de processamento (que tem poucos kilobytes) para ser executado diretamente nos nós onde os dados residem (*data locality*).

### 4.2. As Fases do Fluxo MapReduce

```
[Dados de Entrada Particionados]
               |
               v
       +---------------+
       |   Fase MAP    |  --> Executada em paralelo em cada nó
       +---------------+      Transforma registros em pares (chave, valor)
               |
               v
       +---------------+
       | SHUFFLE/SORT  |  --> Embaralha, agrupa e unifica todos os valores
       |  (Unificação) |      que possuem a mesma chave
       +---------------+
               |
               v
       +---------------+
       |  Fase REDUCE  |  --> Consolida as listas de valores de cada chave
       +---------------+      produzindo a saída agregada final
               |
               v
     [Resultado Consolidado]
```

1. **Map (Mapeamento)**: Cada nó lê sua fatia de dados brutos e aplica uma função que gera pares chave-valor intermediários:
   $$\text{Map}: (k_1, v_1) \longrightarrow \text{list}(k_2, v_2)$$
2. **Shuffle & Sort (Unificação / Embaralhamento)**: O framework coleta todos os pares intermediários gerados por todos os nós mapeadores, reordena-os e agrupa os valores por chave idêntica:
   $$\text{Shuffle}: \text{list}(k_2, v_2) \longrightarrow (k_2, \text{list}(v_2))$$
3. **Reduce (Redução)**: Nós redutores recebem uma chave e a lista consolidada de todos os valores a ela associados, agregando-os em um resultado conciso:
   $$\text{Reduce}: (k_2, \text{list}(v_2)) \longrightarrow \text{list}(k_3, v_3)$$

---

## 5. Estudo de Caso Prático: Identificação de Amigos em Comum

Considere uma rede social onde desejamos identificar todas as amizades em comum entre os usuários. Seja o grafo de conexões:
- **Ana**: amiga de `[Bet, Cal, Don]`
- **Bet**: amiga de `[Ana, Cal, Ely]`
- **Cal**: amigo de `[Ana, Bet, Don, Ely]`
- **Don**: amigo de `[Ana, Cal]`
- **Ely**: amiga de `[Bet, Cal]`

### Passo 1: Execução do Map
O mapeador processa a lista de amigos de cada usuário. Para cada par ordenado lexicograficamente entre o usuário e um de seus amigos, emite a chave composta do par e a lista restante de amizades:

- Processamento de **Ana** `[Bet, Cal, Don]`:
  - `(Ana, Bet)` $\to$ `[Bet, Cal, Don]`
  - `(Ana, Cal)` $\to$ `[Bet, Cal, Don]`
  - `(Ana, Don)` $\to$ `[Bet, Cal, Don]`
- Processamento de **Bet** `[Ana, Cal, Ely]`:
  - `(Ana, Bet)` $\to$ `[Ana, Cal, Ely]`
  - `(Bet, Cal)` $\to$ `[Ana, Cal, Ely]`
  - `(Bet, Ely)` $\to$ `[Ana, Cal, Ely]`
- Processamento de **Cal** `[Ana, Bet, Don, Ely]`:
  - `(Ana, Cal)` $\to$ `[Ana, Bet, Don, Ely]`
  - `(Bet, Cal)` $\to$ `[Ana, Bet, Don, Ely]`
  - `(Cal, Don)` $\to$ `[Ana, Bet, Don, Ely]`
  - `(Cal, Ely)` $\to$ `[Ana, Bet, Don, Ely]`

### Passo 2: Unificação (Shuffle & Group by Key)
O sistema agrupa todas as saídas emitidas que possuem exatamente a mesma chave:

- Chave `(Ana, Bet)`:
  - Lista: `{ [Bet, Cal, Don], [Ana, Cal, Ely] }`
- Chave `(Ana, Cal)`:
  - Lista: `{ [Bet, Cal, Don], [Ana, Bet, Don, Ely] }`
- Chave `(Bet, Cal)`:
  - Lista: `{ [Ana, Cal, Ely], [Ana, Bet, Don, Ely] }`

### Passo 3: Execução do Reduce
O redutor calcula a **interseção de conjuntos** das listas associadas a cada par de usuários:

$$\text{Amigos em Comum}(A, B) = \text{Amigos}(A) \cap \text{Amigos}(B)$$

- Para `(Ana, Bet)`:
  $$\{ \text{Bet}, \mathbf{Cal}, \text{Don} \} \cap \{ \text{Ana}, \mathbf{Cal}, \text{Ely} \} = \{ \mathbf{Cal} \}$$
  $\to$ **Amigo em comum**: `Cal`.
- Para `(Ana, Cal)`:
  $$\{ \mathbf{Bet}, \text{Cal}, \mathbf{Don} \} \cap \{ \text{Ana}, \mathbf{Bet}, \mathbf{Don}, \text{Ely} \} = \{ \mathbf{Bet}, \mathbf{Don} \}$$
  $\to$ **Amigos em comum**: `Bet` e `Don`.
- Para `(Bet, Cal)`:
  $$\{ \mathbf{Ana}, \text{Cal}, \mathbf{Ely} \} \cap \{ \mathbf{Ana}, \text{Bet}, \text{Don}, \mathbf{Ely} \} = \{ \mathbf{Ana}, \mathbf{Ely} \}$$
  $\to$ **Amigos em comum**: `Ana` e `Ely`.

Esse cálculo distribuído permite que uma rede com centenas de milhões de usuários encontre amizades em comum de forma paralela e horizontalmente escalável.

---

## 6. Governança e Boas Práticas em Ambientes de Big Data

1. **Alinhamento com Objetivos de Negócio**: Projetos de Big Data não devem ser guiados exclusivamente por tecnologia, mas ancorados em dores reais do negócio (redução de cancelamentos, previsão de fraudes, aumento de margem operacional).
2. **Centro de Excelência (CoE) em Dados**: Estruturar equipes multifuncionais para disseminar padrões arquiteturais, governança e catálogo de dados, superando a escassez crônica de talentos especializados.
3. **Harmonização de Dados**: Estabelecer mecanismos para cruzar tabelas estruturadas do Data Warehouse corporativo com registros semiestruturados de data lakes.
4. **Alinhamento com Computação em Nuvem**: Utilizar a separação entre poder de processamento (*compute*) e armazenamento de objetos (*storage*), permitindo desligar nós ociosos e otimizar custos.
