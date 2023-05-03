med = 0
for i in range(1, 11):
    n1 = float(input(f'Digite a primieira nota do {i}º aluno: '))
    n2 =float(input(f'Digite a segunda nota do {i}º aluno: '))
    print(f"Media do aluno: {n1+n2/2:.1f}")
    med += n1+n2/2
print(f'-=-=-=-=-=-=-=-=-=-=-=-=-\nMedia total: {med/10:.2f}')
