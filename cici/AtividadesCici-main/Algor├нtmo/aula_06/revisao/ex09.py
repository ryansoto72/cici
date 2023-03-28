peso = int(input("Digite seu peso (em kg): "))
altura = int(input("Digite sua altura (em cm): "))

metro = altura / 100
massa = peso / altura*2

if massa >= 30: print("Obeso Morbido")
elif 26 <= massa > 30: print("Obeso")
else: print("Normal")
