###Corrida

def calcular_pace(tempo_minutos, distancia_km):
    """
    Calcula o pace (min/km) dado o tempo total em minutos e a distância em km.
    """
    pace_decimal = tempo_minutos / distancia_km
    minutos = int(pace_decimal)
    segundos = round((pace_decimal - minutos) * 60)

    return minutos, segundos, pace_decimal

print("CALCULADORA DE PACE")

# Solicitando os dados para o usuário interagir
try:
    distancia_percorrida = float(input("Digite a distância percorrida (em Km): "))
    tempo_total = float(input("Digite o tempo total do treino (em minutos): "))

    # Fazendo o cálculo
    minutos, segundos, pace_decimal = calcular_pace(tempo_total, distancia_percorrida)

    # Exibindo os resultados
    print("-" * 30)
    print(f"Distância: {distancia_percorrida} Km")
    print(f"Tempo total: {tempo_total} minutos")
    print(f"Pace decimal: {pace_decimal:.2f} min/km")
    print(f"Pace formatado: {minutos}'{segundos:02d}\"/km")

except ValueError:
    print("Erro: Por favor, digite apenas números válidos (use ponto no lugar da vírgula para decimais).")
