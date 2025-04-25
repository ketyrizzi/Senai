#Um tonel de refresco é feito com 8 partes de água mineral e 2 partes de suco de maracujá. 
# Faça um algoritmo para calcular quantos litros de água e de suco são necessários para se fazer X litros de refresco (informados pelo usuário).

total_refresco = float(input("Digite a quantidade total de refresco desejada (em litros): "))


litros_agua = (8 / 10) * total_refresco
litros_suco = (2 / 10) * total_refresco


print(f"\nPara fazer {total_refresco:.2f} litros de refresco, você vai precisar de:")
print(f"{litros_agua:.2f} litros de água mineral")
print(f"{litros_suco:.2f} litros de suco de maracujá")
