#################################################
##### Universidade Federal do Rio Grande do Norte
##### Bacharelado em Sistemas de Informação
##### Velocidade Média do Ciclista (Refatorado)

print("Calculadora de Velocidade Média")
distancia = float(input("Qual a distância percorrida (em km)? "))
horas = int(input("Tempo gasto (Horas): "))
minutos = int(input("Tempo gasto (Minutos): "))

tempo_em_horas = horas + (minutos / 60)
vel_kmh = distancia / tempo_em_horas
vel_ms = vel_kmh / 3.6 # Conversão de km/h para m/s

print("Resultados")
print(f"Velocidade média (Km/h): {vel_kmh:.2f} km/h")
print(f"Velocidade média (m/s): {vel_ms:.2f} m/s")
