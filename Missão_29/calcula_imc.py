nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

if idade >= 0 and idade <= 12:
    classificacao = "criança"
elif idade >= 13 and idade <= 17:
    classificacao = "adolescente"
elif idade >= 18 and idade <= 59:
    classificacao = "adulto"
else:
    classificacao = "idoso"

print(f"{nome}, você tem {idade} anos e é {classificacao}.")