age = int(input("Digite sua idade: "))

if 16 <= age < 18 or age > 65: 
    #print("Eleitor Facultativo.")
    classe = "Eleitor Facultativo."

elif 18 <= age <= 65: 
    #print("Eleitor obrigatorio.")
    classe = "Eleitor obrigatorio."
    
else:
    #print("Nao Eleitor")
    classe = "Nao Eleitor"

print(f"Dado sua idade de: {age} anos\nSua classe eleitoral sera: {classe}")