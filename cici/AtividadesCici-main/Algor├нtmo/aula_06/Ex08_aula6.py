altura_cm = int(input("Digite sua altura (em cm): "))
sexo = None

while sexo is None or sexo not in ("F", "M", "f", "m"):
    sexo = input("Digite seu sexo (M ou F): ").lower()

altura_m = altura_cm / 100

if sexo == "m": ideal = (72.7 * altura_m) - 58
else: ideal = (62.1 * altura_m) - 44.7 

if sexo == "m": sexo = "masculino" 
else: sexo = "feminino"

print(f"Para um {sexo} com {altura_cm} cm de altura, o peso ideal seria: {ideal:.2f} kg.") 
