# entrada de dados
sal_min = float(input('Digite o salario minimo do funcionario: '))
                         # turno = input("Digite o turno de trabalho (M - Matutino, V - Vespertino ou N - Noturno): ").upper()
turno = input('-=-=-=-=-=-=-=-=-=-=-=-\n|   M - Matutino     |\n|   V - Vespertino   |\n|   N - Noturno      |\n-=-=-=-=-=-=-=-=-=-=-=-\n Digite a letra correspondente ao turno de trabalho: ').upper()
                         # categoria = input("Digite a categoria do funcionario (O - Operario ou G - Gerente): ").upper()
categoria = input('-=-=-=-=-=-=-=-=-=-=-=-\n|    O - Operario    |\n|    G - Gerente     |\n-=-=-=-=-=-=-=-=-=-=-=-\nDigite a letra correspondente à categoria do funcionário: ').upper()
horas_trab = int(input('Digite o numero de horas trabalhadas no mes do funcionario: '))

# caso erro finalizar codigo
if turno in ['M', 'V', 'N'] and categoria in ['O', 'G'] and sal_min >= 0 and horas_trab >= 0:

    #calc de coeficiente do salario
    coef_sal = sal_min * 0.1 if categoria == 'M' else sal_min * 0.15 if categoria == 'V' else sal_min * 0.12
    #calc sal_bruto
    sal_bruto = coef_sal/horas_trab if turno == 'M' else coef_sal/horas_trab if turno == 'V' else coef_sal/horas_trab
    #calc de imposto
    imposto = sal_bruto * 0.05 if categoria == 'O' and sal_bruto >= 300 else sal_bruto * 0.03 if categoria == 'O' else sal_bruto * 0.06 if categoria == 'G' and sal_bruto >= 400 else sal_bruto * 0.04
    #requisitor to gratification
    gratif = 50 if turno == 'N' and horas_trab > 80 else 30
    #auxilio alimentacao
    aux_alimento = 50 if categoria == 'O' and coef_sal <= 25 else 30
    #calc sal min
    sal_liq = sal_bruto - imposto + gratif + aux_alimento
    #classificacao
    classific = 'Mal remunerado' if sal_liq < 350 else 'Normal' if 350 <= sal_liq < 600 else 'Bem remunerado'
    
    print(f'-----------------------------------------------\n\tCoeficiente do Salario:\tR${coef_sal:.2f}\n\tSalario Bruto:\t\tR${sal_bruto:.2f}\n\tImposto:\t\tR${imposto:.2f}\n\tGratificação\t\tR${gratif}\n\tAuxílio-alimentação:\tR${aux_alimento}\n\tSalario Liquido:\tR${sal_liq:.2f}\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n\tClassificação:\t{classific}')

else: print('Valor invalido digitado!')
