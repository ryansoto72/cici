passou = 0
exame = 0
reprova = 0

for aluno in range(1, 61):
    
    n1 = float(input(f'Digite a priteira nota do {aluno}º aluno: '))
    n2 = float(input(f'Digimemte a segunda nota do {aluno}º aluno: '))

    med = (n1+n2)/2
    
    if med >= 5:
        print('aprovado')
        passou += 1
    elif med < 3:
        print('reprovado')
        reprova += 1
    else:
        print('exame')
        exame += 1

print(f'APROVADOS: {passou}\nREPROVADO: {reprova}\nEXAME: {exame}')