import os

diaria = {"A": 150.00, "B": 100.00, "C": 75.00, "D": 50.00}

nome_hospede = input("Digite o nome do hospede: ")
os.system('cls' if os.name == 'nt' else 'clear')

tipo_apartamento = input("Digite o tipo do apartamento(A, B, C ou D): ").upper()
while tipo_apartamento not in diaria:
    os.system('cls' if os.name == 'nt' else 'clear')
    tipo_apartamento = input("Digite um tipo de apartamento valido (A, B, C ou D): ").upper()

num_diarias = None
while num_diarias is None:
    try:
        num_diarias = int(input("Digite o numero de diarias utilizadas: "))
        if num_diarias <= 0:
            print("O numero de diarias deve ser um valor positivo e maior que zero.")
            num_diarias = None
    except ValueError:
        print("O numero de diarias deve ser um valor numerico e inteiro.")
        num_diarias = None
os.system('cls' if os.name == 'nt' else 'clear')

valor_consumo = None
while valor_consumo is None:
    try:
        valor_consumo = float(input("Digite o valor do consumo interno: "))
        if valor_consumo < 0:
            print("O valor do consumo interno deve ser um valor positivo.")
            valor_consumo = None
    except ValueError:
        print("O valor do consumo interno deve ser um valor numerico.")
        valor_consumo = None
os.system('cls' if os.name == 'nt' else 'clear')

total_diarias = num_diarias * diaria[tipo_apartamento]
sub_total = total_diarias + valor_consumo
taxa_servico = sub_total * 0.1
total_geral = sub_total + taxa_servico

print("===========================================")
print(f"Nome do hospede: {nome_hospede}\nTipo do apartamento: {tipo_apartamento}\nNumero de diarias utilizadas: {num_diarias}\nValor unitario da diaria: R$ {diaria[tipo_apartamento]:.2f}\nValor total das diarias: R$ {total_diarias:.2f}\nValor do consumo interno: R$ {valor_consumo:.2f}\nSubtotal: R$ {sub_total:.2f}\nTaxa de servico: R$ {taxa_servico:.2f}\nTotal geral: R$ {total_geral:.2f}")
print("===========================================")
