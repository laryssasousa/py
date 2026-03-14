####Saída de dados em Python

print("Bem vindo ao curso de Algoritmos!")
nome = (input("Insira o seu nome:" ))
endereço = (input("Insira o seu endereço: "))
idade = int(input("Insira quantos anos você tem:" ))
nota1 = float(input("Insira sua nota da primeira unidade:" ))
nota2 = float(input("Insira sua nota da segunda unidade:" ))
nota3 = float(input("Insira sua nota da terceira unidade:" ))
media = (nota1 + nota2 + nota3)/3
print("Seu nome é:" , nome, "Você mora em:" , endereço, "Você tem:" , idade, "anos", "Sua média é:" , media)
