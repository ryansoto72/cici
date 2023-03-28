media = float(input("Digite a media do aluno: "))

if media < 3:
    print("reprovado")
elif 3 <= media < 5:
    print("exame")
else: # media >= 5
    print("aprovado")