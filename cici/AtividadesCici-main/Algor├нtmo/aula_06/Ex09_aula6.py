peso = int(input("Digite seu peso (em kg): "))
altura = int(input("Digite sua altura (em cm): "))

altura = altura / 100
massa = peso / (altura*2)

if massa < 26: 
    grau = "Normal"

elif 26 <= massa < 30: 
      grau = "Obeso"
  
else: 
      grau = "Obeso Morbido"
  
print(f"Com o peso de {peso} kilos e a altura de {altura} kg, o seu índice de massa corporal é {massa:.2f}, o que indica obesidade {grau}.")
