altura = int(input("Digite  sual altura (em cm): "))

sexo = input("Digite seu sexo (M ou H): ").upper()
while sexo not in ("M", "H"):
    print("Digite um valor valido! (M ou H)")
    sexo = input("Digite seu sexo: ").upper()

altura_m = altura / 100
if sexo == "M":  (62.1*altura_m) - 44.7
else: calc =  (72.7*altura_m) - 58

print(f"Dado sua altura de {altura_m} metros, ")