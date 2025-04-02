nome = input("Digite seu nome:")
cpf = input("Digite seu cpf:")
telefone = input("Digite seu telefone:")
anoNascimento = str(input("Digite o ano do seu nascimento:"))
anoAtual = 2025
idade = anoAtual - anoNascimento
print("Seu nome é: "+ nome + ", seu cpf é "+ cpf +", seu telefone é "+ telefone + " seu ano de nascimento é " + anoNascimento + " e você fez/faz " + str(idade)+" anos" )
peso = float(input("Digite seu peso:"))
altura = float(input("Digite sua altura:"))
imc = peso/(altura*altura)
print("Seu IMC é igual a: "+ str(imc))