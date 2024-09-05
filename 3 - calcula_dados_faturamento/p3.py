import json 

#------------------------------------------------------------------------------------------------------------------------------------
#---------------------------O menor valor de faturamento ocorrido em um dia do mês;--------------------------------------------------
#---------------------------O maior valor de faturamento ocorrido em um dia do mês;--------------------------------------------------
#---------------------------Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.------------------
#------------------------------------------------------------------------------------------------------------------------------------


# Chamando o arquivo dados.json, para que possa ser lido pelo programa
with open('3 - calcula_dados_faturamento/dados.json', 'r') as file:
    dados = json.load(file)

# Verificando os valores maiores que zero (0)
faturamentos = [d['valor'] for d in dados if d['valor'] > 0]

# Calculando a média mensal de faturamento
menor_faturamento = min(faturamentos)
maior_faturamento = max(faturamentos)
media_mensal = sum(faturamentos) / len(faturamentos)
dias_acima_da_media = sum(1 for f in faturamentos if f > media_mensal)

# Imprimindo os cálculos
print(f"Menor faturamento: {menor_faturamento}")
print(f"Maior faturamento: {maior_faturamento}")
print(f"Dias com faturamento acima da média: {dias_acima_da_media}")