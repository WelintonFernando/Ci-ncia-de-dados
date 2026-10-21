---
aliases:
  - Specificity
  - Taxa de Verdadeiros Negativos
  - TNR
  - True Negative Rate
tags:
  - metricas
  - avaliacao
  - classificacao
  - machine-learning
---

# Especificidade

A **Especificidade** (*Specificity*) — também identificada como **Taxa de Verdadeiros Negativos** ($TNR$ — *True Negative Rate*) — é a métrica de desempenho que quantifica a capacidade de um classificador no [[Aprendizado de Máquina]] de **identificar corretamente os casos negativos genuínos** presentes no conjunto de observações.

Enquanto o [[Recall|Recall (Sensibilidade)]] foca na cobertura dos casos positivos de interesse (*"Quantos positivos conseguimos capturar?"*), a Especificidade concentra-se na proteção contra alarmes falsos (*"Quantos indivíduos sabidamente normais foram corretamente liberados sem suspeitas infundadas?"*).

A Especificidade é um componente essencial na formulação da [[Acurácia|Acurácia Balanceada]] e define o eixo horizontal da [[Curva ROC]] em [[Métricas de Avaliação de Modelos]].

---

## 1. Formulação Matemática

A partir dos quadrantes da [[Matriz de Confusão]]:
- **$TN$ (*True Negative*)**: Verdadeiros Negativos (indivíduos negativos classificados corretamente como negativos);
- **$FP$ (*False Positive*)**: Falsos Positivos (indivíduos negativos classificados incorretamente como positivos — Erro Tipo I).

A **Especificidade** é expressa pela razão:

$$\text{Especificidade} = \frac{TN}{TN + FP}$$

Onde:
- O numerador $TN$ representa os acertos na classe negativa;
- O denominador $(TN + FP)$ representa o **total de observações verdadeiramente negativas** existentes no mundo real;
- O indicador varia no intervalo fechado de $0$ a $1$ (ou de $0\%$ a $100\%$).

---

## 2. A Taxa de Falsos Positivos ($FPR$)

O complemento direto da especificidade em relação à unidade é a **Taxa de Falsos Positivos** ($FPR$ — *False Positive Rate* ou *Fall-out*):

$$\text{FPR} = 1 - \text{Especificidade} = \frac{FP}{TN + FP}$$

Essa grandeza mede a probabilidade de um indivíduo sadio ou de uma transação perfeitamente legítima ser erroneamente rotulada como positiva (alarme falso). Na construção da [[Curva ROC]], o **Eixo X** corresponde rigorosamente a essa taxa ($1 - \text{Especificidade}$).

---

## 3. Aplicações Práticas e Relevância de Negócio

A Especificidade assume papel de destaque em decisões operacionais onde os custos de um exame de confirmação invasivo ou o constrangimento de clientes são elevados:

1. **Testes Médicos Confirmatórios de Doenças Estigmatizantes**:
   - Rotular um paciente saudável como portador de uma patologia grave gera estresse psicológico severo, custos adicionais com biópsias invasivas e tratamentos com fortes efeitos colaterais. Uma alta especificidade assegura que apenas suspeitas reais avancem.
2. **Sistemas de Prevenção a Fraudes e Bloqueio Cautelar**:
   - Um modelo com baixa especificidade gera volume insustentável de alarmes falsos ($FP$), sobrecarregando a mesa humana de analistas e provocando o bloqueio indevido de cartões de clientes idôneos.

---

## 4. Relação com a Acurácia Balanceada

Em conjuntos de dados com classes severamente desbalanceadas, a [[Acurácia]] simples gera distorções metodológicas graves. A **Acurácia Balanceada** corrige essa falha combinando a Sensibilidade ([[Recall]]) e a Especificidade em partes iguais:

$$\text{Acurácia Balanceada} = \frac{\text{Sensibilidade} + \text{Especificidade}}{2}$$

---

## 5. Implementação Prática em R

```r
library(caret)

# Observações reais e classificações preditas pelo modelo
reais    <- factor(c(0, 0, 0, 0, 0, 1, 1, 1, 0, 1))
preditos <- factor(c(0, 0, 0, 1, 0, 1, 1, 0, 0, 1))

# 1. Cálculo Manual
tn <- sum(reais == 0 & preditos == 0)
fp <- sum(reais == 0 & preditos == 1)
especificidade_manual <- tn / (tn + fp)
cat("Especificidade Manual:", round(especificidade_manual, 4), "\n") # 5 / (5 + 1) = 0.8333

# 2. Extração via pacote caret
mc <- confusionMatrix(data = preditos, reference = reais, positive = "1")
cat("Especificidade (caret):", round(mc$byClass["Specificity"], 4), "\n")
```

Para analisar como a especificidade varia simultaneamente com o recall ao modificar o limiar de decisão de probabilidades, consulte [[Curva ROC]] e [[Métricas de Avaliação de Modelos]].
