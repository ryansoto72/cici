age = int(input("Digite sua idade: "))

if 16 <= age < 18 or age > 65: 
    print("Eleitor Facultativo")
elif 18 <= age < 65: 
    print("Eleitor Obrigatorio")
else: 
    print("Nao eleitor") # age < 16
