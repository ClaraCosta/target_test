# Desafio TARGET - Python

<h3>Repositório destinado a resolução do desafio TARGET, que envolve a solução de uma série de problemas de lógica e programação, utilizando a linguagem Python. Cada problema foi abordado de forma individual, com exemplos de código e explicações detalhadas.</h3>

---

<p>1) Observe o trecho de código abaixo: int INDICE = 13, SOMA = 0, K = 0;
Enquanto K < INDICE faça { K = K + 1; SOMA = SOMA + K; }
Imprimir(SOMA); 

Ao final do processamento, qual será o valor da variável SOMA?

<b>R:</b> `1 - soma_processamento`
</p>

---

<p> 2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.</p>

IMPORTANTE: Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;

<b>R:</b> `2 - verifica_sequencia_fibonacci`

---

<p>3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:</p>

- O menor valor de faturamento ocorrido em um dia do mês;
- O maior valor de faturamento ocorrido em um dia do mês;
- Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

IMPORTANTE:
- Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
- Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;

<b>R:</b> `3 - calcula_dados_faturamento`

---
<p>4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:</p>

- SP – R$67.836,43
- RJ – R$36.678,66
- MG – R$29.229,88
- ES – R$27.165,48
- Outros – R$19.849,53

<p>Escreva um programa na linguagem que desejar onde calcule o percentual de representação que cada estado teve dentro do valor total mensal da distribuidora.</p> 

<b>R:</b> `4 - calcula_percentual_mensal` 

---
<p>5) Escreva um programa que inverta os caracteres de um string.</p>

IMPORTANTE:
- Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
- Evite usar funções prontas, como, por exemplo, reverse;

<b>R:</b> `inverte_tring_sem_func_pronta` 
