# Problema BeeCrowd #2842

## Definição do Problema

O problema principal é encontrar o tamanho da menor subsequência comum entre duas strings, x e y.

### Formulação Recursiva

A relação de recorrência fundamental é expressa na construção da matriz DP. A entrada dp[i][j] é atualizada com base nas entradas anteriores da matriz, refletindo escolhas ótimas em cada estágio.

### Preenchimento da Matriz DP

- O preenchimento da matriz é realizado de forma iterativa, começando com casos base para i = 0 e j = 0.
- Se i é zero, selecionamos o tamanho j
- Se j é zero, selecionamos o tamanho i 
- Se x[i - 1] é igual a y[j - 1], o valor é atualizado para dp[i - 1][j - 1] + 1, refletindo a correspondência de caracteres nas strings.
- Se os caracteres não são iguais, o valor é atualizado para 1 mais o mínimo entre o valor acima (dp[i - 1][j]) e o valor à esquerda (dp[i][j - 1]), representando a escolha do caminho mais curto na matriz DP.


### Utilização do Resultado Ótimo

O resultado final é armazenado em dp[size1][size2], onde size1 e size2 são os comprimentos das strings x e y, respectivamente. Isso representa o tamanho da menor subsequência comum.
Aspectos Dinâmicos Específicos:

### Evitar Recálculos

A matriz DP evita recálculos desnecessários, armazenando os resultados intermediários e construindo a solução ótima de maneira incremental.

### Decomposição em Subproblemas Menores

O problema principal é decomposto em subproblemas menores que são resolvidos de maneira independente e cujas soluções são utilizadas para construir a solução do problema original.

### Escolha Ótima Local

A cada passo, o algoritmo faz escolhas locais ótimas para construir uma solução globalmente ótima.

### Por que é Dinâmico
A abordagem é dinâmica porque a solução do problema é construída dinamicamente usando informações de soluções menores. A matriz DP atua como uma tabela de memoização, 
armazenando resultados intermediários para evitar a recalculação de subproblemas. A estratégia dinâmica permite resolver instâncias menores do problema e usar essas soluções para construir uma solução globalmente ótima.

## Argumentos de Linha de Comando
A opção `--debug` ou `-d` permite a exibição da matriz DP para fins de depuração.
