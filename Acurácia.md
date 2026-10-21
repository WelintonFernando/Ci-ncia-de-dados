---
aliases:
  - Accuracy
  - Acurácia Balanceada
  - Balanced Accuracy
tags:
  - metricas
  - avaliacao
  - classificacao
  - machine-learning
---

# Acurácia

A **Acurácia** (*Accuracy*) é a métrica mais intuitiva e amplamente difundida para a avaliação global de classificadores no [[Aprendizado de Máquina]]. Ela quantifica a proporção exata entre o número de predições corretas realizadas pelo modelo e o volume total absoluto de instâncias avaliadas.

Embora seja o primeiro indicador frequentemente consultado em relatórios analíticos, seu uso exige cautela metodológica extrema, pois pode induzir a conclusões perigosamente equivocadas em cenários com desbalanceamento de classes, conforme detalhado em [[Métricas de Avaliação de Modelos]].

---

## 1. Formulação Matemática

A partir dos quatro quadrantes elementares da [[Matriz de Confusão]]:
- **$TP$ (*True Positive*)**: Verdadeiros Positivos;
- **$TN$ (*True Negative*)**: Verdadeiros Negativos;
- **$FP$ (*False Positive*)**: Falsos Positivos (Erro Tipo I);
- **$FN$ (*False Negative*)**: Falsos Negativos (Erro Tipo II).

A **Acurácia ($Acc$)** é formulada matematicamente por:

$$\text{Acurácia} = \frac{TP + TN}{TP + TN + FP + FN}$$

Onde:
- O numerador representa a soma de todos os acertos empíricos;
- O denominador representa o espaço amostral total ($N = TP + TN + FP + FN$);
- O resultado é um valor normalizado no intervalo fechado: $0 \le \text{Acurácia} \le 1$ (ou de $0\%$ a $100\%$).

---

## 2. O Paradoxo da Acurácia (*Accuracy Paradox*)

O grande ponto cego da acurácia ocorre quando a distribuição das classes no conjunto de dados é severamente desequilibrada (*imbalanced data*).

### Estudo de Caso Hipotético: Detecção de Fraude Bancária
Considere uma base de dados com $10.000$ transações com cartão de crédito:
- $9.900$ transações são legítimas ($99\%$);
- $100$ transações são fraudulentas ($1\%$).

Se construirmos um modelo "burro" que simplesmente responda **sempre** que a transação é legítima (classe negativa), teremos:
- $TP = 0$ (não detectou nenhuma fraude);
- $FN = 100$ (deixou passar todas as fraudes);
- $FP = 0$;
- $TN = 9.900$.

Calculando a acurácia:

$$\text{Acurácia} = \frac{0 + 9900}{0 + 9900 + 0 + 100} = \frac{9900}{10000} = 99,0\%$$

> [!CAUTION]
> O modelo possui **99% de acurácia**, mas tem **zero utilidade prática**, pois falhou em capturar 100% dos eventos que o negócio necessitava identificar! Para mitigal esse problema, deve-se recorrer a métricas focadas como [[Recall]], [[Precisão]] e [[F1-Score]].

---

## 3. Acurácia Balanceada (*Balanced Accuracy*)

Para contornar o paradoxo em bases desbalanceadas, utiliza-se a **Acurácia Balanceada ($Acc_B$)**, calculada como a média aritmética simples entre a taxa de acerto da classe positiva ([[Recall|Sensibilidade]]) e a taxa de acerto da classe negativa ([[Especificidade]]):

$$\text{Acurácia Balanceada} = \frac{\text{Sensibilidade} + \text{Especificidade}}{2} = \frac{\frac{TP}{TP + FN} + \frac{TN}{TN + FP}}{2}$$

No exemplo da fraude bancária acima:
- $\text{Sensibilidade} = \frac{0}{100} = 0,0$
- $\text{Especificidade} = \frac{9900}{9900} = 1,0$
- $\text{Acurácia Balanceada} = \frac{0,0 + 1,0}{2} = 0,50$ ($50\%$)

O resultado de $50\%$ revela imediatamente que a capacidade preditiva do modelo é idêntica ao acaso (jogar uma moeda honesta para o alto).

---

## 4. Quando Utilizar a Acurácia?

| Cenário Analítico | Recomendação | Justificativa Técnica |
| :--- | :---: | :--- |
| **Classes Balanceadas (ex: 50% / 50%)** | **Altamente Recomendada** | Reflete com fidelidade a performance do modelo sem viés de dominância amostral. |
| **Custos de Erro Simétricos** | **Recomendada** | Quando cometer um Falso Positivo ($FP$) acarreta o mesmo prejuízo que um Falso Negativo ($FN$). |
| **Classes Desbalanceadas (ex: 95% / 5%)** | **NÃO Recomendada** | Sujeita ao Paradoxo da Acurácia; mascara a ineficácia do classificador na classe minoritária. |
| **Custos de Erro Assimétricos (Medicina/Fraude)** | **NÃO Recomendada** | Deixar de detectar um caso grave ($FN$) custa infinitamente mais que um falso alarme ($FP$). |

---

## 5. Implementação Prática em R

No ecossistema [[Introdução ao R|R]], a acurácia é calculada diretamente a partir das predições de modelos como [[Regressão Logística]] ou [[Árvores de Decisão]]:

```r
library(caret)

# Vetores de teste
classes_reais    <- factor(c(1, 1, 0, 1, 0, 0, 1, 0, 1, 1))
classes_preditas <- factor(c(1, 1, 0, 0, 0, 0, 1, 1, 1, 1))

# Cálculo manual
total_acertos <- sum(classes_reais == classes_preditas)
acuracia_manual <- total_acertos / length(classes_reais)
cat("Acurácia Manual:", acuracia_manual, "\n") # 0.8 (80%)

# Cálculo completo via pacote caret
mc <- confusionMatrix(data = classes_preditas, reference = classes_reais, positive = "1")

# Extração de métricas
cat("Acurácia Global:", mc$overall["Accuracy"], "\n")
cat("Acurácia Balanceada:", mc$byClass["Balanced Accuracy"], "\n")
```

Para uma análise comparativa profunda diante de outros indicadores, consulte [[Métricas de Avaliação de Modelos]] e acompanhe as curvas de trade-off em [[Curva ROC]].
