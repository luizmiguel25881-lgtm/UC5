# divisao_zero.py

try:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    
    resultado = num1 / num2
    print(f"O resultado da divisão é: {resultado}")

except ValueError:
    print("Erro digite apenas um numero")

except ZeroDivisionError:
    print("não é possível dividir por zero")