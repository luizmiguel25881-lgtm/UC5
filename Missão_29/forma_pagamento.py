print("=== SISTEMA DE PAGAMENTO ===")
print("Escolha a forma de pagamento:")
print("1 → Pix (5% de desconto)")
print("2 → Crédito (sem desconto)")
print("3 → Débito (3% de desconto)")


valor = float(input("Digite o valor da compra: R$ "))


forma_pagamento = int(input("Digite a opção desejada: "))


if forma_pagamento == 1:
    desconto = valor * 0.05
    valor_final = valor - desconto
    print(f"Pagamento via Pix. Desconto de 5% aplicado.")
    print(f"Valor final: R$ {valor_final:.2f}")

elif forma_pagamento == 2:
    valor_final = valor
    print("Pagamento via Crédito. Sem desconto.")
    print(f"Valor final: R$ {valor_final:.2f}")

elif forma_pagamento == 3:
    desconto = valor * 0.03
    valor_final = valor - desconto
    print(f"Pagamento via Débito. Desconto de 3% aplicado.")
    print(f"Valor final: R$ {valor_final:.2f}")

else:
    print("Forma de pagamento inválida.")
