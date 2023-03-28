linha = "-=-=-=-=-=-=-=-=-=-=-=-=-=-"
menu = "-=-=- MENU DE OPCOES -=-=-"
print(linha)
num1 = float(input("Digite o primeiro numero: "))
num2 = float(input("Digite o segundo numero: "))

if num2 == 0:
    gay = {1:"num1 + num2", 2:"num1 * num2", 3:"num1 - num2"}
    opcao = float(input(f"{menu}\n1- Somar dois números.\n2- Multiplicar dois números\n3- Subtrair dois números\nOpcao: "))
    while opcao not in gay.keys():
        print(linha)
        print("Opcao invalida!")
        opcao = float(print(f"{menu}\n1- Somar dois números.\n2- Multiplicar dois números\n3- Subtrair dois números\n\nOpcao: "))
else:
    gay = {1:"num1 + num2", 2:"num1 * num2", 3:"num1 - num2", 4:"num1 / num2"}
    opcao = float(input(f"{menu}\n1- Somar dois números.\n2- Multiplicar dois números\n3- Subtrair dois números\n4- Dividir dois números\nOpcao: "))
    while opcao not in gay.keys():
        print(linha)
        print("Opcao invalida!")
        opcao = float(print(f"{menu}\n1- Somar dois números.\n2- Multiplicar dois números\n3- Subtrair dois números\n4- Dividir dois números\nOpcao: "))
operacao = eval(gay[opcao])
print(f"{linha}\nResultado: {operacao}")