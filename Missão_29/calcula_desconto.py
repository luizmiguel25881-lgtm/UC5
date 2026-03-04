nome = input("Digite o nome do cliente: ")
valor = float(input("Digite o valor da compra: R$ "))

if valor < 100:
    desconto = 0
elif 100 <= valor <= 300:
    desconto = 0.10
else:
    desconto = 0.20

valor_desconto = valor * desconto
valor_final = valor - valor_desconto

if desconto > 0:
    print(f"\nParabéns, {nome}! Você ganhou {int(desconto*100)}% de desconto na sua compra!")
else:
    print(f"\n{nome}, sua compra não possui desconto.")

print(f"Valor da compra: R$ {valor:.2f}")
print(f"Valor final: R$ {valor_final:.2f}")

print("\nDeseja finalizar a sua compra?")
opcao = input("Digite 1 para SIM ou 2 para NÃO: ")

if opcao == "1":
    print("Compra feita com sucesso")
elif opcao == "2":
    print("Compra cancelada")
else :
    ("a opção invalida")
