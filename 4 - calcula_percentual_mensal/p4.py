#------------------------------------------------------------------------------------------------------------------------------------
#--------------Percentual de representação que cada estado teve dentro do valor total mensal da distribuidora------------------------
#------------------------------------------------------------------------------------------------------------------------------------

# Dados de faturamento por estado
faturamento_estados = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "PB": 21485.25,  #  ;)
    "Outros": 19849.53
}

# Soma dos valores e armazenamento em uma variável
total = sum(faturamento_estados.values())

# Calculando o percentual e printando o resultado
for estado, valor in faturamento_estados.items():
    percentual = (valor / total) * 100
    print(f"{estado}: {percentual:.2f}%")