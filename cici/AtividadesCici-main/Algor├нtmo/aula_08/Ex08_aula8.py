med = 0
num = int(input('Digite a quantidade de valores: '))
for i in range(num):
    n = float(input(f'informe o {i+1}º valor: '))
    med += n

print(f'A media aritmedica dos valores sera: {med / num:.2f}')