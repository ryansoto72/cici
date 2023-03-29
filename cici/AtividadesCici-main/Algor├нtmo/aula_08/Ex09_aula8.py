medias = []
t=0
linha = '========================================='
rep = 10


for i in range(rep):
    print(linha)
    nota1 = float(input(f'Digite a primieira nota do {i+1}º aluno: '))
    nota2 =float(input(f'Digite a segunda nota do {i+1}º aluno: '))
    
    media = (nota1+nota2)/2
    medias.append(media)
print(linha)
for media_ind in medias:
    t += 1
    print(f'Media do {t}º aluno: {media_ind}')
print('-=-=-=-=-=-=-=-=-=-=-=-=-')
print(f'Media total: {sum(medias)/rep:.2f}')
