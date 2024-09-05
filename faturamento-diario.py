import json

# Carregar os dados do arquivo JSON
with open('faturamento.json', 'r') as file:
    dados = json.load(file)

# Extrair a lista de faturamento do JSON
faturamento_diario = dados['faturamento']

# Filtrar dias com faturamento
dias_com_faturamento = [dia['valor'] for dia in faturamento_diario if dia['valor'] > 0]

# Cálculos
menor_valor = min(dias_com_faturamento)
maior_valor = max(dias_com_faturamento)
media_mensal = sum(dias_com_faturamento) / len(dias_com_faturamento)
dias_acima_media = sum(1 for valor in dias_com_faturamento if valor > media_mensal)

# Resultados
print(f"Menor valor de faturamento: R${menor_valor:.2f}")
print(f"Maior valor de faturamento: R${maior_valor:.2f}")
print(f"Média mensal de faturamento: R${media_mensal:.2f}")
print(f"Número de dias acima da média mensal: {dias_acima_media}")