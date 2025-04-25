#   Calcule o volume de uma caixa d'água cilíndrica.
import math
raio = float(input("digite o raio da base da caixa d'água (em metros): "))
altura = float(input("digite a altura da base da caixa d'água (em metros): "))


volume_m3 = math.pi * (raio ** 2) * altura

volume_litros = volume_m3 * 1000

print(f"\nO volume da caixa d'água é:")
print(f"{volume_m3:.2f} m³ (metros cúbicos)")
print(f"{volume_litros:.2f} litros")

