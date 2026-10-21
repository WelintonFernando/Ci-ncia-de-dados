---
aliases:
  - Sensibilidade
  - Revocação
  - True Positive Rate
  - TPR
tags:
  - metricas
  - avaliacao
  - classificacao
  - machine-learning
---

# Recall (Sensibilidade)

O **Recall** — também denominado na literatura técnica como **Sensibilidade** (*Sensitivity*), **Revocação** ou **Taxa de Verdadeiros Positivos** ($TPR$ — *True Positive Rate*) — é a métrica de desempenho que quantifica a capacidade de um classificador de **encontrar e capturar todas as ocorrências positivas reais** existentes no conjunto de dados.

Enquanto a [[Precisão]] se preocupa com a qualidade das predições emitidas pelo algoritmo (*"Quando o modelo diz que é positivo, ele acerta?"*), o Recall concentra-se na **abrangência da cobertura** do modelo (*"Deixamos escapar algum evento positivo importante?"*).

A análise do Recall é um dos pilares mais decisivos em [[Métricas de Avaliação de Modelos]], constituindo inclusive a coordenada do eixo vertical na construção gráfica da [[Curva ROC]].

---

## 1. Formulação Matemática

A partir dos quadrantes da [[Matriz de Confusão]]:
- **$TP$ (*True Positive*)**: Verdadeiros Positivos (casos positivos detectados com sucesso);
- **$FN$ (*False Negative*)**: Falsos Negativos (casos positivos reais que o modelo ignorou — Erro Tipo II).

O **Recall** é definido pela razão:

$$\text{Recall} = \frac{TP}{TP + FN}$$

Onde:
- O numerador $TP$ contabiliza os acertos positivos confirmados;
- O denominador $(TP + FN)$ representa o **universo total de casos positivos reais** existentes no mundo observado;
- O indicador varia de $0$ a $1$ (ou de $0\%$ a $100\%$).

---

## 2. Cenários Onde o Recall é a Métrica Primária

O Recall deve ser a métrica otimizada prioritariamente sempre que as consequências de um **Falso Negativo ($FN$)** forem potencialmente desastrosas, letais ou financeiramente irreparáveis.

```
                  CUSTO DE ERRO TIPO II (FALSO NEGATIVO) É CRÍTICO
                                         |
                                         v
                         MAXIMIZAÇÃO OBRIGATÓRIA DO RECALL
                                         |
               +-------------------------+-------------------------+
               |                                                   |
               v                                                   v
      DIAGNÓSTICO MÉDICO                                DETECÇÃO DE FRAUDES
Paciente doente liberado sem tratamento         Transação criminosa concluída
  -> Risco imediato de morte!                     -> Prejuízo financeiro direto!
```

### Casos de Aplicação Vital:
1. **Triagem Médica e Oncológica**:
   - Se um paciente possui uma neoplasia maligna e o teste prediz negativo ($FN$), o tratamento precoce é perdido, colocando a vida do indivíduo em risco extremo. Um falso alarme ($FP$), por sua vez, acarreta apenas um exame confirmatório adicional de biópsia.
2. **Segurança Cibernética e Detecção de Intrusões**:
   - Um ataque de ransomware ou vazamento de dados que passe despercebido ($FN$) pode paralisar as operações corporativas globais.
3. **Manutenção Preditiva Aeronáutica e Industrial**:
   - Não identificar uma fissura de fadiga em uma turbina de avião ($FN$) pode causar um acidente fatal.

---

## 3. O Trade-off com a Precisão

Para garantir que praticamente nenhum caso positivo passe despercebido (maximizando o Recall próximo a $100\%$):
- Reduz-se propositalmente o limiar de corte ($\theta$) na [[Regressão Logística]] (por exemplo, classificando como positivo qualquer indivíduo com probabilidade superior a apenas $0,15$);
- Ou utiliza-se uma matriz de perda ponderada em [[Árvores de Decisão]] atribuindo peso $10\times$ maior a erros de falso negativo.

Como consequência direta dessa postura agressiva de detecção, o modelo emitirá mais alarmes falsos ($FP \uparrow$), o que faz com que a [[Precisão]] sofra redução correspondente. A combinação balanceada de ambos os objetivos é formalizada pelo [[F1-Score]].

---

## 4. O Papel do Recall na Curva ROC

Na construção da [[Curva ROC]] e no cálculo da [[AUC]]:
- O **Eixo Y (Ordenadas)** é exatamente a Taxa de Verdadeiros Positivos ($\text{TPR} = \text{Recall}$);
- O **Eixo X (Abscissas)** é a Taxa de Falsos Positivos ($\text{FPR} = 1 - \text{Especificidade}$).

Uma curva que sobe rapidamente em direção ao canto superior esquerdo indica que o modelo é capaz de alcançar alto Recall sem permitir elevação descontrolada da taxa de alarmes falsos.

---

## 5. Implementação Prática em R

```r
library(caret)

# Observações reais e classificações preditas pelo modelo
reais    <- factor(c(1, 1, 1, 1, 1, 0, 0, 0, 0, 0))
preditos <- factor(c(1, 1, 1, 1, 0, 1, 0, 0, 0, 0))

# 1. Cálculo Manual
tp <- sum(reais == 1 & preditos == 1)
fn <- sum(reais == 1 & preditos == 0)
recall_manual <- tp / (tp + fn)
cat("Recall Manual:", recall_manual, "\n") # 4 / (4 + 1) = 0.80 (80%)

# 2. Extração via Matriz de Confusão do pacote caret
mc <- confusionMatrix(data = preditos, reference = reais, positive = "1")
recall_caret <- mc$byClass["Sensitivity"]
cat("Recall / Sensibilidade (caret):", round(recall_caret, 4), "\n")
```

Para uma visão integrada de todas as métricas de confusão, examine [[Métricas de Avaliação de Modelos]] e compare o comportamento de corte em [[Curva ROC]].
