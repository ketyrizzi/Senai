#Pedrinho tem um cofrinho com muitas moedas, e deseja saber quantos reais conseguiu poupar. 
# Faça um algoritmo para ler a quantidade de cada tipo de moeda, e imprimir o valor total economizado, em reais. 
# Considere que existam moedas de 1, 5, 10, 25 e 50 centavos, e ainda moedas de 1 real. Não havendo moeda de um tipo, a quantidade respectiva é zero.


moeda_1_centavos = int(input("quantidade de moedas de 1 centavo: "))
moeda_5_centavos = int(input("quantidade de moedas de 5 centavos: "))
moeda_10_centavos = int(input("quantidade de moedas de 10 centavos: "))
moeda_50_centavos = int(input("quantidade de moedas de 50 centavos:  "))
moeda_1_real = int(input("quantidade de moedas de 1 real: "))


total = moeda_1_centavo * 0.01 +
moeda_5_centavos * 0.05 +
moeda_10_centavos * 0.010 +
moeda_50_centavos * 0.050 +
moeda_1_real * 1.00 +

print(f"\nValor total economizando: R$ {total: .2f}")