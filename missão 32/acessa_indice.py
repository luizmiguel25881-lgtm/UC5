# acessa_indice.py

nomes = []

# Lendo 5 nomes
for i in range(5):
    nome = input(f"Digite o {i+1}º nome: ")
    nomes.append(nome)

try:
    indice = int(input("Digite um índice para acessar a lista: "))
    print(f"Nome no índice {indice}: {nomes[indice]}")

except ValueError:
    print("algo de errado você deve digitar um número inteiro para o índice")

except IndexError:
    print(" índice não existe na lista")

# Verificação de nome na lista
nome_busca = input("Digite um nome para procurar na lista: ")

if nome_busca in nomes:
    print("Nome encontrado na lista!")
else:
    print("Erro: nome não encontrado")