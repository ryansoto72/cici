linhas = ('-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
apes = {"A":150.00, "B":100.00, "C":75.00, "D":50.00}
#-============== Entradas ====================-
nome = input("Digite o nome do hospede: ")
print(linhas)

ape = input("Digite o tipo do apartamento: ").upper()
while ape not in apes.keys():
    print(linhas,"\nDigite um valor valido! A, B, C ou D")
    ape = input("Digite o tipo do apartamento: ").upper()
print(linhas)

diarias= int(input("Digite o numero de diarias utilizadas: "))
while diarias <= 0:
    print(linhas,"\nO numero de diarias deve ser maior que 0.")
    diarias= int(input("Digite o numero de diarias utilizadas: "))
print(linhas)

consumo = int(input("Digite o valor de consumo interno: "))
while consumo < 0:
    print(linhas,"\nOValor de consumo interno nao pode ser negativo!")
    consumo = int(input("Digite o valor de consumo interno: "))
print(linhas)
#infelismente se alguem colocar uma letra no 'consumo' ou 'diarias' o codigo quebra#
print("-=-=-=-=-=-=-= Processo + Saida =-=-=-=-=-=-=-")
print(f"Nome do hospede: {nome}.\nTipo do apartamento: {ape}.")
print(f"Valor unitário da diária: R${apes[ape]:.2f}\nTotal das diarias: R${diarias * apes[ape]:.2f}\nConsumo interno: R${consumo:.2f}\n{linhas}\nSubtotal: R${(diarias * apes[ape])+consumo:.2f}\nTaxa de servico: R${((diarias * apes[ape])+consumo)*0.1:.2f}\nTOTAL GERAL: R${(((diarias * apes[ape])+consumo)*0.1)+((diarias * apes[ape])+consumo):.2f}\n{linhas}")


