#Exercício 1
anoNascimento = int(input("Qual ano você nasceu? "))
idade = int(2025) - anoNascimento
print("Você tem "+ str(idade) +" anos")

#Exercício 2
quantidadeCarros = int(input("Quantos carros você quer alugar? "))
preco = quantidadeCarros*100
print("Cada aluguel de carro custa 100 reais, logo você terá que pagar "+ str(preco) + " reais" )

#Exercício 3
tempCelsius = int(input("Qual a temperatura em celsius? "))
fahrenheit = (tempCelsius*9/5)+ 32
print(str(tempCelsius) + " corresponde a "+ str(fahrenheit) + " graus Fahrenheit")

#Exercício 4
nota1 = float(input("Escreva sua primeira nota: "))
nota2 = float(input("Escreva sua segunda nota: "))
nota3 = float(input("Escreva sua terceira nota: "))
nota4 = float(input("Escreva sua quarta nota: "))
media = (nota1 + nota2 + nota3 + nota4)/4
print("Sua média é: "+ str(media))

#Exercício 5
idadeEmAnos = int(input("Quantos anos você tem? "))
idadeEmMeses = idadeEmAnos*12
print("Você tem "+ str(idadeEmMeses)+" meses")

#Exercício 6 
precoQuilo = float(input("Qual o valor do quilo? "))
quantidadeQuilos = float(input("Quantos quilos você irá comprar? "))
precoTotal = precoQuilo * quantidadeQuilos
print("Irá custar "+ str(precoTotal) +" reais")