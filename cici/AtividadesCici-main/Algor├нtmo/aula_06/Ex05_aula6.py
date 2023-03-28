diaria = {"A": 150.00, "B":100.00, "C":75.00, "D":50.00}

# A) entrada de dados basicos
nome_hospede = input("Digite o nome do hospede: ")
tipo_apartamento = input("Digite o tipo do apartamento(A, B, C ou D): ").upper()
while tipo_apartamento not in diaria.keys():
    print("Digite um valor valido!")
    tipo_apartamento = input("Digite o tipo do apartamento(A, B, C ou D): ").upper()
num_diarias = int(input("Digite o numero de diarias utilizadas: ")) 
valor_consumo = float(input("Digite o valor do consumo interno: "))

# B) calc diaria * dias 
total_diarias = num_diarias * diaria[tipo_apartamento]
# C) total + consumo
sub_total = total_diarias + valor_consumo
# D) calc de taxa de servico
taxa_senvico = sub_total + (sub_total * 0.1)
# E) soma de sub com taxa de servico
total_geral = taxa_senvico + sub_total
num_diarias = int(num_diarias)

# apresentacao dos resultados
print("===========================================")
print(f"Nome do hospede: {nome_hospede}")
print(f"Tipo do apartamento: {tipo_apartamento}")
print(f"Numero de diarias utilizadas: {num_diarias}")
print(f"Valor unitario da diaria: R$ {diaria[tipo_apartamento]:.2f}")
print(f"Valor total das diaria: R$ {total_diarias:.2f}")
print(f"Valor do consumo interno: R$ {valor_consumo:.2f}")
print(f"Subtotal: R$ {sub_total:.2f}")
print(f"Taxa de serviço: R$ {taxa_senvico:.2f}")
print(f"Total geral: R$ {total_geral:.2f}")
print("===========================================")





