def inverter_string(texto):
    invertida = ''
    for i in range(len(texto) - 1, -1, -1):
        invertida += texto[i]
    return invertida

# Entrada do usuário
texto_original = input("Digite uma string para inverter: ")

# Inverter a string
texto_invertido = inverter_string(texto_original)

# Imprimir resultado
print(f"String original: {texto_original}")
print(f"String invertida: {texto_invertido}")