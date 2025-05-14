# Entrada da quantidade de sanduíches
quantidade = int(input("Digite a quantidade de sanduíches a fazer: "))


queijo_gramas = quantidade * 2 * 50     
presunto_gramas = quantidade * 1 * 50    
hamburguer_gramas = quantidade * 1 * 100
queijo_quilos = queijo_gramas / 1000
presunto_quilos = presunto_gramas / 1000
hamburguer_quilos = hamburguer_gramas / 1000


print(f"\nQuantidade necessária para {quantidade} sanduíches:")
print(f"Queijo: {queijo_quilos:.2f} kg")
print(f"Presunto: {presunto_quilos:.2f} kg")
print(f"Hambúrguer: {hamburguer_quilos:.2f} kg")
