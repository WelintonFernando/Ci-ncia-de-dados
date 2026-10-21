---
aliases:
  - Precision
  - Valor Preditivo Positivo
  - PPV
tags:
  - metricas
  - avaliacao
  - classificacao
  - machine-learning
---

# Precisão

A **Precisão** (*Precision*) — também denominada na literatura biomédica e estatística como **Valor Preditivo Positivo** ($PPV$ — *Positive Predictive Value*) — é uma métrica de desempenho de classificadores no [[Aprendizado de Máquina]] que avalia a confiabilidade e exatidão das previsões afirmativas do modelo.

Ela responde diretamente à pergunta crítica de negócio: *"De todas as vezes em que o modelo classificou uma instância como pertencente à classe positiva, quantas eram verdadeiramente positivas no mundo real?"*

Ao contrário da [[Acurácia]], que calcula uma média sobre todo o espaço amostral, a Precisão restringe sua análise estritamente ao universo dos casos rotulados como positivos pelo algoritmo, conforme estruturado em [[Métricas de Avaliação de Modelos]].

---

## 1. Formulação Matemática

A partir dos quadrantes da [[Matriz de Confusão]]:
- **$TP$ (*True Positive*)**: Verdadeiros Positivos (acertos na classe positiva);
- **$FP$ (*False Positive*)**: Falsos Positivos (erros do Tipo I — alarmes falsos).

A **Precisão** é expressa formalmente por:

$$\text{Precisão} = \frac{TP}{TP + FP}$$

Onde:
- O numerador representa os acertos positivos confirmados;
- O denominador $(TP + FP)$ representa o **total de predições positivas** emitidas pelo modelo;
- O indicador varia de $0$ a $1$ (ou de $0\%$ a $100\%$).

---

## 2. Cenários de Negócio Onde a Precisão é Prioridade

A maximização da Precisão torna-se o objetivo primordial sempre que o custo operacional, financeiro ou de reputação decorrente de um **Falso Positivo ($FP$)** for substancialmente superior ao custo de um Falso Negativo ($FN$).

### Casos de Uso Críticos:
1. **Filtros de Spam em E-mails**:
   - Um falso negativo ($FN$) significa receber um e-mail indesejado na caixa de entrada (inconveniente tolerável).
   - Um falso positivo ($FP$) significa classificar um contrato assinado ou oferta de emprego como spam (prejuízo inaceitável).
2. **Sistemas de Recomendação de Alto Custo / Marketing Direto**:
   - Se o envio de um brinde ou visita presencial de um consultor sênior custa $\text{R\$} 5.000$, a empresa só deve abordar clientes com altíssima probabilidade de fechamento, minimizando os alarmes falsos.
3. **Bloqueio Cautelar de Contas Bancárias**:
   - Bloquear indevidamente a conta de um cliente idôneo de alta renda causa atrito severo, processos judiciais e perda imediata do cliente para concorrentes.

---

## 3. O Trade-off entre Precisão e Recall

Existe uma tensão matemática inversa e incontornável entre Precisão e [[Recall]]:

```
                 AUMENTO DO LIMIAR DE DECISÃO (Ex: Cutoff de 0.50 para 0.85)
                                      |
                     O Modelo torna-se conservador:
                 Só dispara positivo quando tem certeza!
                               /          \
                              v            v
                    Falsos Positivos (FP)     Falsos Negativos (FN)
                       caem drasticamente        aumentam rapidamente
                              |                           |
                              v                           v
                       PRECISÃO SOBE                RECALL DESPENCA
```

- Para obter **alta precisão**, elevamos o limiar de corte ($\theta$) na [[Regressão Logística]]. O modelo reduz os alarmes falsos ($FP \to 0$), mas perde casos positivos sutis.
- Para equilibrar essa compensação sem sacrificar excessivamente nenhuma das duas métricas, calcula-se o [[F1-Score]], que é a média harmônica entre ambas.

---

## 4. Implementação em R

No ecossistema [[Introdução ao R|R]], calculamos a precisão manualmente ou via biblioteca `caret`:

```r
library(caret)

# Vetores de teste
classes_reais    <- factor(c(1, 0, 1, 1, 0, 1, 0, 0, 1, 0))
classes_preditas <- factor(c(1, 0, 1, 0, 0, 1, 1, 0, 1, 0))

# 1. Cálculo Manual
tp <- sum(classes_reais == 1 & classes_preditas == 1)
fp <- sum(classes_reais == 0 & classes_preditas == 1)
precisao_manual <- tp / (tp + fp)
cat("Precisão Manual:", precisao_manual, "\n") # 4 / (4 + 1) = 0.80 (80%)

# 2. Extração via Matriz de Confusão do caret
mc <- confusionMatrix(data = classes_preditas, reference = classes_reais, positive = "1")
precisao_caret <- mc$byClass["Pos Pred Value"]
cat("Precisão (Pos Pred Value):", round(precisao_caret, 4), "\n")
```

Para visualizar a evolução conjunta da precisão sob diferentes pontos de corte, consulte [[Métricas de Avaliação de Modelos]] e inspecione as taxas de alarme falso em [[Curva ROC]].
