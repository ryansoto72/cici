valores = []
num = int(input('Digite a quantidade de valores: '))
for i in range(num):
    valor = float(input(f'informe o {i+1}º valor: '))
    valores.append(valor)

print(f'A media aritmedica dos valores sera: {sum(valores) / num:.2f}')