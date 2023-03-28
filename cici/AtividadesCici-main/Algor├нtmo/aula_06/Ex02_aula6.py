cargos = ["Escrituario", "Secretaria", "Caixa", "Gerente", "Diretor"]

while True:
    num = int(input("Digite o número correspondente ao seu cargo: "))
    if 1 <= num <= 5:
        print(cargos[num-1])
        break
    else:
        print("Digite um valor válido! 1, 2, 3, 4 ou 5.")
