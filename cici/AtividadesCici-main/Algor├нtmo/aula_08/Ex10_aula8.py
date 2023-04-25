n = int(input('Digite  a quantitade de numeros: '))
pares = 0

for i in range(n):
    num = float(input('Digite um numero: '))
    if num % 2 == 0:
        pares += 1

print(f'Existem {pares} numeros pares.')