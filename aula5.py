###CONVERSOR DE TEMPERATURA PARA AMIGA QUE MORA NOS EUA

def converter_celsius_para_fahrenheit(celsius):
    """
    Converte a temperatura de graus Celsius para Fahrenheit.
    """
    fahrenheit = (celsius * 1.8) + 32
    return fahrenheit

print("Bem-vinda! / Welcome!")

try:
    temp_celsius = float(input("\nDigite a temperatura atual em ºC: "))
    temp_fahrenheit = converter_celsius_para_fahrenheit(temp_celsius)

    print("-" * 40)
    print(f"Temperatura no Brasil: {temp_celsius:.1f} ºC")
    print(f"Temperatura para você (EUA): {temp_fahrenheit:.1f} ºF")

    if temp_celsius >= 35:
        print("Aviso: Beba muita água e fique na sombra! (Drink lots of water!)")

except ValueError:
    print("\nErro: Por favor, digite apenas números. Use ponto no lugar da vírgula (ex: 32.5).")
