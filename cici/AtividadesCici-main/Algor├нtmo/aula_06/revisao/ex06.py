
peso = float(input("Peso de peixes(quilos): "))
if peso >= 0:
    if peso > 50:
        excesso = peso - 50
        multa = 4.00 * excesso
    else:
        excesso = 0
        multa = 0
else: print('Peso deve ser um valor POSITIVO')
print(f"Peso: {peso} Kg\nExcesso: {excesso:.1f} Kg\nMulta: {multa:.2f}.")
