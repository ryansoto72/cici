nome = input("Insira o nome do contribuinte: ")
cpf=int(input('Insira o CPF do contribuinte: '))
rend = float(input('Insira a renda anual: '))
dep = int(input('Quantidade de dependentes: '))

calc_dep = (dep*110)

if  rend <= 800: ali = 1
elif 800 < rend <= 4000: ali = 0.025
elif 4000 < rend <= 9000: ali = 0.05
else: ali = 0.1

print(f'O valor do imposto de renda será de {(rend-calc_dep)*ali:.2f}')
