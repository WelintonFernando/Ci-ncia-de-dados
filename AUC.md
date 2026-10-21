---
aliases:
  - Area Under the Curve
  - AUROC
  - Área sob a Curva ROC
  - Estatística C
tags:
  - metricas
  - avaliacao
  - classificacao
  - machine-learning
---

# AUC (Área sob a Curva ROC)

A **AUC** (*Area Under the Curve* — Área sob a Curva), também identificada na literatura científica como **AUROC** (*Area Under the Receiver Operating Characteristic*) ou **Estatística $C$ de Concordância**, é o indicador escalar padrão-ouro no [[Aprendizado de Máquina]] para mensurar a capacidade discriminativa global de um classificador binário.

Enquanto a [[Curva ROC]] fornece uma representação gráfica bidimensional das taxas de acerto e alarmes falsos, a AUC resume essa curva em um único número compreendido no intervalo fechado entre $0$ e $1$.

---

## 1. Formulação Matemática

Do ponto de vista do cálculo infinitesimal, a AUC é a integral definida da função da taxa de verdadeiros positivos ($\text{TPR}$) integrada em relação à taxa de falsos positivos ($\text{FPR}$) de $0$ a $1$:

$$\text{AUC} = \int_{0}^{1} \text{TPR}(\text{FPR}) \, d(\text{FPR})$$

Para conjuntos discretos de observações finitas, a AUC é calculada numericamente por meio da **regra dos trapézios**, somando as áreas geométricas formadas sob os segmentos da [[Curva ROC]].

---

## 2. Interpretação Probabilística: A Estatística de Concordância

Além de sua interpretação geométrica como área sob a curva, a AUC possui um significado estatístico elegante:

$$\text{AUC} = P\left(\hat{p}_{\text{positivo}} > \hat{p}_{\text{negativo}}\right)$$

> [!IMPORTANT]
> A AUC representa a **probabilidade exata** de que o classificador atribua uma pontuação de propensão maior a um indivíduo positivo sorteado aleatoriamente do que a um indivíduo negativo sorteado aleatoriamente.

Por exemplo, um modelo com $\text{AUC} = 0,85$ garante que, se escolhermos ao acaso uma transação fraudulenta e uma transação legítima, em **$85\%$ das vezes** o algoritmo atribuirá uma probabilidade de fraude maior à transação criminosa do que à idônea.

---

## 3. Escala Qualitativa de Desempenho

| Faixa de Valor da AUC | Classificação Qualitativa | Comportamento das Classes |
| :---: | :---: | :--- |
| **$1,00$** | **Perfeito** | Separação absoluta; nenhuma sobreposição entre as distribuições das classes. |
| **$0,90 \le \text{AUC} < 1,00$** | **Excelente** | Altíssimo poder discriminativo; quase ausência de alarmes falsos. |
| **$0,80 \le \text{AUC} < 0,90$** | **Bom** | Performance sólida; atende à ampla maioria das aplicações corporativas. |
| **$0,70 \le \text{AUC} < 0,80$** | **Regular / Aceitável** | Capacidade razoável; recomendam-se refinamentos em [[Pré-Processamento e Engenharia de Atributos]]. |
| **$0,60 \le \text{AUC} < 0,70$** | **Pobre** | Pouco superior a uma escolha ingênua. |
| **$0,50$** | **Aleatório** | Equivalente a uma moeda honesta; o modelo não aprendeu nenhum sinal útil. |
| **$< 0,50$** | **Invertido** | Pior que o acaso; indica erro na convenção dos rótulos de classe no treinamento. |

---

## 4. Por que a AUC é Superior à Acurácia?

A métrica AUC apresenta duas vantagens teóricas decisivas em relação à [[Acurácia]]:

1. **Invariância de Limiar (*Threshold-Invariance*)**: A AUC mede a capacidade intrínseca do algoritmo de **ranquear corretamente as observações**, independentemente do limiar estático de decisão ($\theta$) escolhido pelo analista para a [[Matriz de Confusão]].
2. **Invariância de Prevalência (*Scale-Invariance*)**: O indicador não se degrada artificialmente quando o conjunto de dados possui classes severamente desbalanceadas, evitando o perigoso Paradoxo da Acurácia.

---

## 5. Implementação Prática em R com o Pacote ROCR

No estudo de caso de concessão de crédito em [[Regressão Logística]], o cálculo programático da AUC é realizado da seguinte forma:

```r
library(ROCR)

# Vetores de probabilidades preditas e classes observadas
probabilidades <- c(0.92, 0.85, 0.78, 0.65, 0.58, 0.42, 0.35, 0.22, 0.15, 0.08)
classes_reais  <- c(1,    1,    1,    0,    1,    0,    0,    1,    0,    0)

# 1. Criação do objeto de predição
pred_obj <- prediction(probabilidades, classes_reais)

# 2. Extração do valor escalar da AUC
auc_obj  <- performance(pred_obj, measure = "auc")
auc_score <- auc_obj@y.values[[1]]

cat("Pontuação AUC:", round(auc_score, 4), "\n")
```

Para inspecionar a curva correspondente traçada no plano cartesiano, consulte [[Curva ROC]] e compare o resultado com as demais métricas em [[Métricas de Avaliação de Modelos]].
