#try:
num1 = int(input("Digite primeiro valor:"))
num2 = int(input("Digite segundo valor:"))
num3 = int(input("Digite terceiro valor:"))
if num1 < 0 or num2 < 0 or num3 < 0:
    print('Os numeros devem ser positivos.')
else: print(f"========================\nMaior valor: {max(num1, num2, num3)}\nMenor valor: {min(num1, num2, num3)}\nMedia: {(num1 + num2 + num3)/3:.2f}")

#except ValueError: print('Valor deve ser NUMERO e INTEIRO')
