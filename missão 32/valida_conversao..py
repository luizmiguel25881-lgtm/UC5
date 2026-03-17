# valida_conversao.py

try:
    numero = int(input("Digite um número: "))
    print(f"você digitol o numero: {numero}")
except ValueError:
    print("algo deu errado digita o numero")