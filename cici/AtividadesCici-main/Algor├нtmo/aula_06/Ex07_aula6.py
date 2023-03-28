num1 = None
num2 = None
num3 = None

while num1 is None or num1 <= 0:
    num1 = int(input("Digite o primeiro valor: "))

while num2 is None or num2 <= 0:
    num2 = int(input("Digite o segundo valor: "))

while num3 is None or num3 <= 0:
    num3 = int(input("Digite o terceiro valor: "))

maior = max(num1, num2, num3)

menor = min(num1, num2, num3)

media = (num1 + num2 + num3)/3

print("O maior numero é de: ", maior)
print("A menor numero é de: ", menor)
print("A media é de: ", media)
