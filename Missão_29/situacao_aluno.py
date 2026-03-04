nota = float(input("Digite a nota final do aluno (0 a 10): "))
frequencia = float(input("Digite a frequência do aluno (0 a 100): "))

if nota < 0 or nota > 10:
    print("Nota inválida.")
elif frequencia < 0 or frequencia > 100:
    print("Frequência inválida.")
else:
    if frequencia < 75:
        print("Aluno reprovado por falta.")
    else:
        if nota >= 6:
            print("Aluno aprovado.")
        elif nota >= 4:
            print("Aluno em recuperação.")
        else:
            print("Aluno reprovado por nota.")