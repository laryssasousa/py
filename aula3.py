###Calculando a média das UND1, UND2 e UND3

print("Cálculo da média")

def obter_nota(ordem):
    while True:
        try:
            nota_str = input(f"Digite a {ordem} nota: ")
            nota = float(nota_str)
            return nota
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")

nota1 = obter_nota("1a")
nota2 = obter_nota("2a")
nota3 = obter_nota("3a")

soma = nota1 + nota2 + nota3
media = soma / 3
print("Sua média foi: ", media)
