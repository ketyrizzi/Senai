   #A granja Frangotech possui um controle automatizado de cada frango da sua produção. 
   # No pé direito do frango há um anel com um chip de identificação; no pé esquerdo são dois anéis para indicar o tipo de alimento que ele deve consumir. 
   # Sabendo que o anel com chip custa R$4,00 e o anel de alimento custa R$3,50, faça um algoritmo para calcular o gasto total da granja para marcar todos os seus frangos.


quantidade_frangos = int(input("Número total de frangos: "))
custo_por_frango = 4 + (2 * 3.5)
custo_total = custo_por_frango * quantidade_frangos
print(f"Custo total para marcar {quantidade_frangos} frangos: R$ {custo_total:.2f}")
