
peso = int(input("Peso de peixes(quilos): "))

if peso > 50:
    excesso = peso - 50
    multa = 4.00 * excesso
else:
    excesso = 0
    multa = 0

print(f"Peso: {peso} Kg\nExcesso: {excesso} Kg\nMulta: {multa:.2f}.")
