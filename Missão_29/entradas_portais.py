
numero = int(input("Digite um número para testar os portais: "))


if numero % 2 == 0:
    print("Portal 1 aberto! Número é par.")
    
    
    if numero % 3 == 0:
        print("Portal 2 aberto! Número é múltiplo de 3.")
        
        
        if 10 <= numero <= 30:
            print("Portal 3 aberto! Número está no intervalo.")
            print(" O COFRE MÁGICO FOI ABERTO!")
        else:
            print("Portal 3 bloqueado! Número fora do intervalo.")
    else:
        print("Portal 2 bloqueado! Número não é múltiplo de 3.")
else:
    print(" Portal 1 bloqueado! Número não é par.")