traco = "=================================="
menu = "========= Menu de opções ========="
print(traco)
num1 = float(input("Digite o primeiro numero: "))
num2 = float(input("Digite o segundo numero: "))
print(traco)
option = {1:num1 + num2, 2:num1 * num2, 3:num1 - num2}
if num1 == 0 or num2 == 0:
    print(menu)
    cao = int(input("1-Somar dois números.\n2-Multiplicar dois números.\n3-Subtrair dois números.\nOpção: "))
    print(traco)
    while cao not in option.keys():
        print("Digite um numero valido! 1, 2 ou 3")
        print(menu)
        cao = int(input("1-Somar dois números.\n2-Multiplicar dois números.\n3-Subtrair dois números.\nOpção: "))
        print(traco)
else:
    option = {1:num1 + num2, 2:num1 * num2, 3:num1 - num2, 4:num1 /num2}
    print(menu)
    cao = int(input("1-Somar dois números.\n2-Multiplicar dois números.\n3-Subtrair dois números.\n4-Dividir dois números.\nOpção: "))
    print(traco)
    while cao not in option.keys():
        print("Digite um numero valido! 1, 2, 3 ou 4")
        print(menu)
        cao = int(input("1-Somar dois números.\n2-Multiplicar dois números.\n3-Subtrair dois números.\n4-Dividir dois números.\nOpção: "))
print("=-=-=-=-=-=- Resultado -=-=-=-=-=-")
print(f"Resposta: {option[cao]:.2f}")