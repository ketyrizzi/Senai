#A empresa Hipotheticus paga R$10,00 por hora normal trabalhada, e R$15,00 por hora extra. Faça um algoritmo para calcular e imprimir o salário bruto e o salário líquido 
# de um determinado funcionário. Considere que o salário líquido é igual ao salário bruto descontando-se 10% de impostos.


horas_normais = float(input("Digite as horas normais trabalhadas: "))
horas_extras = float(input("Digite as horas extras trabalhadas: "))
salario_bruto = (horas_normais * 10.00) + (horas_extras * 15.00)
impostos = salario_bruto * 0.10
salario_liquido = salario_bruto - impostos
print(f"\nSalário Bruto: R$ {salario_bruto:.2f}")
print(f"Descontos (10%): R$ {impostos:.2f}")
print(f"Salário Líquido: R$ {salario_liquido:.2f}")
