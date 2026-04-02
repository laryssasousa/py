### SUPER PROGRAMA DE UTILIDADES

#### Mensagem de boas-vindas para o usuário
print("  BEM-VINDO AO SUPER PROGRAMA DE UTILIDADES ")
print("Escolha uma das opções abaixo digitando o número correspondente:")

#### Menu de opções
print("1 - Somar dois números")
print("2 - Subtrair dois números")
print("3 - Multiplicar dois números")
print("4 - Dividir dois números")
print("5 - Descobrir se um número é Par ou Ímpar")
print("6 - Calcular a área de um Quadrado")
print("7 - Calcular a área de um Retângulo")
print("8 - Calcular a área de um Triângulo")
print("9 - Converter temperatura de Celsius para Fahrenheit")
print("10 - Converter temperatura de Fahrenheit para Celsius")
print("11 - Converter metros para centímetros")
print("12 - Classificar sua idade (Criança, Adolescente, Adulto, Idoso)")
print("13 - Ver uma mensagem motivacional")
print("14 - Calcular Teorema de Pitágoras")
print("0 - Sair do programa")

#### Solicitação para o usuário digitar a opção escolhida. 
opcao = int(input("Digite o número da sua escolha: "))

if opcao == 1:
    ### Opção de Soma
    print("\nVocê escolheu: Somar dois números.")
    # Usamos 'float()' porque a pessoa pode querer somar números com vírgula (ex: 2.5)
    numero1 = float(input("Digite o primeiro número: "))
    numero2 = float(input("Digite o segundo número: "))
    resultado = numero1 + numero2
    print("O resultado da soma é:", resultado)

elif opcao == 2:
    ### Opção de Subtração
    print("\nVocê escolheu: Subtrair dois números.")
    numero1 = float(input("Digite o primeiro número: "))
    numero2 = float(input("Digite o segundo número: "))
    resultado = numero1 - numero2
    print("O resultado da subtração é:", resultado)

elif opcao == 3:
    ### Opção de Multiplicação
    print("\nVocê escolheu: Multiplicar dois números.")
    numero1 = float(input("Digite o primeiro número: "))
    numero2 = float(input("Digite o segundo número: "))
    resultado = numero1 * numero2
    print("O resultado da multiplicação é:", resultado)

elif opcao == 4:
    ### Opção de Divisão
    print("\nVocê escolheu: Dividir dois números.")
    numero1 = float(input("Digite o primeiro número: "))
    numero2 = float(input("Digite o segundo número: "))
    
    ### Há 'if' extra aqui porque não se pode dividir por zero!
    if numero2 == 0:
        print("Erro! Não é possível dividir um número por zero.")
    else:
        resultado = numero1 / numero2
        print("O resultado da divisão é:", resultado)

elif opcao == 5:
    ### Opção de Par ou Ímpar
    print("\nVocê escolheu: Descobrir se é Par ou Ímpar.")
    # Foi usado 'int()' porque a regra de par ou ímpar se aplica a números inteiros
    numero = int(input("Digite um número inteiro: "))
    
    ### O operador '%' pega o resto da divisão. Se dividir por 2 e sobrar 0, é par!
    if numero % 2 == 0:
        print("O número", numero, "é PAR!")
    else:
        print("O número", numero, "é ÍMPAR!")

elif opcao == 6:
    ### Opção Área do Quadrado
    print("\nVocê escolheu: Calcular a área de um Quadrado.")
    lado = float(input("Digite o tamanho do lado do quadrado: "))
    area = lado * lado
    print("A área do quadrado é:", area)

elif opcao == 7:
    ### Opção Área do Retângulo
    print("\nVocê escolheu: Calcular a área de um Retângulo.")
    base = float(input("Digite o tamanho da base do retângulo: "))
    altura = float(input("Digite o tamanho da altura do retângulo: "))
    area = base * altura
    print("A área do retângulo é:", area)

elif opcao == 8:
    ### Opção Área do Triângulo
    print("\nVocê escolheu: Calcular a área de um Triângulo.")
    base = float(input("Digite o tamanho da base do triângulo: "))
    altura = float(input("Digite o tamanho da altura do triângulo: "))
    ### A fórmula da área do triângulo é (base * altura) dividido por 2
    area = (base * altura) / 2
    print("A área do triângulo é:", area)

elif opcao == 9:
    ### Opção Celsius para Fahrenheit
    print("\nVocê escolheu: Converter Celsius para Fahrenheit.")
    celsius = float(input("Digite a temperatura em graus Celsius: "))
    # Fórmula de conversão
    fahrenheit = (celsius * 9/5) + 32
    print("A temperatura em Fahrenheit é:", fahrenheit)

elif opcao == 10:
    ### Opção Fahrenheit para Celsius
    print("\nVocê escolheu: Converter Fahrenheit para Celsius.")
    fahrenheit = float(input("Digite a temperatura em graus Fahrenheit: "))
    ### Fórmula de conversão inversa
    celsius = (fahrenheit - 32) * 5/9
    print("A temperatura em Celsius é:", celsius)

elif opcao == 11:
    ### Opção Metros para Centímetros
    print("\nVocê escolheu: Converter metros para centímetros.")
    metros = float(input("Digite a quantidade de metros: "))
    ### 1 metro tem 100 centímetros
    centimetros = metros * 100
    print(metros, "metros equivalem a", centimetros, "centímetros.")

elif opcao == 12:
    ### Opção de Classificação de Idade
    print("\nVocê escolheu: Classificar sua idade.")
    idade = int(input("Digite a sua idade: "))
    
    ### Aqui usamos múltiplos 'if', 'elif' e 'else' para checar a faixa etária
    if idade < 0:
        print("Idade inválida! Você ainda não nasceu?")
    elif idade <= 12:
        print("Você é uma Criança.")
    elif idade >= 13 and idade <= 17:
        print("Você é um Adolescente.")
    elif idade >= 18 and idade <= 59:
        print("Você é um Adulto.")
    else:
        print("Você é um Idoso(a).")

elif opcao == 13:
    ### Opção de Mensagem Motivacional
    print("\nVocê escolheu: Ver uma mensagem motivacional.")
    print("Lembre-se: Todo grande programador começou escrevendo códigos simples!")
    print("Continue praticando, você está no caminho certo. Parabéns por estudar Python!")

elif opcao == 14:
    ### Opção de Calcular Teorema de Pitágoras
    print("\nVocê escolheu: Calcular Teorema de Pitágoras.")
    import math

    ### Valores dos catetos
    cateto1 = int(input("Digite o valor do cateto 1: "))
    cateto2 = int(input("Digite o valor do cateto 2: "))
    hipotenusa = math.sqrt(cateto1**2 + cateto2**2)
    print(f"Hipotenusa (sqrt): {hipotenusa}")

elif opcao == 0:
    ### Opção de Sair
    print("\nVocê escolheu sair. Muito obrigado por usar o Super Programa!")
    print("Até a próxima!")

else:
    ### O 'else' final pega qualquer número que não esteja nas opções acima
    ### Se o usuário digitar 99, aparece esta mensagem
    print("\nOpção Inválida! Por favor, da próxima vez escolha um número entre 0 e 13.")

### Fim do programa
print("Fim do superprograma, espero que tenha te ajudado! :)")
