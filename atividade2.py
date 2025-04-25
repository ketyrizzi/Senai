

   #Alguns países medem temperaturas em graus Celsius, e outros em graus Fahrenheit. Faça um algoritmo para ler uma temperatura Celsius e imprimi-Ia em Fahrenheit 
   # (pesquise como fazer este tipo de conversão).

celsius = float(input("Digite a temperatura em graus Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"\n{celsius:.2f}°C equivalem a {fahrenheit:.2f}°F")
