cargo = {1:"Escrituario",2:"Secretaria", 3:"Caixa", 4:"Gerente", 5:"Diretor"}
codigo = int(input("Digite o codigo referente ao um cargo: "))

while codigo not in cargo.keys():
    print("Digite um codigo valido! 1, 2, 3, 4 ou 5")
    codigo = int(input("Digite o codigo referente ao um cargo: "))

print(f"Cargo q ce eh {cargo[codigo]}.")
