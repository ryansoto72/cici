# nome = input("Insira o nome do contribuinte: ")
# cpf = int(input('Insira o CPF do contribuinte (apenas numeros): '))
rend = float(input('Insira a renda anual: '))
dep = int(input('Quantidade de dependentes: '))

if rend >= 0 or dep >= 0:
    calc_dep = dep*110

    if  rend <= 800: ali = 1
    elif 800 < rend <= 4000: ali = 0.025
    elif 4000 < rend <= 9000: ali = 0.05
    else: ali = 0.1

    imposto = (rend-calc_dep)*ali

    if imposto <= 0:
        print('isento')
    else:
        print('teu imposto eh de: R$',imposto)
else: print('Valores invalidos')
#print(f'O valor do imposto de renda será de R${imposto:.2f}')
